import csv
from os import path


MAX_INVEST = 500


def read_csv(file_path: str):
    if not path.exists(file_path):
        print("Le fichier n'existe pas")
        return

    with open(file_path, 'r') as f:
        data = [d for d in csv.reader(f)]

    return data[1:]


def convert_percent_in_euro(price: float, profit: float) -> float:
    return profit / 100 * price


