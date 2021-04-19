#! /usr/local/bin/python
# -*- coding: utf-8 -*-
from calendar import timegm
from datetime import datetime
from flask import Flask, request, jsonify
app = Flask(__name__)

app.debug = True
# 

def convert_to_time_ms(timestamp):
    return 1000 * timegm(datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%S.%fZ').timetuple())


@app.route('/')
def health_check():
    return 'This datasource is healthy.'


@app.route('/search', methods=['POST'])
def search():
    return jsonify(['my_series', 'another_series'])


@app.route('/query', methods=['POST'])
def query():
    req = request.get_json()
    data = [
        {
            "target": req['targets'][0]['target'],
            "datapoints": [
                [861, convert_to_time_ms(req['range']['from'])],
                [767, convert_to_time_ms(req['range']['to'])]
            ]
            # "datapoints": [
            #     [767, convert_to_time_ms(req['range']['from'])],
            #     [861, convert_to_time_ms(req['range']['to'])]
            # ]
        }
    ]
    return jsonify(data)


@app.route('/annotations', methods=['POST'])
def annotations():
    req = request.get_json()
    data = [
        {
            "annotation": 'This is the annotation',
            "time": (convert_to_time_ms(req['range']['from']) +
                     convert_to_time_ms(req['range']['to'])) / 2,
            "title": 'Deployment notes',
            "tags": ['tag1', 'tag2'],
            "text": 'Hm, something went wrong...'
        }
    ]
    return jsonify(data)


if __name__ == '__main__':
    app.run()
