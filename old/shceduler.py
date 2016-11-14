from boto.s3.connection import S3Connection
from boto.s3.key import Key
import datetime
import pandas as pd
import numpy as np
import time 
import pg
import ConfigParser
from StringIO import StringIO 
import sys
import re
import os 
import optparse
import subprocess
import glob




config = ConfigParser.SafeConfigParser()
config.read(sys.argv[1])

def concat_files(input_directory, output_directory):

	print "Concatenating files..."

	


	p = subprocess.Popen("fpart -s 250000000 -o part " + input_directory    ,shell=True)  
	p.wait()

	part_list = glob.glob(output_directory+"/part.*")

	print part_list
	i = 0
	concat_list = []

	for part in part_list:
		ts = datetime.datetime.now().isoformat().replace(':','.')
		file_name =  "concat_" + str(i) + "_"  + ts
		print  "cat " + part + " | xargs -n 32 -P 8 cat >> " + output_directory + "/" + file_name 
	 	p = subprocess.Popen("cat " + part +  " |  xargs -n 32 -P 8 cat >> " + output_directory + "/" + file_name   ,shell=True)  
		p.wait()
		concat_list.append(output_directory + "/" + file_name )
		i = i+1


	return  concat_list



def transform_data(file_name, output_directory):
	
	header = config.get('db','header').split(",\n")

	format_time = lambda x: str(x)[0:4] + '-'+ str(x)[4:6]+ '-'+str(x)[6:8] + ' ' + str(x)[8:10]  + ':' + str(x)[10:12] + ':'+ str(x)[12:14]  

	df =pd.DataFrame()
	df = pd.read_csv(file_name, names=header,  delim_whitespace=True, error_bad_lines= False)
	# d.phone_ID =  first_file.replace(".csv",'')
	df.set_index ( df.timestamp.apply(format_time), inplace=True )
	del df['timestamp']	

	print "Dataframe loaded..."
		
	print "Transforming files..."

	#coerce columns to numeric (incase of garbage values)
	df['power_source'] = df['power_source'].convert_objects(convert_numeric='force')
	df['power_source'].fillna(0,inplace=True)
	df['power_source'] = df['power_source'].astype(int)
	
	df['battery_level'] = df['battery_level'].convert_objects(convert_numeric='force')
	df['battery_level'].fillna(0,inplace=True)
	df['battery_level'] = df['battery_level'].astype(int)

	df['wifi_signal_strength'] = df['wifi_signal_strength'].convert_objects(convert_numeric='force')
	df['wifi_signal_strength'].fillna(0,inplace=True)
	df['wifi_signal_strength'] = df['wifi_signal_strength'].astype(int)


	df['duration'] = df['duration'].convert_objects(convert_numeric='force')
	df['duration'].fillna(0,inplace=True)
	df['duration'] = df['duration'].astype(int)

	df['bytes_cellular'] = df['bytes_cellular'].convert_objects(convert_numeric='force')
	df['bytes_cellular'].fillna(0,inplace=True)
	df['bytes_cellular'] = df['bytes_cellular'].astype(int)

	df['bytes_non_cellular'] = df['bytes_non_cellular'].convert_objects(convert_numeric='force')
	df['bytes_non_cellular'].fillna(0,inplace=True)
	df['bytes_non_cellular'] = df['bytes_non_cellular'].astype(int)

	df['m87_signal_strength'] = df['m87_signal_strength'].convert_objects(convert_numeric='force')
	df['m87_signal_strength'].fillna(0,inplace=True)
	df['m87_signal_strength'] = df['m87_signal_strength'].astype(int)	

	df['cellular_signal_strength'] = df['cellular_signal_strength'].convert_objects(convert_numeric='force')
	df['cellular_signal_strength'].fillna(0,inplace=True)
	df['cellular_signal_strength'] = df['cellular_signal_strength'].astype(int)	
	
	df = df[df.cellular_signal_strength > 0]
	df = df[df.m87_signal_strength > 0]

	#map 0,1,2 to none,node,gateway
	df['node_type'].replace(0, "none", inplace=True)
	df['node_type'].replace(1, "node", inplace=True)
	df['node_type'].replace(2, "gateway", inplace=True)
	#remove -1 from node_type
	df = df[df.node_type != -1]

	#duration
	df['none_duration'] = df['duration'].where(df['node_type']=='none')
	df['none_duration'].fillna(0,inplace=True)
	df['none_duration'] = df['none_duration'].astype(int)

	df['node_duration'] = df['duration'].where(df['node_type']=='node')
	df['node_duration'].fillna(0,inplace=True)
	df['node_duration'] = df['node_duration'].astype(int)
	
	df['gateway_duration'] = df['duration'].where(df['node_type']=='gateway')
	df['gateway_duration'].fillna(0,inplace=True)
	df['gateway_duration'] = df['gateway_duration'].astype(int)

	#calculate bytecount 
	df['none_bytes']= df['bytes_cellular'].where(df['node_type'] == 'none')	
	df['none_bytes'].fillna(0,inplace=True)
	df['none_bytes'] = df['none_bytes'].astype(int)

	df['node_bytes']= df['bytes_non_cellular'].where(df['node_type'] == 'node')	
	df['node_bytes'].fillna(0,inplace=True)
	df['node_bytes'] = df['node_bytes'].astype(int)

	df['gateway_bytes']= (df['bytes_cellular'].where(df['node_type']=='gateway') - df['bytes_non_cellular'].where(df['node_type']=='gateway'))
	df['gateway_bytes'].fillna(0,inplace=True)
	df['gateway_bytes'] = df['gateway_bytes'].astype(int)

	df['m87_signal_strength_inter'] = df['cellular_signal_strength'].where(df['node_type']=='none')
	df['m87_signal_strength_inter'].fillna(0,inplace=True)
	df['m87_signal_strength_inter'] = df['m87_signal_strength_inter'].astype(int)

	#fills in null values (where M87 signal strenght is empty) with corresponding values in cellular_signal_strength
	df['m87_signal_strength'] = df['m87_signal_strength'] + df['m87_signal_strength_inter'].astype(int)
	del df['m87_signal_strength_inter']
	

	#m87 gain when device is in node mode
	df['m87_gain'] = ( df['m87_signal_strength'].where(df['node_type']=='node') - df['cellular_signal_strength'].where(df['node_type']=='node')  ) *2
	df['m87_gain'].fillna(0, inplace=True)
	df['m87_gain'] = df['m87_gain'].astype(int)

	df['mss_node'] = df['m87_signal_strength'].where(df['node_type']=='node') *2
	df['mss_node'].fillna(0, inplace=True)
	df['mss_node'] = df['mss_node'].astype(int)
	
	df['css_node'] = df['cellular_signal_strength'].where(df['node_type']=='node') *2
	df['css_node'].fillna(0, inplace=True)
	df['css_node'] = df['css_node'].astype(int)

	#remove 0 and negative values



	ts = datetime.datetime.now().isoformat().replace(':','.')
	# print df
	#concatenate file name and write to csv 
	file_name =  output_directory + "/transformed_" + ts + '.csv'
	df.to_csv(file_name)
	print file_name
	return file_name


#uploafd data to specified S3 bucket given the file path
def upload_data(file, bucket):

	print 'Uploading to S3...'
	k = Key(bucket)
	k.key = file	
	k.set_contents_from_filename(file, reduced_redundancy=True)		

def delete_data(file,bucket):

	print "Deleting " + file_name + " from S3..."
	k = Key(bucket)
	k.key = file	
	k.delete_key(file)	


def to_db(db, user, host, port, password, table, bucket_name, aws_access_key_id, aws_secret_access_key, file_name):

	conn = pg.connect(dbname=db, user=user, host=host, port=int(port), passwd= password)
	print "connected to db"



	insert_query =  '''copy %(table)s
					   from 's3://%(bucket_name)s/%(file_name)s'
					   credentials 'aws_access_key_id=%(aws_access_key_id)s;aws_secret_access_key=%(aws_secret_access_key)s'
				       delimiter ','
				       csv
					   ignoreheader 1	
					   maxerror 250;
				''' % { "table": table, 'bucket_name' : bucket_name, 'file_name' : file_name, 'aws_access_key_id': aws_access_key_id, 'aws_secret_access_key': aws_secret_access_key }


	print insert_query
	conn.query(insert_query)
	conn.query('END;')
	print "Added to database."



def main():


	#Set variables
	#S3
	start = time.time()
	client_bucket = config.get('S3','client_bucket')
	# print client_bucket
	s3_id = config.get('S3','s3_id')
	s3_key = config.get('S3','s3_key')
	#Redshift
	db=config.get('db','db_name')
	user=config.get('db','user')
	host=config.get('db','host')
	port=config.get('db','port')
	password=config.get('db','password')
	table = config.get('db','table')
	
	input_directory = config.get('folders','input_directory')
	output_directory = config.get('folders','output_directory')

	# file_list = glob.glob(input_directory+"/*.csv")
	# print file_list
	concated_files = concat_files(input_directory, output_directory)
	
	for file in concated_files:
		transformed_moe = transform_data(file, output_directory)


	# connected to S3 buckets
	try:
		conn = S3Connection(s3_id, s3_key)
		bucket = conn.get_bucket(client_bucket)
		print "Connected to " + client_bucket
	except:
		print "Error connecting to S3."
		print "Enter correct credentials in config.ini and restart the script"

	# upload_data(transformed_moe, bucket)	
	# to_db(db,user,host,port,password,table, bucket, s3_id, s3_key, transformed_moe)

	# os.remove(output_directory + '/' + concated_file)
	# os.remove(output_directory + '/' + transformed_moe)
	# delete_data(transformed_moe, bucket)

	# for f in file_list:
	# 	os.remove(f)

	end = time.time()
	print end - start

if __name__ == '__main__':
	main()