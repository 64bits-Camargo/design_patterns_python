class Order:

    def __init__(self, customer, products, promotion=None):
        self.customer = customer
        self.products = list(products)
        self.promotion = promotion

    @property
    def subtotal(self):
        return round(sum(product.total for product in self.products), 2)

    @property
    def total(self):
        discount = 0
        if self.promotion is not None:
            discount = self.promotion.discount(self)
        return round(self.subtotal - discount, 2)

    def __repr__(self):
        return f"<class Order: total={self.total}, subtototal={self.subtotal}>"