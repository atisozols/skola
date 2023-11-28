import requests
response = requests.get('https://randomuser.me/api/').json()
print(response['results'][0]['name']['first'], response['results'][0]['name']['last'])


# response = requests.get("https://api.agify.io?name=atis")
# response = response.json()

# response = requests.get("https://api.agify.io?name=atis").json()


obj = {
    'age': 56,
    'name': 'atis',
    'interests': [
        {
            'name': 'sports',
            'type': 'activity'    
        },
        {
            'name': 'tv',
            'type': 'media consumption'    
        }
    ]
}

# print(obj['interests'][0]['type'])




