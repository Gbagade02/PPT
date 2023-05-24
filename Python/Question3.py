import pandas as pd
import re, json, requests

url = 'https://raw.githubusercontent.com/Biuni/PokemonGO-Pokedex/master/pokedex.json'

resp = requests.get(url)
resp_parsed = re.sub(r'^jsonp\d+\(|\)\s+$', '', resp.text)
data = json.loads(resp_parsed)

df = pd.json_normalize(data['pokemon'])
df.to_excel("Pokemon.xlsx") 