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
    host = os.environ.get('IP', '0.0.0.0')
    port = int(os.environ.get('PORT', 8080))
    app.run(host=host, port=port)
