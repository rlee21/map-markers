import json
import os
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    with open('data/markers.json') as json_file:
        markers = json.load(json_file)
        API_KEY = os.environ['GOOGLE_MAPS_KEY']
    return render_template('index.html', markers=markers, API_KEY=API_KEY)


if __name__ == '__main__':
    env = os.environ.get('PYTHON_ENV', 'local')
    HOST = '0.0.0.0'
    PORT = 5000
    debug = False if env == 'prod' else True
    app.run(host=HOST, port=PORT, debug=debug)

