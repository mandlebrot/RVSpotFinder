from twilio.rest import TwilioRestClient
 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "ACfeab90b395875933e09b902c3886c426"
auth_token  = "5a4c2ac221f703dd091f9c9c92f54c55"
client = TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(body="Test",
    to="+13038065253",    # Replace with your phone number
    from_="+15005550006") # Replace with your Twilio number

print message.sid
