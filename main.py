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

    def create_postcode(self, postcode_data):
        response = requests.post('https://api.postcodes.io/postcodes/', json=postcode_data)
        if response.status_code == 201:
            return print(response.json())
        else:
            return None


postcode = PostcodeApi()postcode.get_postcode_info('UB24PG')
postcode.get_postcode_info_random()

postcode_data = {
    "postcode": "SW1A1AA",
    "quality": 1,
    "eastings": 530047,
    "northings": 179951,
    "country": "England",
    "nhs_ha": "London",
    "longitude": -0.127695,
    "latitude": 51.507322,
    "european_electoral_region": "London",
    "primary_care_trust": "Westminster",
    "region": "London",
    "lsoa": "Westminster 018A",
    "msoa": "Westminster 018",
    "incode": "1AA",
    "outcode": "SW1A",
    "parliamentary_constituency": "Cities of London and Westminster",
    "admin_district": "Westminster",
    "parish": "Westminster, unparished area",
    "admin_county": None,
    "admin_ward": "St James's",
    "ccg": "NHS Central London (Westminster)",
    "nuts": "Westminster",
    "codes": {
        "admin_district": "E09000033",
        "admin_county": "E99999999",
        "admin_ward": "E05000644",
        "parish": "E43000236",
        "parliamentary_constituency": "E14000639",
        "ccg": "E38000032",
        "ccg_id": "02D",
        "ced": "E99999999",
        "nuts": "UKI32"
    }
}
postcode.create_postcode(postcode_data)