#!/usr/bin/env python3
# coding: utf-8
import socket
import csv
import json

# settings
host = "192.168.0.13" #192.168.0.199
port = 30003

# open socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

l = []

while True:
    response = client.recv(4096)
    
    if str(response.decode("utf-8"))[:5] == "MSG,3":
        data_list = str(response).split(',')
        d = {}
        d['date'] = data_list[6]
        d['time'] = data_list[7]
        d['longitude'] = data_list[15]
        d['latitude'] = data_list[14]
        d['altitude'] = data_list[11]
        #l.append(d)
        # リストの先頭に新しいデータを追加し、古いデータを削除
        l.insert(0, d)
        if len(l) > 10:
            l = l[:10]  # リストの最初の10個のデータを保持
        
        # CSVファイルへの書き込み
        outfilename = "flight_data.csv"
        with open(outfilename, "w", newline="") as csvfile:
            fieldnames = ['date', 'time', 'longitude', 'latitude', 'altitude']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(l)

