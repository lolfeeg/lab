import json
from pathlib import Path
tests, values, report = Path(input()), Path(input()), Path(input())
with open(values, 'r', encoding='utf-8') as file:
    data = json.load(file)
    dry={}
    for _, values in data.items():
        for value in values:
            dry[value['id']] = value['value']
def func(it):
    for value in it:
        if 'value' in value:
            value['value'] = dry[value['id']]
        if 'values' in value:
            func(value['values'])
with open(tests, 'r', encoding='utf-8') as file:
    data = json.load(file)
for _, values in data.items():
    func(values)
with open(report, 'w', encoding='utf-8') as file:
    json.dump(data, file, indent=2)
