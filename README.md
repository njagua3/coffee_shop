# Coffee Shop Domain Model

This project implements a simple domain model for a coffee shop, focusing on three main entities:
- `Customer`
- `Coffee`
- `Order`

The project demonstrates relationships between these entities, with customers placing orders for different types of coffee, and coffees having many associated orders.

## Features

- A `Customer` can place many `Orders`.
- A `Coffee` can have many `Orders`.
- An `Order` belongs to one `Customer` and one `Coffee`.
- Methods for creating orders, calculating the number of orders for a coffee, and finding the customer who spent the most on a specific coffee.
- Full unit test coverage using `pytest`.

## Project Structure


## Getting Started

### Prerequisites

Ensure you have the following installed on your system:
- Python 3.8 or later
- Pipenv (Python dependency management)

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/njagua3/coffee_shop.git
   cd coffee_shop

Classes and Relationships
Customer
Initializes with a name (1-15 characters).
Methods:
orders(): Returns all orders placed by the customer.
coffees(): Returns all unique coffees ordered by the customer.
create_order(coffee, price): Creates a new order for a given coffee and price.
most_aficionado(coffee): Returns the customer who has spent the most on a given coffee.
Coffee
Initializes with a name (minimum 3 characters).
Methods:
orders(): Returns all orders for this coffee.
customers(): Returns all unique customers who ordered this coffee.
num_orders(): Returns the total number of orders for this coffee.
average_price(): Returns the average price of this coffee based on its orders.
Order
Initializes with a customer, coffee, and price (1.0 to 10.0).
Properties:
customer: Returns the customer who placed the order.
coffee: Returns the coffee ordered.
price: Returns the price of the order.
Testing
All methods and properties are tested using pytest. The test cases are located in the tests/ directory.

To run the tests: pytest