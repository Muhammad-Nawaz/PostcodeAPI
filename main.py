import json
import requests


class PostcodeApi:
    def __init__(self):
        pass

    def get_postcode_info(self, postcode):
        response = requests.get(f'https://api.postcodes.io/postcodes/{postcode}')
        if response.status_code == 200:
            return print(response.json())
        else:
            return None

    def get_postcode_info_random(self):
        response = requests.get('https://api.postcodes.io/random/postcodes')
        if response.status_code == 200:
            return print(response.json())
        else:
            return None


postcode = PostcodeApi()
postcode.get_postcode_info('UB24PG')
postcode.get_postcode_info_random()
