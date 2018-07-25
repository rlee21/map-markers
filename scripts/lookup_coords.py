import os
import requests


def get_addresses(address_file):
    """ Read csv file and return set of addresses """
    with open('../data/addresses.csv') as lines:
        addresses = {line.rstrip('\n') for line in lines}

    return addresses


def get_coords(addresses):
    """ Fetch coords from Google Maps Geocode API and return dict """
    coords = {}
    for address in addresses:
        url = 'https://maps.googleapis.com/maps/api/geocode/json?region=us&key={0}&address={1}'.format(API_KEY, 'Seattle,WA')
        # print(url)
        req = requests.get(url)
        resp = req.json()
        lat_long = resp['results'][0]['geometry']['location']
        if address not in coords:
            coords[address] = lat_long

    return coords


if __name__ == '__main__':
    API_KEY = os.environ['GOOGLE_MAPS_KEY']
    address_file = '../data/addresses.csv'
    addresses = get_addresses(address_file)
    coords = get_coords(addresses)
    print(coords)
