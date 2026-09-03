import requests

webhook = input("Webhook: ")
username = input("Username: ")

while True:
    message = input("Message: ")
    payload = {
                "content": message,
                "username": username,
            }
    response = requests.post(webhook, json=payload);
    print(response)
