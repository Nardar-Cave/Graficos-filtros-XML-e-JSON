from flask import Flask, render_template, request, jsonify
import json
import xml.etree.ElementTree as ET
from datetime import datetime
import os

app = Flask(__name__)

def parse_json_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
        return [{
            'date': datetime.strptime(item['date'], '%Y-%m-%d').strftime('%Y-%m-%d'),
            'value': float(item['value']),
            'source': 'json'
        } for item in data]

def parse_xml_file(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    data = []
    for item in root.findall('.//item'):
        data.append({
            'date': datetime.strptime(item.find('date').text, '%Y-%m-%d').strftime('%Y-%m-%d'),
            'value': float(item.find('value').text),
            'source': 'xml'
        })
    return data

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data')
def get_data():
    min_value = float(request.args.get('min_value', 0))
    max_value = float(request.args.get('max_value', float('inf')))
    start_date = request.args.get('start_date', '1900-01-01')
    end_date = request.args.get('end_date', '2100-12-31')

    json_data = parse_json_file('data/dados.json')
    xml_data = parse_xml_file('data/dados.xml')
    all_data = json_data + xml_data

    filtered_data = [
        item for item in all_data
        if min_value <= item['value'] <= max_value
        and start_date <= item['date'] <= end_date
    ]

    return jsonify(filtered_data)

if __name__ == '__main__':
    app.run(debug=True)
