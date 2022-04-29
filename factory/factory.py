from abc import ABC, abstractmethod
from strategy.order import Order
from strategy.product import Product
from strategy.customer import Customer
from strategy.promotion import bulk_item_promo, fidelity_promo, large_order_promo, best_promo


class IOrder(ABC):

    @staticmethod
    @abstractmethod
    def create_object(order_type, order): ...


class NormalOrder(IOrder):

    def __init__(self, order):
        self.order = order

    def create_object(self, order):
        return order


class PreOrder(IOrder):

    def __init__(self, order):
        self.order = order

    def create_object(self, order):
        return order


class FactoryTypeOrder:

    def __init__(self, order):
        self.order = order

    def create_object(self, order_type):
        if order_type == 'order':
            return NormalOrder(self.order)
        elif order_type == 'pre_order':
            return PreOrder(self.order)
        return None


if __name__ == '__main__':
    cliente = Customer('Mateus', 1001)

    camisa = Product('Camisa', 2, 60.50)
    jaqueta = Product('Jaqueta', 1, 120.50)
    tenis = Product('Tênis', 1, 420.50)
    bone = Product('Boné', 1, 20.50)
    oculos_de_sol = Product('Óculos de Sol', 1, 100.50)

    carrinho = [camisa, jaqueta, tenis, bone, oculos_de_sol]

    ordem = Order(cliente, carrinho, best_promo)

    factory = FactoryTypeOrder(ordem)
    pre_order = factory.create_object('pre_order')
