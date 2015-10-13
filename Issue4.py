from pipedrive import Pipedrive
from twilio.rest import TwilioRestClient

pd = Pipedrive('pd_token')      # PD login info

# Twilio login info
account = "twilio_login"
token = "twilio_token"
client = TwilioRestClient(account, token)

call = client.calls.create(             # create new call
    to="client_phone",
    from_="+15005550006",
    url="http://twimlets.com/holdmusic?Bucket=com.twilio.music.ambient")

print call.sid
print call.duration

new = pd.activities.post({       # create corresponding activity
    "subject": "click_to_call",
    "type": "call",
    "duration": call.duration,
    "deal_id": "693"
    })

print new.id
