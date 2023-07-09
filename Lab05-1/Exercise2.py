import requests
import json

url = "https://michaelgathara.com/api/python-challenge"

response = requests.get(url)

challenges = response.json()

print(challenges)

#Desired output
print("Name - Sathvik Chiluvuri")

print("Blazer Id - SCHILUVU")

#Challenges is a list so iterate through each loop
for i in challenges:
    #Now in each iteration we have a dicionary and keyword is problem so using the keyword we can access its pair
    #eval is used for evaluating expressions and in pair we have ? replaces with ""
    print(i," -> Desired Output = ",eval(i["problem"].replace("?","")))
