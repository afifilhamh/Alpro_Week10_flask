from flask import Flask
from flask import render_template, request, jsonify
import pandas as pd
import csv
import json
import os

app = Flask(__name__)

@app.route('/')
def profile():
    return render_template('profile.html')

@app.route('/linktree/')
def linktree():
    return render_template('linktree.html')

@app.route('/biodatadiri/')
def biodatadiri():
    return render_template('biodatadiri.html')

@app.route('/fibbonaci/')
def fibbonaci():
    return render_template('fibbonaci.html')

@app.route('/education/')
def education():
    return render_template('education.html')

@app.route('/organization/')
def organization():
    return render_template('organization.html')

@app.route('/skill/')
def skill():
    return render_template('skill.html')

@app.route('/kotaksaran/', methods=['GET', 'POST'])
def kotaksaran():
    if request.method == 'POST':
        feedback_data = request.form.get('feedback')
        return render_template('feedback_result.html', feedback_data=feedback_data)
    
    return render_template('kotaksaran.html')


base_dir = os.path.dirname(os.path.abspath(__file__))
csv_file_path = os.path.join(base_dir, 'static', 'csv', 'datapribadi.csv')


def csv_to_json(file_path):
    with open(file_path, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        data = [row for row in csv_reader]

    json_data = json.dumps(data)
    return json_data


def showdata():
    if os.path.exists(csv_file_path):
        json_data = csv_to_json(csv_file_path)
        return json_data
    else:
        return 'CSV file not found.'


@app.route('/showdata')
def get_data():
    return jsonify(showdata())


@app.route('/getdata')
def retrieve_data():
    return render_template('JSON.html')


if __name__ == '__main__':
    app.run(debug=True)