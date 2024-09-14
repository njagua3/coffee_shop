from coffee_shop.order import Order

class Customer:
    def __init__(self, name):
        """
        Initialize the Customer instance with a name and an empty list of orders.
        
        Args:
            name (str): The name of the customer.
        """
        self._name = None
        self.name = name
        self._orders = []

    @property
    def name(self):
        """
        Return the name of the customer.
        
        Returns:
            str: The customer's name.
        """
        return self._name

    @name.setter
    def name(self, value):
        """
        Set the name of the customer.
        
        The name must be a string with a length between 1 and 15 characters.
        
        Args:
            value (str): The name to set for the customer.
        
        Raises:
            ValueError: If the name is not a string or does not meet length requirements.
        """
        if isinstance(value, str) and 1 <= len(value) <= 15:
            self._name = value
        else:
            raise ValueError("Name must be a string between 1 and 15 characters.")

    def orders(self):
        """
        Return the list of orders placed by this customer.
        
        Returns:
            list: A list of Order instances associated with this customer.
        """
        return self._orders

    def coffees(self):
        """
        Return a list of unique coffees ordered by this customer.
        
        Returns:
            list: A list of unique Coffee instances that this customer has ordered.
        """
        return list(set([order.coffee for order in self._orders]))

    def create_order(self, coffee, price):
        """
        Create a new order for this customer.
        
        Args:
            coffee (Coffee): The coffee being ordered.
            price (float): The price of the order.
        
        Returns:
            Order: The newly created Order instance.
        """
        order = Order(self, coffee, price)
        self._orders.append(order)
        return order

    @classmethod
    def most_aficionado(cls, coffee):
        """
        Determine the customer who has spent the most on a given coffee.
        
        Args:
            coffee (Coffee): The coffee for which to find the top spender.
        
        Returns:
            Customer: The customer who has spent the most on the given coffee, or None if no orders exist.
        """
        customers_spending = {}
        for order in coffee.orders():
            if order.customer in customers_spending:
                customers_spending[order.customer] += order.price
            else:
                customers_spending[order.customer] = order.price
        if customers_spending:
            return max(customers_spending, key=customers_spending.get)
        return None
