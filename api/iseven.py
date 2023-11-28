import requests

num = input('sk: ')

res = requests.get('https://api.isevenapi.xyz/api/iseven/' + num)

result = res.json()

print(result['iseven'])