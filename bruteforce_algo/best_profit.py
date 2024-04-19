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
