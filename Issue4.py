from pipedrive import Pipedrive
from twilio.rest import TwilioRestClient

pd = Pipedrive('dc8fe731bb412373b21482cdb0a8a73c265afb18')      # PD login info

# Twilio login info
account = "ACfeab90b395875933e09b902c3886c426"
token = "5a4c2ac221f703dd091f9c9c92f54c55"
client = TwilioRestClient(account, token)

call = client.calls.create(             # create new call
    to="+13038065253",
    from_="+15005550006",
    url="http://twimlets.com/holdmusic?Bucket=com.twilio.music.ambient")

print call.sid
print call.duration

new = pd.activities.post({       # create corresponding activity
    "subject": "click_to_call",
    "type": "call",
    "duration": call.duration,
    "note": "test1",
    "deal_id": "693"
    })

print new.id
