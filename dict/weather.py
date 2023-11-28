import requests

url = "https://weatherapi-com.p.rapidapi.com/forecast.json"

city = input("city: ")

querystring = {"q":city,"days":"3"}

headers = {
	"X-RapidAPI-Key": "a6108fdc97msh60c32ab6027c096p1c6364jsn95a40d24770d",
	"X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

res = response.json()

forecast = res['forecast']['forecastday']


for i in range(3):
    print(forecast[i]['date'], forecast[i]['day']['condition']['text'], 'and', forecast[i]['day']['avgtemp_c'], 'degrees')