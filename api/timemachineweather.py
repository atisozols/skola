import requests

url = "https://dark-sky.p.rapidapi.com/56.969664, 23.153190,2019-02-20"

headers = {
	"X-RapidAPI-Key": "a6108fdc97msh60c32ab6027c096p1c6364jsn95a40d24770d",
	"X-RapidAPI-Host": "dark-sky.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers)

print(response.text)