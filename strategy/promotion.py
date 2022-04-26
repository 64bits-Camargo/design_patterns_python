from abc import ABC, abstractmethod


class Promotion(ABC):

    @abstractmethod
    def discount(self, order):
        pass


class FidelityPromo(Promotion):

    def discount(self, order):
        discount = 0
        if order.customer.fidelity_points >= 1000:
            discount = order.subtotal * 0.05
        return discount


class BulkItemPromo(Promotion):

    def discount(self, order):
        discount = 0
        for product in order.products:
            if product.quantity >= 20:
                discount += product.total * 0.1
        return discount


class LargeOrderPromo(Promotion):

    def discount(self, order):
        discount = 0
        distinct_products = list(set(order.products))
        if len(distinct_products) >= 10:
            discount = order.subtotal * 0.07
        return discount
