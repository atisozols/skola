import requests

url = "https://football-prediction-api.p.rapidapi.com/api/v2/predictions"

querystring = {"market":"classic","iso_date":"2022-12-07"}

headers = {
	"X-RapidAPI-Key": "a6108fdc97msh60c32ab6027c096p1c6364jsn95a40d24770d",
	"X-RapidAPI-Host": "football-prediction-api.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)
print(response.text)

for game in response.json()["data"]:
    print(game["home_team"], "vs", game["away_team"], game["prediction"], game["season"])