import requests


api_key = "afe93d1a9da34815947707f91bef5284"
country = "ng"
url = f"https://newsapi.org/v2/top-headlines?country={country}&apiKey={api_key}"
try:
	res = requests.get(url, timeout = 5)
	
except Exception as e:
	print("request timeout")
else:
	print("request not timeout")
	print(res.text)
finally:
	pass

#news = res.json()
#print(news["articles"][0])

