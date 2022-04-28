from time import sleep

from strategy.order import Order
from strategy.product import Product
from strategy.customer import Customer
from strategy.promotion import best_promo

from stock import Stock, BuyStock, SellStock
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

    for item in order.products:
        stock_product = Stock(item)

        buy_stock = BuyStock(stock_product)
        sell_stock = SellStock(stock_product)

        invoker.take_order(buy_stock)
        invoker.take_order(sell_stock)

    invoker.place_orders()
