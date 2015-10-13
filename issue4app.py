import os

from clicktocall.app import app


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    if port == 5000:
        app.debug = True
    app.run(host='0.0.0.0', port=port)

from pipedrive import Pipedrive

pd = Pipedrive('Pipedrive_login')      # PD login info

print call.sid
print call.duration

new = pd.activities.post({       # create corresponding activity
    "subject": "click_to_call",
    "type": "call",
    "duration": call.duration,
    "deal_id": "693"
    })

print new.id
