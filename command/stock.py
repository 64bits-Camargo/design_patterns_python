from abc import ABC, abstractmethod


class CommandStock(ABC):

    @abstractmethod
    def execute(self):
        pass


class BuyStock(CommandStock):

    def __init__(self, stock):
        self.stock = stock

    def execute(self):
        self.stock.buy()


class SellStock(CommandStock):

    def __init__(self, stock):
        self.stock = stock

    def execute(self):
        self.stock.sell()


class Stock:

    def __init__(self, product):
        self.product = product

    def buy(self):
        print(f'\t - Stock [Name: {self.product.name} '
              f'Qtd: {self.product.quantity}] bought.')

    def sell(self):
        print(f'\t - Stock [Name: {self.product.name} '
              f'Qtd: {self.product.quantity}] sold.')
