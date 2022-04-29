from abc import ABC, abstractmethod


class ActionStock:

    @staticmethod
    @abstractmethod
    def execute():
        pass


class ReceiverStock:

    @staticmethod
    def buy(stock):
        stock.buy()

    @staticmethod
    def sell(stock):
        stock.sell()


class BuyStock(ActionStock):

    def __init__(self, receiver, stock):
        self._receiver = receiver
        self.stock = stock

    def execute(self):
        self._receiver.buy(self.stock)


class SellStock(ActionStock):

    def __init__(self, receiver, stock):
        self._receiver = receiver
        self.stock = stock

    def execute(self):
        self._receiver.sell(self.stock)


class Stock:

    def __init__(self, product):
        self.product = product

    def buy(self):
        print(f'\t - Stock [Name: {self.product.name} '
              f'Qtd: {self.product.quantity}] bought.')

    def sell(self):
        print(f'\t - Stock [Name: {self.product.name} '
              f'Qtd: {self.product.quantity}] sold.')
