import pandas as pd
import re, json, requests

url = 'https://raw.githubusercontent.com/Biuni/PokemonGO-Pokedex/master/pokedex.json'

resp = requests.get(url)
resp_parsed = re.sub(r'^jsonp\d+\(|\)\s+$', '', resp.text)
data = json.loads(resp_parsed)

df = pd.json_normalize(data['pokemon'])
df = pd.DataFrame(df)

# Q1. Get all Pokemons whose spawn rate is less than 5%
spawn_rate_is_less_than_5 = df[df['spawn_chance'] < 5]

# Q2. Get all Pokemons that have less than 4 weaknesses
less_than_4_weaknesses = df[df['weaknesses'].apply(lambda x: len(x)) < 4]

# Q3. Get all Pokemons that have no multipliers at all
no_multipliers = df[df['multipliers'].isna()]

# Q4.Get all Pokemons that do not have more than 2 evolutions
No_Evolution = df[df['next_evolution'].isnull()]

# Q6. Get all Pokemon who have more than two types of capabilities
capabilities = df[df['type'].apply(lambda x: len(x)) > 2]