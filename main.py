# pip install requests
import requests
import os
import random
import string
import json
import threading

chars = string.ascii_letters + string.digits + '!@#$%^&*()'
random.seed(os.urandom(1024))

url_flush = ""
url_card = ""


def flush_database(url):
    email_endings = [
        "gmail.com",
        "yahoo.com",
        "outlook.com",
        "hotmail.com",
        "aol.com",
        "icloud.com",
        "mail.com",
        "zoho.com",
        "protonmail.com",
        "yandex.com"
    ]
    names = json.loads(open('names.json').read())

    for name in names:
        name_extra = ''.join(random.choice(string.digits))
        username = name.lower() + name_extra + "@" + random.choice(email_endings)
        password = ''.join(random.choice(chars) for i in range(random.randint(8, 14)))
        requests.post(url, allow_redirects=False, data={
            'username': username,
            'password': password
        })
        print(f'sending username {username} and password {password}')


def card_number_sending(url, thread_id):
    i = 0
    while True:
        i += 1
        status_code, response_text = send_post_request(url)
        print(f"Thread {thread_id} - Request {i}: Status Code = {status_code}")
        print(f"Thread {thread_id} - Money he lost: {i * 0.2:.1f}$")
        if i == 20:
            break


headers = {
    # will not give an example for this because it has some sensitive details
}

payload = {
    "captcha": "",
    "step": "",
    "IDNumber": "620721197305109531",
    "full": "name lastname",
    "one": "4940 7233 1497 0171",
    "two": "23/34",
    "three": "1234",
    "submit": ""
}


def send_post_request(url):
    response = requests.post(url, headers=headers, data=payload)
    return response.status_code, response.text


thread1 = threading.Thread(target=flush_database, args=(url_flush,))
thread1.start()

threads = []
for i in range(20):
    thread = threading.Thread(target=card_number_sending, args=(url_card, i+1))
    threads.append(thread)
    thread.start()

thread1.join()
for thread in threads:
    thread.join()

print(f"Go to https://safebrowsing.google.com/safebrowsing/report_phish and report the url")
