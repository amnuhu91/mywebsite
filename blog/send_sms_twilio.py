from twilio.rest import Client 
 
account_sid = 'AC77c58d059917dee5f2198c168f66d8b2' 
auth_token = '10c70247d9cd5be501732a956fc53385' 


# client = Client(account_sid, auth_token)

# message = client.messages \
#                 .create(
#                      body="Join Earth's mightiest heroes. Like Kevin Bacon.",
#                      from_='+18508217243',
#                      to='+2348064790955'
#                  )

# print(message)

#+18508217243


#account_sid = 'AC77c58d059917dee5f2198c168f66d8b2' 
#auth_token = '[AuthToken]' 



def send_whatsapp_message(msg,sender='+14155238886',receiver='+2348064790955'):
    client = Client(account_sid, auth_token) 
 
    message = client.messages.create( 
                              from_=f'whatsapp:{sender}',  
                              body=msg,      
                              to=f'whatsapp:{receiver}' 
                          ) 
    #print(message.sid)

#send_whatsapp_message(msg="welcome to new world")
 