from __future__ import annotations

from time import sleep

from strategy.order import Order
from strategy.product import Product
from strategy.customer import Customer
from strategy.promotion import best_promo


class BuyStock:

    def __init__(self, stock):
        self.stock = stock

    def execute(self):
        self.stock.buy()


class SellStock:

    def __init__(self, stock):
        self.stock = stock

    def execute(self):
        self.stock.sell()


class Stock:

    def __init__(self, product):
        self.product = product

    def buy(self):
        print(f'Stock [Name: {self.product.name} '
              f'Qtd: {self.product.quantity}] bought.')

    def sell(self):
        print(f'Stock [Name: {self.product.name} '
              f'Qtd: {self.product.quantity}] sold.')


class Invoker:
    _actions = []

    def take_order(self, product):
        self._actions.append(product)

    def place_orders(self):
        for product in self._actions:
            product.execute()

        self._actions.clear()


if __name__ == '__main__':
    cliente = Customer('Mateus', 1001)

    camisa = Product('Camisa', 2, 60.50)
    jaqueta = Product('Jaqueta', 1, 120.50)
    tenis = Product('Tênis', 1, 420.50)
    bone = Product('Boné', 1, 20.50)
    oculos_de_sol = Product('Óculos de Sol', 1, 100.50)

    carrinho = [camisa, jaqueta, tenis, bone, oculos_de_sol]

    order = Order(cliente, carrinho, best_promo)

    invoker = Invoker()

    for item in order.products:
        stock_product = Stock(item)

        buy_stock = BuyStock(stock_product)
        sell_stock = SellStock(stock_product)

        invoker.take_order(buy_stock)
        invoker.take_order(sell_stock)

    for i in range(10):
        sleep(1)
        print("I wait a moment to process")

    invoker.place_orders()
