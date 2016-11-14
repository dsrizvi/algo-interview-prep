import sys
import imaplib
import getpass
import email
import datetime
import pprint
import requests
import json
import googlemaps
import datetime

payload = {'auth-id': "c23eec09-b403-4409-952d-9ad28035785a", 'auth-token': '3UWB4JSlV3eo2yiM994h'}



mail = imaplib.IMAP4_SSL('imap.gmail.com')
# imaplib module implements connection based on IMAPv4 protocol
mail.login('d.s.rizvi@gmail.com', 'hafehkxnhayvkicj')
# >> ('OK', [username at gmail.com Vineet authenticated (Success)'])

mail.select('inbox') # Connected to inbox.
result, data = mail.uid('search', None, "ALL")



msg_by_sender =  {}
sender_address = {}
uid = data[0].split()
# print uid
# for id in uid[::-1]:
# 	typ, data = mail.fetch(id,'(RFC822)')
# 	# msg = email.message_from_string(data[0][1])

for i in range(0,1000):
	typ, data = mail.fetch(uid[i],'(RFC822)')
	msg = email.message_from_string(data[0][1])
	# print msg.get_payload()
	try:
		msg_by_sender.setdefault(msg["from"], [])
		msg_by_sender[msg["from"]].append(msg.get_payload(decode=1).replace('\n', ' ').replace('\r', ''))
	except:
		pass

	# print msg_by_sender

for key, value in msg_by_sender.iteritems():
	for i in value:
		# print i
		r = requests.post('https://extract-beta.api.smartystreets.com', params=payload, data=i)
		# print r.text
		try:
			response = json.loads(r.text)
			if response['addresses']:
				destination = response['addresses'][0]['text']
				sender_address[key] = str(destination).replace("<br />","")
		except:
			pass
		# print key

for key, value in sender_address.iteritems():
	print "Contact: " + key
	print "Address: " + value

