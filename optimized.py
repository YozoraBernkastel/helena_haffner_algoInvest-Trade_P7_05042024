import time
from data_helper import read_csv, convert_percent_in_euro


def opti_format_data(file_path):
    data = read_csv(file_path)
    new_data = {}
    for d in data:
        if float(d[1]) > 0.01 and float(d[2]) > 0.01:
            new_data[d[0]] = [float(d[1]), convert_percent_in_euro(float(d[1]), float(d[2])), float(d[2])]

    return (sorted(new_data.items(), key=lambda x: x[1][2], reverse=True),
            sorted(new_data.items(), key=lambda x: x[1][1], reverse=True))


def compute_sequence(data):
    actions = []
    total_profit = [0, 0.0, 0.0]

    for d in data:
        if total_profit[1] + d[1][0] > 500:
            continue
        actions.append(d[0])
        total_profit[0] += 1
        total_profit[1] += d[1][0]
        total_profit[2] += d[1][1]

    return actions, total_profit


def compare_sequences(ratio_sequence: list, profit_sequence: list) -> None:
    ratio_actions, ratio_total = compute_sequence(ratio_sequence)
    profit_actions, profit_total = compute_sequence(profit_sequence)

    best_total = ratio_total if ratio_total[2] > profit_total[2] else profit_total
    best_sequence = ratio_actions if ratio_total[2] > profit_total[2] else profit_actions
    
    print(f"Pour gagner {best_total[2]}€, dépensez {best_total[1]} Achetez les {best_total[0]} actions :")
    for action in best_sequence:
        print(f"   - {action}")


def optimized_entry_point(file_path: str) -> None:
    start = time.time()
    print("############### opti ################\n")
    ratio_data, profit_data = opti_format_data(file_path)
    compare_sequences(ratio_data, profit_data)

    end = time.time()

    print(f"\nOptimized Algo execution time -> {end - start}")
