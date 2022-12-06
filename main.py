import requests
import json

token = '62cb73aad28a535aee344fae47eb30d9'
response = requests.post('https://pokemonbattle.me:5000/pokemons', headers={'trainer_token': token}, json={
        "name": "Victini",
        "photo": "https://pokemonov.net/assets/images/pokemony/494-victini.png"
})
print(response.text)

response_rename = requests.put('https://pokemonbattle.me:5000/pokemons', headers={'trainer_token': token}, json={    "pokemon_id": 1403,
    "name": "Виктини",
    "photo": "https://pokemonov.net/assets/images/pokemony/494-victini.png"  
})
print(response_rename.text)

response_catch = requests.post('https://pokemonbattle.me:5000/trainers/addPokebol', headers={'trainer_token': token}, json={
    "pokemon_id": "1403"
})
print(response_catch.text)