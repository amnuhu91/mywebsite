import requests as rq 


def send_sms():
	url = "https://api.mtn.com/v2/messages/sms/outbound"

	payload = {
	    "senderAddress": "08064790955",
	    "receiverAddress": ["08162472682"],
	    "message": "this is from me Abubakar",
	    "clientCorrelator": "string12345"
	}
	headers = {
	    "Content-Type": "application/json",
	    #"Authorization": "",
	    "x-api-key":"HhYDrgnil2aKGHgrDnrNjfEI7LZuztP6"
	    #"secret_key":"S6gzEJX2z6otYGZL"
	    
	}

	response = rq.request("POST", url, json=payload, headers=headers)

	print(response.text)
send_sms()