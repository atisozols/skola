# https://api.funtranslations.com/translate/yoda.json?text=Master%20Obiwan%20has%20lost%20a%20planet.

import requests

text = input("input your text\n")
text = text.replace(" ", "%20")



response = requests.get("https://api.funtranslations.com/translate/yoda.json?text=" + text)

yoda = response.json()

print(yoda)