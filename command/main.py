from time import sleep

from strategy.order import Order
from strategy.product import Product
from strategy.customer import Customer
from strategy.promotion import best_promo

from stock import Stock, BuyStock, SellStock, ReceiverStock
from invoker import Invoker


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
    for index, item in enumerate(order.products):
        receiver = ReceiverStock()
        stock = Stock(item)

        buy_stock = BuyStock(receiver, stock)
        sell_stock = SellStock(receiver, stock)

        invoker.take_order(f'buy_order_{order.id}_{index}', buy_stock)
        invoker.take_order(f'sell_order_{order.id}_{index}', sell_stock)

    invoker.place_orders()
