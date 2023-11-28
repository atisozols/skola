import requests

response = requests.get('http://universities.hipolabs.com/search?country=Latvia')
response = response.json()
# print(response)
names = []

for school in response:
    names.append(school['name'])
    
names.sort()

for name in names:
    print(name)