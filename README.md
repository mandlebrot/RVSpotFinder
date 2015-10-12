# Code for Issue #4

### Dependencies

- [Twilio-python](https://github.com/twilio/twilio-python) library
- [Pipedrive wrapper](https://github.com/mandlebrot/RVSpotFinder/tree/master/pipedrive)

### What this code does:

- Initiates a call to a given number, from given Twilio number
- Creates a new activity corresponding to the call in Pipedrive

### What this code does not (yet) do:

- opens a window to edit the activity in Pipedrive


##### Ideas for further development:

Hopefully your dev team will be be able to trigger this code through 
the website, which I do not have access to. Otherwise, I can begin
writing an application in order to do this.

Additionally, creating a pop-up when the link is clicked which 
redirects to the newly created activity could likely be done more 
efficiently directly through HTML.
