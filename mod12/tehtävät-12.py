import json
import requests

#tehtävä-1
pyyntö = "https://api.chucknorris.io/jokes/random"

try:
    vastaus = requests.get(pyyntö)
    print('Status code', vastaus.status_code)
    if vastaus.status_code==200:
        data = vastaus.json()
        print(json.dumps(data, indent=2))
        print(data['value'])
except requests.exceptions.RequestException as e:
    print(e)
    print ("Hakua ei voitu suorittaa.")


#tehtävä-2

