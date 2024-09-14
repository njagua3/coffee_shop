import pytest
from coffee_shop.customer import Customer
from coffee_shop.coffee import Coffee

def test_customer_name():
    customer = Customer("Kevin")
    assert customer.name == "Kevin"

    with pytest.raises(ValueError):
        Customer("A very long name")

def test_customer_order():
    customer = Customer("Kevin")
    coffee = Coffee("Latte")
    order = customer.create_order(coffee, 5.0)
    assert order.price == 5.0
    assert order.coffee == coffee
    assert order.customer == customer
