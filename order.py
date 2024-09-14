class Order:
    def __init__(self, customer, coffee, price):
        self._customer = customer
        self._coffee = coffee
        self.price = price
        customer.orders().append(self)
        coffee.orders().append(self)

    @property
    def customer(self):
        return self._customer

    @property
    def coffee(self):
        return self._coffee

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if isinstance(value, float) and 1.0 <= value <= 10.0:
            self._price = value
        else:
            raise ValueError("Price must be a float between 1.0 and 10.0.")
