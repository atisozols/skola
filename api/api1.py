import requests

name = input("name: ")
response = requests.get("https://api.agify.io?name=" + name)
response = response.json()

print(response['age']) # {'age': 57, 'count': 277, 'name': 'atis'}
