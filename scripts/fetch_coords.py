import csv
import os
import requests


def read_cities(cities_file):
    """ Read CSV file and return set of cities """
    with open('../data/cities.csv') as lines:
        cities = {line.rstrip('\n') for line in lines}

    return cities


def get_coords(cities):
    """ Fetch coordinates from Google Maps Geocode API and return dict """
    coords = {}
    for city in cities:
        url = 'https://maps.googleapis.com/maps/api/geocode/json?region=us&key={0}&address={1}'.format(API_KEY, city)
        req = requests.get(url)
        if req.status_code == 200:
            resp = req.json()
            lat_long = resp['results'][0]['geometry']['location']
            if city not in coords:
                coords[city] = lat_long
        else:
            if city not in coords:
                coords[city] = {'lat': 'unknown', 'lng': 'unknown'}

    return coords


def write_coords(coords):
    """ Write to CSV file """
    with open('../data/markers.csv', 'w') as outfile:
        writer = csv.writer(outfile)
        for city, coord in coords.items():
            writer.writerow((city, coord['lat'], coord['lng']))




if __name__ == '__main__':
    API_KEY = os.environ['GOOGLE_MAPS_KEY']
    cities_file = '../data/cities.csv'
    cities = read_cities(cities_file)
    coords = get_coords(cities)
    write_coords(coords)
