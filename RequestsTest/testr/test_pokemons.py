import requests
import pytest

URL = 'https://api.pokemonbattle.me/v2'
token = '9b5b8bfb350c9a3558474358e3d10b24'
HEADER = {'Content-Type' : 'application/json', 'trainer_token': token}
TRAINER_ID= '3987'

def test_status_code():
    respons = requests.get(url=f'{URL}/trainers', params = {'traier_id': TRAINER_ID})
    assert respons.status_code == 200
    
def test_name_trainer():
    response_get = requests.get(url=f'{URL}/trainers', params = {'traier_id': TRAINER_ID})
    assert response_get.json()['data'][0]['trainer_name'] == 'фыфы'

