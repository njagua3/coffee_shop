class Order:
    def __init__(self, customer, coffee, price):
        """
        Initialize an Order instance with a customer, coffee, and price.
        
        This method also appends the order to the customer's and coffee's order lists.
        
        Args:
            customer (Customer): The customer placing the order.
            coffee (Coffee): The coffee being ordered.
            price (float): The price of the order.
        
        Raises:
            ValueError: If the price is not between 1.0 and 10.0.
        """
        self._customer = customer
        self._coffee = coffee
        self.price = price  # This will call the setter and perform validation.
        customer.orders().append(self)  # Add this order to the customer's list of orders.
        coffee.orders().append(self)     # Add this order to the coffee's list of orders.

    @property
    def customer(self):
        """
        Return the customer associated with this order.
        
        Returns:
            Customer: The customer who placed the order.
        """
        return self._customer

    @property
    def coffee(self):
        """
        Return the coffee associated with this order.
        
        Returns:
            Coffee: The coffee being ordered.
        """
        return self._coffee

    @property
    def price(self):
        """
        Return the price of the order.
        
        Returns:
            float: The price of the order.
        """
        return self._price

    @price.setter
    def price(self, value):
        """
        Set the price of the order.
        
        The price must be a float between 1.0 and 10.0.
        
        Args:
            value (float): The price to set for the order.
        
        Raises:
            ValueError: If the price is not a float or is outside the valid range.
        """
        if isinstance(value, float) and 1.0 <= value <= 10.0:
            self._price = value
        else:
            raise ValueError("Price must be a float between 1.0 and 10.0.")
