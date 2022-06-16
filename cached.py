import requests
import requests_cache

session = requests.Session()

def req():
    for i in range(60):
        session.get('http://httpbin.org/delay/1')

print("calling req")
#req()
def cach():
    sessions = requests_cache.CachedSession('demo_cache')
    for i in range(60):
        sessions.get('http://httpbin.org/delay/1')

print("callingcach")

cach()