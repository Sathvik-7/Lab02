import requests
import json

url = "https://michaelgathara.com/api/python-challenge"

response = requests.get(url)

challenges = response.json()

print(challenges)

print("Name - Sathvik Chiluvuri")

print("Blazer Id - SCHILUVU")

for i in challenges:
    print(i,"->",eval(i["problem"].replace("?","")))
