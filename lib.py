import csv
import json
import os
from typing import Any

def flatten_json(json: Any):
    """Зведення структури JSON"""
    def flatten(obj, name=''):
        flattened = {}
        if isinstance(obj, dict):
            for key, value in obj.items():
                flattened.update(flatten(value, f'{name}{key}_'))
        elif isinstance(obj, list):
            for i, item in enumerate(obj):
                flattened.update(flatten(item, f'{name}{i}_'))
        else:
            flattened[name[:-1]] = obj

        return flattened

    if isinstance(json, list):
        return [flatten(item) for item in json]
    else:
        return flatten(json)

def write_to_csv(data: any, filename: str):
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = data[0].keys()
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()
        for row in data:
            writer.writerow(row)

def convert_json_into_csv(json_file_dir: str):
    """Перетворює файл JSON у файл CSV"""

    # Читання JSON з файлу
    with open(json_file_dir, 'r') as f:
        data = json.load(f)

    # Зведення структури JSON
    data = flatten_json(data)
    print(data)

    # Отримати назву файлу призначення та зберегти в cvs файл
    csv_filename = os.path.splitext(os.path.basename(json_file_dir))
    csv_filename = f'{csv_filename[0]}.csv'
    csv_path = os.path.join(os.path.dirname(json_file_dir), csv_filename)

    if isinstance(data, list):
        write_to_csv(data, csv_path)
    else:
        write_to_csv([data], csv_path)


