from flask import Flask, jsonify
import csv
import json

app = Flask(__name__)

@app.route("/")
def show_json_data():
    data = []

    # CSVファイルを読み込んでJSON形式に変換
    with open('flight_data.csv', 'r') as csvfile:
        csvreader = csv.DictReader(csvfile)
        for row in csvreader:
            data.append(row)

    # JSON形式に変換して返す
    return jsonify(data)

if __name__ == '__main__':
    app.run()

