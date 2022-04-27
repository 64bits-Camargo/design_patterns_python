import pytest

from customer import Customer
from order import Order
from product import Product
from promotion import bulk_item_promo, fidelity_promo, large_order_promo


@pytest.fixture()
def customer_800():
    return Customer(name="Teste 0", fidelity_points=800)


@pytest.fixture()
def customer_1000():
    return Customer(name="Teste 1", fidelity_points=1000)


@pytest.fixture()
def customer_1800():
    return Customer(name="Teste 2", fidelity_points=1800)


@pytest.fixture()
def cart():
    products = [
        {
            "name": "Blusa",
            "quantity": 2,
            "price": 45.4
        },
        {
            "name": "Blusa",
            "quantity": 2,
            "price": 45.4
        },
        {
            "name": "Blusa",
            "quantity": 2,
            "price": 45.4
        },
        {
            "name": "Blusa",
            "quantity": 2,
            "price": 45.4
        },
        {
            "name": "Blusa",
            "quantity": 2,
            "price": 45.4
        },
    ]

    return [Product(name=product['name'],
                    quantity=product['quantity'],
                    price=product['price']) for product in products]


def test_customer_attr(customer_800,
                       customer_1000,
                       customer_1800):
    assert customer_800.name == "Teste 0"
    assert customer_1000.name == "Teste 1"
    assert customer_1800.name == "Teste 2"

    assert customer_800.fidelity_points == 800
    assert customer_1000.fidelity_points == 1000
    assert customer_1800.fidelity_points == 1800


def test_cart_len(cart):
    assert len(cart) == 5
