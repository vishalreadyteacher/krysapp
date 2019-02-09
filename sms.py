from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
import csv, sys 
from twilio.rest import TwilioRestClient
numbers = []

# Twilio: Find these values at https://twilio.com/user/account
account_sid = "AC1463097da80581b34636d0b4224fadc6"
auth_token = "05bed2172cf091a21961f32acb9af54e"
from_num = "+61488842902"          # 'From' number in Twilio
app = Flask(__name__)
@app.route("/sms", methods=['GET', 'POST'])
def incoming_sms():
    """Send a dynamic reply to an incoming text message"""
    # Get the message the user sent our Twilio number
    
    body = request.values.get('Body', None)
    num = request.values.get('From')
    if num == '+61469069668' and body == 'BEGIN' :
    	start(body,num)
    elif num == '+61469069668'and body == 'BSEND' :
     	delay_sms()

def start(body,num):

    # Start our TwiML response
    resp = MessagingResponse()

    # Determine the right reply for this message
    if body == 'YES':
        resp.message("Thank you for the interest. We will get back to you shortly!!")
        print(num)
        insert(num)
    else:
        resp.message("Please reply with YES")

    
    return str(resp)

def insert(numb): 
	log_file = open('numbers.txt', 'a')
	log_file.write(numb + "\n")


def delay_sms():
	# Open the people CSV and get all the numbers out of it
	with open("numbers.txt","r") as f:
	    text = f.readlines()
	for line in text:
	    numbers.append(line)

	    # Set up Twilio client
	client = TwilioRestClient(account_sid, auth_token)

	    # Send the messages
	for num in numbers:
	        # Send the sms text to the number from the CSV file:
	    print("Sending to " + num)
	    sms = "click the link to registere: https://zfrmz.com/pTLqav1zvJufuDlnVNl4?mobile=" + num
	    print(sms)
	    message = client.messages.create(to=num, from_=from_num, body=sms)


if __name__ == "__main__":
    app.run(debug=True)