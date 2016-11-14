try:
    import sys
    import imaplib
    import getpass
    import email
    import datetime
    import requests
    import json
    import googlemaps
    import datetime
    import time
    import xml
    import re
    import setup
    from getpass import getpass
    from validate_email import validate_email
except ImportError:
    setup.main()

'''
Uses imaplib to fetch emails.
Returns a dictionary of senders mapped to an array of emails they've sent.
'''

def getBySender(conn, numEmails):
    emails = {}
    conn.select('inbox')
    result, data = conn.uid('search', None, "ALL")
    if result == "OK":
        uid = data[0].split()
        if numEmails > len(uid):
            numEmails = len(uid)
        for i in range(0,numEmails):
            typ, data = conn.fetch(uid[i],'(RFC822)')
            msg = email.message_from_string(data[0][1])
            try:
                emails.setdefault(msg["from"], [])
                emails[msg["from"]].append(msg.get_payload(decode=1).replace('\n', ' ').replace('\r', ''))
                sys.stdout.write("\r%d emails fetched..." % i)
                sys.stdout.flush()
            except:
                pass
    print "\n"
    return emails

''' 
Extracts addresses from the body of emails using the SmartyStreets API.
Returns a dictionary with sender email addresses mapped to an ssociated address.
'''

def getSenderAddresses(emails, SSID, SSTOK):
    auth = {'auth-id': SSID, 'auth-token': SSTOK}

    senderAddresses = {}
    a = 1
    print "Extracting addresses..."
    for key, value in emails.iteritems():
        for i in value:
            r = requests.post('https://extract-beta.api.smartystreets.com', params=auth, data=i)
            try:
                response = json.loads(r.text)
                if response['addresses']:
                    destination = response['addresses'][0]['text']
                    senderAddresses[key] = re.sub("<.*?>", " ", destination)
                    a+=1
            except:
                pass
    return  senderAddresses


''' Prints driving directions from start to dest using the Google Maps API.'''
def getDirections(conn, start, dest):
    while True:
        try:
            now = datetime.datetime.now()
            directions_result = conn.directions(start,
                                                 dest,
                                                 departure_time=now)
        except:
            print "Invalid start or destination addresses"
            start = raw_input("Re-enter start address: ")
        else:
            break
    print "Route to " + dest
    print "   Total Distance: " + directions_result[0]['legs'][0]['distance']['text']
    print "   Total Duration: " + directions_result[0]['legs'][0]['duration']['text']
    steps = directions_result[0]['legs'][0]['steps']

    i = 1
    for step in steps:
        print str(i) + ". " + re.sub("<.*?>", "", step['html_instructions'])
        print "    Duration: " + step['duration']['text']
        print "    Distance: " + step['distance']['text']
        i+=1


def main():

    # SmartyStreet API crendentials
    SSID = "c23eec09-b403-4409-952d-9ad28035785a"
    SSTOK = "3UWB4JSlV3eo2yiM994h"
    # Google Maps API credentials
    GMKEY = "AIzaSyBK1u0qCRMmbnT5Y4Z9wEINbuyUjenF7ug"

    print
    print "This tool maps addresses mentioned in your email to contacts and gives you the option of receiving directions."
    print "For use with Gmail. Creating an application specific password is necessary.\n"

    # Input email credentials
    while True:
        emailAddress = raw_input("Gmail Address: ")
        while not validate_email(emailAddress):
            print '%s is not a valid email address.' % emailAddress
            print 'Please try again with proper email.'
            emailAddress = raw_input("Gmail Address: ")
        password = getpass("Application Specific Password:")
        try:
            mailConn = imaplib.IMAP4_SSL('imap.gmail.com')
            mailConn.login(emailAddress, password)
        except Exception, e:
            print "Error logging into Gmail: " + str(e)
            print "Please try again with proper credentials.\n"
        else:
            break

    # Input number of emails to be searched
    while True:
        numEmails = raw_input("Numbers of emails to search: ")
        try:
            int(numEmails)
        except:
            print "Please input a number."
        else:
            break

    # Get emails organized by sender in a dictionary
    emailsBySender = getBySender(mailConn, int(numEmails))

    if len(emailsBySender) <= 0:
        print "No emails found."
        sys.exit(0)

    # Extract addresses from emails and map them to senders
    senderAddresses = getSenderAddresses(emailsBySender, SSID, SSTOK)

    # Check if any addresses where found in the emails
    # If not, ask for higher number of emails to search
    while len(senderAddresses) == 0:
        print "No addresses found."
        print "Search more emails."
        while True:
            numEmails = raw_input("Numbers of emails to search: ")
            try:
                int(numEmails)
            except:
                print "Please input a number."
            else:
                break
        # Fetch new number of emails
        emailsBySender = getBySender(mailConn, int(numEmails))
        # Search new emails for addresses
        senderAddresses = getSenderAddresses(emailsBySender, SSID, SSTOK)


    # Flatten dictionary into an array of tuples [(email address, address),...]
    senderAddresses = senderAddresses.items()

    # Input starting address
    start = raw_input("Starting location: ")
    i = 0
    while True:
        # Print out all email address to address mappings
        for tuple in senderAddresses:
            print "["+str(i)+"] " + tuple[0]
            print "     " + tuple[1]
            i+=1
        i=0

        # Select destination
        while True:
            destNum = raw_input("Directions to: ")
            try:
                int(destNum)
                senderAddresses[int(destNum)]
            except:
                print "Please input a valid number."
            else:
                break
        dest = senderAddresses[int(destNum)][1]

        # Connect to Google Maps API
        mapsConn = googlemaps.Client(key= GMKEY)

        # Print directions from start address to destination
        getDirections(mapsConn, start, dest)

        raw_input("Press Return to for more locations or Ctrl+C to exit. ")

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print "\nExiting."
    sys.exit(0)
