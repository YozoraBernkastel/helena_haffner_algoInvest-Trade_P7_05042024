import csv
import logging
from os import path
from itertools import combinations


class BestProfit:
    def __init__(self):
        self.value = 0.0


def convert_percent_in_euro(price: float, profit: float) -> float:
    return profit / 100 * price


def read_csv():
    file_path = "./input/bruteforce_data.csv"
    if not path.exists(file_path):
        logging.info("Le fichier bruteforce_data.csv n'existe pas")
        return

    with open(file_path, 'r') as f:
        data = [d for d in csv.reader(f)]

    return data[1:]


def format_data():
    data = read_csv()
    new_data = {d[0]: [d[1], convert_percent_in_euro(float(d[1]), float(d[2]))] for d in data}

    return new_data


def compute_all_combinations(data: dict, r: int, best_profit: BestProfit):
    all_comb = list(combinations(data, r))

    for comb in all_comb:
        in_list = list(comb)
        total_price = sum([float(data[k][0]) for k in in_list])
        profit_list = [data[k][1] for k in in_list]
        total_profit = sum(profit_list)

        if total_price <= 500 and total_profit > best_profit.value:
            print(r)
            print(f"{best_profit.value = }")
            best_profit.value = total_profit

            print(in_list)
            print(f"{total_price = }")
            print(f"{profit_list = }")
            print(f"{total_profit = }")
            print()


def entry_point():
    data = format_data()
    best_profit = BestProfit()

    for r in range(1, len(data) + 1):
        compute_all_combinations(data, r, best_profit)


