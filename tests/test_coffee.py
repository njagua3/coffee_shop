import pytest
from coffee_shop.coffee import Coffee
from coffee_shop.customer import Customer


def test_coffee_name():
    coffee = Coffee("Espresso")
    assert coffee.name == "Espresso"

    # Test for name validation (string less than 3 characters)
    with pytest.raises(ValueError):
        Coffee("a")

def test_coffee_orders():
    coffee = Coffee("Latte")
    assert coffee.num_orders() == 0  # Assuming no orders initially
def test_coffee_orders_after_creation():
    coffee = Coffee("Latte")
    customer = Customer("Kevin")

    # Initially, no orders
    assert coffee.num_orders() == 0

    # Create an order and check if it's reflected in coffee orders
    customer.create_order(coffee, 5.0)
    assert coffee.num_orders() == 1
    assert len(coffee.orders()) == 1
    assert coffee.customers() == [customer]
