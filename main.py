import json
import requests

response = requests.get('https://api.postcodes.io/postcodes/UB24PG')
print(response.json())
