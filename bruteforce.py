import csv
import time
from os import path
from itertools import combinations


class BestProfit:
    def __init__(self):
        self.total_price: float = 0.0
        self.value: float = 0.0
        self.combination: list = []

    def is_better(self, new_profit: float) -> bool:
        return new_profit < self.value

    def is_cheaper(self, new_profit: int, total_price: float) -> bool:
        return new_profit == self.value and total_price < self.total_price


def convert_percent_in_euro(price: float, profit: float) -> float:
    return profit / 100 * price


def read_csv():
    file_path = "./input/bruteforce_data.csv"
    if not path.exists(file_path):
        print("Le fichier bruteforce_data.csv n'existe pas")
        return

    with open(file_path, 'r') as f:
        data = [d for d in csv.reader(f)]

    return data[1:]


def format_data():
    data = read_csv()
    new_data = {d[0]: [d[1], convert_percent_in_euro(float(d[1]), float(d[2]))] for d in data}

    return new_data


def info_best_combination(best_profit):
    print(f"Meilleure combinaison -> {best_profit.combination}")
    print(f"Prix total de la combinaison -> {best_profit.total_price}")
    print(f"Profits sur deux ans -> {best_profit.value}")


def compute_all_combinations(data: dict, r: int, best_profit: BestProfit):
    all_comb = list(combinations(data, r))

    for comb in all_comb:
        actions_combination = list(comb)
        total_price = sum([float(data[k][0]) for k in actions_combination])
        profit_list = [data[k][1] for k in actions_combination]
        total_profit = sum(profit_list)

        if total_price > 500 or best_profit.is_better(total_profit):
            continue

        if best_profit.is_cheaper(total_profit, total_price) or not best_profit.is_better(total_profit):
            best_profit.total_price = total_price

        best_profit.value = total_profit
        best_profit.combination = actions_combination


def entry_point():
    start = time.time()
    data = format_data()
    best_profit = BestProfit()

    for r in range(1, len(data) + 1):
        compute_all_combinations(data, r, best_profit)

    info_best_combination(best_profit)
    end = time.time()

    print(f"\nExecution time -> {end - start}")



