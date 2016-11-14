import requests
import json
import googlemaps
import datetime

string = "sky being blue? in the world is true? jackfroast nipping on the firehead"
payload = {'auth-id': "c23eec09-b403-4409-952d-9ad28035785a", 'auth-token': '3UWB4JSlV3eo2yiM994h'}
r = requests.post('https://extract-beta.api.smartystreets.com', params=payload, data=string)
response = json.loads(r.text)
# print response
if response['addresses']:
	destination = response['addresses'][0]['text']
	print destination

# start = "2100 Squire Dobbins Drive Sugar Land, TX"
# end = "12722 Paleo Ct. Sugar Land, TX"


# gmaps = googlemaps.Client(key='AIzaSyBK1u0qCRMmbnT5Y4Z9wEINbuyUjenF7ug')
# now = datetime.datetime.now()
# directions_result = gmaps.directions(start,
#                                      end,
#                                      mode="walking",
#                                      departure_time=now)
# # directions_result = json.loads(directions_result)
# # print json.dumps(directions_result, indent=4, sort_keys=True)
# print "Route to " + end
# print "   Total Distance: " + directions_result[0]['legs'][0]['distance']['text']
# print "   Total Duration: " + directions_result[0]['legs'][0]['duration']['text']
# steps = directions_result[0]['legs'][0]['steps']

# i = 1
# for step in steps:
# 	print str(i) + ". " + step['html_instructions'].replace('<b>', '').replace('</b>','')
# 	print "   Duration: " + step['duration']['text']
# 	print "   Distance: " + step['distance']['text']
# 	i+=1