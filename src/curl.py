import urllib.request, json

with urllib.request.urlopen("http://pogoapi.net/api/v1/pokemon_names.json") as url:
    data = json.loads(url.read().decode())
    for i in range(len(data)):
        print(data[i])