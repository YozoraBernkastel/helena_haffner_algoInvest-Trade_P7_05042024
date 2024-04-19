import time
from itertools import combinations
from helper.data_helper import read_csv, convert_percent_in_euro, MAX_INVEST
from bruteforce_algo.best_profit import BestProfit
from rich import print
from rich.console import Console
from rich.table import Table


def display_best_combination(best_profit: BestProfit) -> None:
    print(f"Achetez les {len(best_profit.actions_sequence)} actions suivantes pour gagner "
          f"{best_profit.best_profit}€ en dépensant {best_profit.total_price}€ :")
    table = Table()
    table.add_column("Action", style="green", no_wrap=True)
    table.add_column("Prix", style="blue")
    table.add_column("Profit", style="magenta")
    for action in best_profit.actions_sequence_detail:
        table.add_row(f"{action[0]}", f"{action[1][0]}", f"{action[1][1]}")

    table.add_row("Total", f"{best_profit.total_price}", f"{best_profit.best_profit}")

    console = Console()
    console.print(table)


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
    print("############### Bruteforce ################\n")
    start = time.time()
    file_path = "./input/bruteforce_data.csv"
    data = format_data(file_path)
    best_profit = BestProfit()

    for r in range(1, len(data) + 1):
        compute_all_combinations(data, r, best_profit)

    best_profit.get_actions_info(data)
    display_best_combination(best_profit)
    end = time.time()

    print(f"\nExecution time  for Brute force alo-> {end - start}\n")
