from __future__ import annotations
from abc import ABC, abstractmethod


class Order:

    def execute(self):
        pass


class BuyStock(Order):

    def __init__(self, stock):
        self.stock = stock

    def execute(self):
        self.stock.buy()


class SellStock(Order):

    def __init__(self, stock):
        self.stock = stock

    def execute(self):
        self.stock.sell()


class Stock:

    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def buy(self):
        print(f'Stock [Name: {self.name} Qtd: {self.quantity}] bought.')

    def sell(self):
        print(f'Stock [Name: {self.name} Qtd: {self.quantity}] sold.')


class Invoker:

    _actions = []

    def take_order(self, order):
        self._actions.append(order)

    def place_orders(self):
        for order in self._actions:
            order.execute()

        self._actions.clear()


if __name__ == '__main__':
    stock_teste = Stock('Teste', 100)

    buy_stock = BuyStock(stock_teste)
    sell_stock = SellStock(stock_teste)

    invoker = Invoker()
    invoker.take_order(buy_stock)
    invoker.take_order(sell_stock)

    invoker.place_orders()
