import time
from itertools import combinations
from helper.data_helper import read_csv, convert_percent_in_euro, MAX_INVEST
from bruteforce_algo.best_profit import BestProfit
from rich import print


def compute_all_combinations(data: dict, r: int, best_profit: BestProfit) -> None:
    all_comb = list(combinations(data, r))

    for comb in all_comb:
        actions_combination = list(comb)
        total_price = sum([float(data[k][0]) for k in actions_combination])
        total_profit = sum([data[k][1] for k in actions_combination])

        if total_price > MAX_INVEST or best_profit.has_better_profit(total_profit):
            continue

        best_profit.keep_the_better(actions_combination, total_price, total_profit)


def format_data(file_path: str) -> dict[str: list]:
    data = read_csv(file_path)
    new_data = {d[0]: [d[1], convert_percent_in_euro(float(d[1]), float(d[2]))] for d in data}

    return new_data


def bruteforce_entry_point() -> None:
    print("\n############### Bruteforce ################\n")
    start = time.time()
    file_path = "./input/bruteforce_data.csv"
    data = format_data(file_path)
    best_profit = BestProfit()

    for r in range(1, len(data) + 1):
        compute_all_combinations(data, r, best_profit)
    best_profit.get_actions_info(data)
    end = time.time()
    best_profit.display_best_combination()

    print(f"\nTemps d'exécution de l'algo brute force -> {end - start}\n")
