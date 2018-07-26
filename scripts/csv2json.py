import csv
import json


def read_csv():
    markers = []
    with open('../data/coords.csv') as infile:
        reader = csv.reader(infile)
        for row in reader:
            markers.append(
                {'lat': float(row[1]), 'lng': float(row[2])}
            )

    return markers

def write_json(markers):
    with open('../data/markers.json', 'w') as outfile:
        json.dump(markers, outfile, indent=2)

if __name__ == '__main__':
    markers = read_csv()
    write_json(markers)
