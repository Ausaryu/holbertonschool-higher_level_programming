import csv
import json


def convert_csv_to_json(filename):
    try:
        with open(filename, "r") as f:
            reader = csv.DictReader(f)
            with open("data.json", "w") as j:
                j.write(json.dumps(list(reader), indent=4))
        return True
    except Exception:
        return False
