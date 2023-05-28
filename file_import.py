import csv
# static

def import_csv(path):
    with open(path) as f:
        file = [{k: v for k, v in row.items()} for row in csv.DictReader(f, skipinitialspace=True)]
    return file