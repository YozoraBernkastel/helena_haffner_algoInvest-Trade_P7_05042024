import time
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


def compare_sequences(ratio_sequence: list, profit_sequence: list) -> None:
    ratio_actions, ratio_total = compute_sequence(ratio_sequence)
    # todo Un excès de prudence ? Ou peut-être tester plus d'angles ?
    profit_actions, profit_total = compute_sequence(profit_sequence)

    best_total = ratio_total if ratio_total[2] > profit_total[2] else profit_total
    best_sequence = ratio_actions if ratio_total[2] > profit_total[2] else profit_actions

    print(f"Achetez les {best_total[0]} actions suivantes pour gagner {best_total[2]}€ en dépensant {best_total[1]}€ :")
    table = Table()
    table.add_column("Action", style="green", no_wrap=True)
    table.add_column("Prix", style="blue")
    table.add_column("Profit", style="magenta")

    for action in best_sequence:
        table.add_row(action[0], f"{action[1][0]}", f"{action[1][1]}")

    table.add_row("Total", f"{best_total[1]}", f"{best_total[2]}")

    console = Console()
    console.print(table)


def optimized_entry_point(file_path: str, name: str) -> None:
    print(f"############### Optimized {name} ################\n")
    start = time.time()
    ratio_data, profit_data = opti_format_data(file_path)
    compare_sequences(ratio_data, profit_data)

    end = time.time()

    print(f"\nOptimized Algo execution time -> {end - start}\n")
