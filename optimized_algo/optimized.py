import time
import tracemalloc
from helper.data_helper import read_csv, convert_percent_in_euro, MAX_INVEST
from rich import print
from rich.console import Console
from rich.table import Table


def opti_format_data(file_path: str) -> tuple[list, list]:
    data = read_csv(file_path)
    new_data = {}
    for d in data:
        if float(d[1]) > 0.01 and float(d[2]) > 0.01:
            new_data[d[0]] = [float(d[1]), convert_percent_in_euro(float(d[1]), float(d[2])), float(d[2])]

    return (sorted(new_data.items(), key=lambda x: x[1][2], reverse=True),
            sorted(new_data.items(), key=lambda x: x[1][1], reverse=True))


def compute_sequence(data: list) -> tuple[list, list]:
    actions = []
    total_profit = [0, 0.0, 0.0]

    for d in data:
        if total_profit[1] + d[1][0] > MAX_INVEST:
            continue
        actions.append(d)
        total_profit[0] += 1
        total_profit[1] += d[1][0]
        total_profit[2] += d[1][1]

    return actions, total_profit


def display_results(best_sequence : list, best_total: list):
    print(f"Achetez les {best_total[0]} actions suivantes pour gagner {round(best_total[2], 2)}€ "
          f"en dépensant {round(best_total[1], 2)}€ :")
    table = Table()
    table.add_column("Action", style="green", no_wrap=True)
    table.add_column("Prix", style="blue")
    table.add_column("Profit", style="magenta")

    for action in best_sequence:
        table.add_row(action[0], f"{round(action[1][0], 2)}", f"{round(action[1][1], 2)}")

    table.add_row("Total", f"{round(best_total[1], 2)}", f"{round(best_total[2], 2)}")

    console = Console()
    console.print(table)


def compare_sequences(ratio_sequence: list, profit_sequence: list) -> tuple[list, list]:
    """
    Ratio total should be better most of the time but, in some case, the better ratio can eliminate the second one when
    first + second > max_value and second is almost equal to max_value. So, we need to compare the two possibility to
    fill that hole (as second will be in first position when we sort by raw profit).
    """
    ratio_actions, ratio_total = compute_sequence(ratio_sequence)
    profit_actions, profit_total = compute_sequence(profit_sequence)

    print("À titre informatif :")
    print(f"   - Tri par ratio -> Nombre d'actions à acheter {ratio_total[0]}; Prix des actions {round(ratio_total[1], 2)}€."
          f"; Gain au bout de deux ans {round(ratio_total[2], 2)}€.")
    print(f"   - Tri par profit brut -> Nombre d'actions à acheter {profit_total[0]}; Prix des actions {round(profit_total[1], 2)}€."
          f"; Gain au bout de deux ans {round(profit_total[2], 2)}€.\n")

    best_total = ratio_total if ratio_total[2] > profit_total[2] else profit_total
    best_sequence = ratio_actions if ratio_total[2] > profit_total[2] else profit_actions

    return best_sequence, best_total


def optimized_entry_point(file_path: str, name: str) -> None:
    print(f"############### Optimized {name} ################\n")
    start = time.time()
    # tracemalloc.start()
    ratio_data, profit_data = opti_format_data(file_path)
    best_sequence, best_total = compare_sequences(ratio_data, profit_data)
    # current, peak = tracemalloc.get_traced_memory()
    # print(
    #     f"Current memory usage is {current / 10 ** 3}KB; Peak was {peak / 10 ** 3}KB; Diff = {(peak - current) / 10 ** 3}KB")
    # tracemalloc.stop()
    end = time.time()

    display_results(best_sequence, best_total)

    print(f"\nTemps d'exécution de l'algo optimisé -> {end - start} secondes.\n")
