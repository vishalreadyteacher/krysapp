from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
import os


app = Flask(__name__)
@app.route("/sms", methods=['GET', 'POST'])
def incoming_sms():
    """Send a dynamic reply to an incoming text message"""
    # Get the message the user sent our Twilio number
    
    body = request.values.get('Body', None)
    num = request.values.get('From')
    #if num == "+61469069668" and body == "ENDD":
    if body == "Blah" :
    	os.system("python main.py")
    else:
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

if __name__ == "__main__":
    app.run(debug=True)