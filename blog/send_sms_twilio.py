from twilio.rest import Client 
 
account_sid = 'AC77c58d059917dee5f2198c168f66d8b2' 
auth_token = '5955a2ea52879ab2886a6ef7494d3fa5' 

 
# Download the helper library from https://www.twilio.com/docs/python/install



# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
#account_sid =  #os.environ['TWILIO_ACCOUNT_SID']
#auth_token = #os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_='+18508217243',
                     to='+2348064790955'
                 )

print(message)

#+18508217243