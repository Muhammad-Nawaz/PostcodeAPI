from main import *


class RandomAddress():
    def __init__(self, random_postcode):
        self.postcode = random_postcode.get('postcode')
        self.quality = random_postcode.get('quality')
        self.eastings = random_postcode.get('eastings')
        self.northings = random_postcode.get('northings')


random_address = RandomAddress(random_postcode)
