import requests

URL = 'https://api.pokemonbattle.me/v2'
token = '9b5b8bfb350c9a3558474358e3d10b24'
HEADER = {'Content-Type' : 'application/json', 'trainer_token': token}

body_generate = {
    "name": "generate",
    "photo": "generate"
}

body_id = {
    "pokemon_id": "26361"
}

body_shift = {
    "pokemon_id": "26361",
    "name": "pichy",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
}



respons = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_generate)
print(respons.text)

respons = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_id)
print(respons.text)

respons = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_shift)
print(respons.text)