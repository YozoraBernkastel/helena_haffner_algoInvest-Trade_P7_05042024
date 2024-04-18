class BestProfit:
    def __init__(self):
        self.total_price: float = 0.0
        self.value: float = 0.0
        self.combination: list = []

    def has_better_profit(self, new_profit: float) -> bool:
        return new_profit < self.value

    def new_is_cheaper(self, new_profit: float, total_price: float) -> bool:
        return new_profit == self.value and total_price < self.total_price

    def keep_the_better(self, actions_combination: list, new_price: float, new_profit: float) -> None:
        if self.new_is_cheaper(new_profit, new_price) or not self.has_better_profit(new_profit):
            self.total_price = new_price
            self.value = new_profit
            self.combination = actions_combination

