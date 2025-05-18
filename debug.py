from customer import Customer
from coffee import Coffee
from order import Order

alice = Customer("Alice")
bob = Customer("Bob")

latte = Coffee("Latte")
espresso = Coffee("Espresso")

alice.create_order(latte, 3.5)
alice.create_order(espresso, 3.5)
bob.create_order(latte, 5.0)
bob.create_order(espresso, 4.5)

print(f"Alice coffees: {alice.coffees_ordered()}")
print(f"Latte orders: {latte.num_of_orders()}")
print(f"Average price of Latte: {latte.average_price()}")
print(f"Customers who ordered Latte: {latte.customer_names()}")
