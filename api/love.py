import requests

url = "https://love-calculator.p.rapidapi.com/getPercentage"

m = input("Ievadi savu vardu! ")
f = input("Ievadi savas milotas sievietes vardu! ")

querystring = {"sname":m,"fname":f}

headers = {
	"X-RapidAPI-Key": "a6108fdc97msh60c32ab6027c096p1c6364jsn95a40d24770d",
	"X-RapidAPI-Host": "love-calculator.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

data = response.json()['percentage']
print(data + "%")