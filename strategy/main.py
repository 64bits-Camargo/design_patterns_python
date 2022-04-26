from customer import Customer
from order import Order
from product import Product
from promotion import BulkItemPromo, FidelityPromo, LargeOrderPromo

if __name__ == '__main__':
    cliente = Customer('Mateus', 1001)

    camisa = Product('Camisa', 1, 60.50)
    jaqueta = Product('Jaqueta', 1, 120.50)
    tenis = Product('Tênis', 1, 420.50)
    bone = Product('Boné', 1, 20.50)
    oculos_de_sol = Product('Óculos de Sol', 1, 100.50)

    carrinho = [camisa, jaqueta, tenis, bone, oculos_de_sol]

    order = Order(cliente, carrinho, FidelityPromo())

    print('Subtotal:', order.subtotal)
    print('Total:', order.total)
