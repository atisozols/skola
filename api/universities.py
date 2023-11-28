import requests

country = input("ievadi valsti: ")
response = requests.get("http://universities.hipolabs.com/search?country=" + str(country))

schools = response.json()

for school in schools:
    print(school['name'],"|", school['domains'][0])



