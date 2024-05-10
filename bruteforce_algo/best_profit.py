from rich.console import Console
from rich.table import Table


class BestProfit:
    def __init__(self):
        self.total_price: float = 0.0
        self.best_profit: float = 0.0
        self.actions_sequence: list = []
        self.actions_sequence_detail: list = []

    def has_better_profit(self, new_profit: float) -> bool:
        return new_profit < self.best_profit

    def new_is_cheaper(self, new_profit: float, total_price: float) -> bool:
        return new_profit == self.best_profit and total_price < self.total_price

    def keep_the_better(self, actions_combination: list, new_price: float, new_profit: float) -> None:
        if self.new_is_cheaper(new_profit, new_price) or not self.has_better_profit(new_profit):
            self.total_price = new_price
            self.best_profit = new_profit
            self.actions_sequence = actions_combination

    def get_actions_info(self, data: dict) -> None:

        for action_name in self.actions_sequence:
            this_action_detail = [action_name, data[action_name]]
            self.actions_sequence_detail.append(this_action_detail)

    def display_best_combination(self) -> None:
        print(f"Achetez les {len(self.actions_sequence)} actions suivantes pour gagner "
              f"{round(self.best_profit, 2)}€ en dépensant {round(self.total_price, 2)}€ :")
        table = Table()
        table.add_column("Action", style="green", no_wrap=True)
        table.add_column("Prix", style="blue")
        table.add_column("Profit", style="magenta")
        for action in self.actions_sequence_detail:
            table.add_row(f"{action[0]}", f"{round(action[1][0], 2)}", f"{round(action[1][1], 2)}")

        table.add_row("Total", f"{round(self.total_price)}", f"{round(self.best_profit, 2)}")

        console = Console()
        console.print(table)
