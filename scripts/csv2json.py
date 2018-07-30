import csv
import json


def read_csv():
    """ Read markers and return list of dicts with coords and content """
    markers = []
    with open('../data/markers.csv') as infile:
        reader = csv.reader(infile)
        for row in reader:
            markers.append({
                'coords': {
                     'lat': float(row[1]),
                     'lng': float(row[2])
                },
                'content': '<h3>{city}</h3>'.format(city=row[0]).replace(',', ', ')
            })

    return markers


def write_json(markers):
    """ Write list of dicts to json file """
    with open('../data/markers.json', 'w') as outfile:
        json.dump(markers, outfile, indent=2)




if __name__ == '__main__':
    markers = read_csv()
    write_json(markers)
