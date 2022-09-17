import requests

url = "https://pokeapi.co/api/v2/pokemon?limit=151"

response = requests.get(url)
if response.status_code != 200:
    print("Fk, work better", response.text)
else:
    data = response.json()
    
    for pokemon in data['results']:
        print(pokemon['name'].capitalize())