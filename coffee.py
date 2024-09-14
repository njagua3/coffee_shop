class Coffee:
    def __init__(self, name):
        # Initialize the Coffee instance with a name and an empty list of orders.
        self._name = None
        self.name = name
        self._orders = []

    @property
    def name(self):
        """Return the name of the coffee."""
        return self._name

    @name.setter
    def name(self, value):
        """
        Set the name of the coffee.
        
        The name must be a string with at least 3 characters.
        
        Args:
            value (str): The name to set for the coffee.
        
        Raises:
            ValueError: If the name is less than 3 characters long.
        """
        if isinstance(value, str) and len(value) >= 3:
            self._name = value
        else:
            raise ValueError("Name must be at least 3 characters.")

    def orders(self):
        """
        Return the list of orders associated with this coffee.
        
        Returns:
            list: A list of Order instances.
        """
        return self._orders

    def customers(self):
        """
        Return a list of unique customers who have ordered this coffee.
        
        Returns:
            list: A list of unique Customer instances.
        """
        return list(set([order.customer for order in self._orders]))

    def num_orders(self):
        """
        Return the total number of orders for this coffee.
        
        Returns:
            int: The number of orders.
        """
        return len(self._orders)

    def average_price(self):
        """
        Calculate the average price of this coffee based on its orders.
        
        Returns:
            float: The average price of the coffee. Returns 0 if there are no orders.
        """
        if self._orders:
            return sum([order.price for order in self._orders]) / len(self._orders)
        return 0
