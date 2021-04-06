import requests

url = "https://deezerdevs-deezer.p.rapidapi.com/search"

querystring = {"q": "matuê"}

headers = {
    'x-rapidapi-key': "65974055c3msh69184b63aaae0aap1937bcjsnf744c11eab81",
    'x-rapidapi-host': "deezerdevs-deezer.p.rapidapi.com"
    }

response = requests.get("GET", url, headers=headers, params=querystring)

for c in response:
    print(response.json())
    exit()