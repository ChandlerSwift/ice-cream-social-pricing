#!/usr/bin/env nix-shell
#! nix-shell -i python3
#! nix-shell -p python3

import json
import os
overall = {}
ordercount = 0
directory = input("directory? e.g. 2024: ")

def analyze(name, data):
    totals = {}
    for order in data:
        for itemname, item in order['items'].items():
            if not itemname in totals:
                totals[itemname] = 0
            totals[itemname] += item['quantity']
    print(f"{name}: {len(data)} orders (${sum([data[0]['items'][name]['cost'] * qty for name, qty in totals.items()]):.2f}): {", ".join([f"{total} {item} (${total * data[0]['items'][item]['cost']:.2f})" for item, total in totals.items()])}")

alldata = []
for file in os.listdir(directory):
    if not file.endswith(".json"):
        continue
    with open(os.path.join(directory, file)) as f:
        data = json.load(f)
    alldata += data
    analyze(file.removesuffix(".json"), data)
analyze("total", alldata)
