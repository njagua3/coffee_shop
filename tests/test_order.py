import pytest

from coffee_shop.order import Order
from coffee_shop.customer import Customer
from coffee_shop.coffee import Coffee


def test_order_creation():
    customer = Customer("Kevin")
    coffee = Coffee("Latte")
    order = Order(customer, coffee, 3.5)
    assert order.price == 3.5
    assert order.customer == customer
    assert order.coffee == coffee

def test_invalid_price():
    customer = Customer("Kevin")
    coffee = Coffee("Latte")
    with pytest.raises(ValueError):
        Order(customer, coffee, 20.0)
