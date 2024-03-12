
import requests


class PostcodeApi:
    def __init__(self):
        pass

    def get_postcode_info(self, postcode):
        try:
            response = requests.get(f'https://api.postcodes.io/postcodes/{postcode}')
            if response.status_code == 200:
                return response.json()
            else:
                return None
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")


    def get_postcode_info_random(self):
        try:
            response = requests.get('https://api.postcodes.io/random/postcodes')
            if response.status_code == 200:
                return response.json()
            else:
                return None
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")


    def get_bulk_lookup(self, postcode_data):
        try:
            response = requests.post('https://api.postcodes.io/postcodes/', json=postcode_data)
            if response.status_code == 200:
                return response.json()
            else:
                return None
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            return None


postcode = PostcodeApi()
postcode_info = postcode.get_postcode_info('UB24PG')
print(postcode_info)

random_postcode = postcode.get_postcode_info_random()
print(random_postcode)

postcode_data = {
  "postcodes" : ["PR3 0SG", "M45 6GN", "EX165BL"]
}

bulk_lookup = postcode.get_bulk_lookup(postcode_data)
print(bulk_lookup)
