import time
from data_helper import read_csv, convert_percent_in_euro
from best_profit import BestProfit
from itertools import combinations


def opti_format_data(file_path):
    data = read_csv(file_path)
    new_data = {}
    for d in data:
        if float(d[1]) > 1.0 and float(d[2]) > 1.0:
            new_data[d[0]] = [d[1], convert_percent_in_euro(float(d[1]), float(d[2]))]

    return sorted(new_data.items(), key=lambda x: x[1][1], reverse=True)


def compute_all_combinations(data: dict, r: int):
    all_comb = list(combinations(data, r))
    print(all_comb)


def optimized_entry_point():
    start = time.time()
    print("opti")
    first_file_path = "./input/dataset1_Python+P7.csv"
    data = opti_format_data(first_file_path)
    print(data)

    # best_profit = BestProfit()

    # print(f"Meilleure combinaison -> {best_profit.combination}")
    # print(f"Prix total de la combinaison -> {best_profit.total_price}")
    # print(f"Profits sur deux ans -> {best_profit.value}")

    end = time.time()

    print(f"Optimized Algo execution time -> { end - start}")
