class Product:

    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

    def total(self):
        return self.price * self.quantity


class Order:

    def __init__(self, customer, cart, promotion=None):
        self.customer = customer
        self.cart = list(cart)
        self.promotion = promotion

    @property
    def total(self):
        return sum(item.total() for item in self.cart)

    def due(self):
        discount = 0
        if self.promotion is not None:
            discount = self.promotion.discount(self)
        return self.total() - discount


if __name__ == '__main__':
    camisa = Product('Camisa', 1, 10.50)
    jaqueta = Product('Blusa', 1, 120.50)

    order = Order('Mateus', [camisa, jaqueta])
    print(order.total)