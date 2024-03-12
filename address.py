from main import *


class Address():
    def __init__(self, postcode_info):
        self.postcode = postcode_info.get('postcode')
        self.quality = postcode_info.get('quality')
        self.eastings = postcode_info.get('eastings')
        self.northings = postcode_info.get('northings')


address = Address(postcode_info)
