import time
from itertools import combinations
from data_helper import read_csv, convert_percent_in_euro
from best_profit import BestProfit


def info_best_combination(best_profit):
    print(f"Meilleure combinaison -> {best_profit.combination}")
    print(f"Prix total de la combinaison -> {best_profit.total_price}")
    print(f"Profits sur deux ans -> {best_profit.value}")


def compute_all_combinations(data: dict, r: int, best_profit: BestProfit):
    all_comb = list(combinations(data, r))

    for comb in all_comb:
        actions_combination = list(comb)
        total_price = sum([float(data[k][0]) for k in actions_combination])
        total_profit = sum([data[k][1] for k in actions_combination])

        if total_price > 500 or best_profit.has_better_profit(total_profit):
            continue

        best_profit.keep_the_better(actions_combination, total_price, total_profit,)


def format_data(file_path):
    data = read_csv(file_path)
    new_data = {d[0]: [d[1], convert_percent_in_euro(float(d[1]), float(d[2]))] for d in data}

    return new_data


def bruteforce_entry_point():
    start = time.time()
    file_path = "./input/bruteforce_data.csv"
    data = format_data(file_path)
    best_profit = BestProfit()

    for r in range(1, len(data) + 1):
        compute_all_combinations(data, r, best_profit)

    info_best_combination(best_profit)
    end = time.time()

    print(f"\nExecution time  for Brute force alo-> {end - start}")
    print()



