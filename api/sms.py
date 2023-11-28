import requests

url = "https://matchilling-tronald-dump-v1.p.rapidapi.com/random/quote"

headers = {
	"Accept": "application/hal+json",
	"X-RapidAPI-Key": "a6108fdc97msh60c32ab6027c096p1c6364jsn95a40d24770d",
	"X-RapidAPI-Host": "matchilling-tronald-dump-v1.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers)

print(response.json()["value"], end="")