from order import Order

class Customer:
    all_customers = []

    def __init__(self, name):
        self.name = name
        Customer.all_customers.append(self)

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        if 1 <= len(value) <=15:
            self.__name = value
        else:
            raise ValueError ("Customer Name ust be between 1 and 15 characters")
        
    # All orders made by this customer
    def orders(self):
        orders = []
        for order in Order.all_orders:
            if order.customer == self:
                orders.append(order)
        return orders
    
    # Returns all coffee objects for this customer
    def coffees(self):
        coffees = set()
        for order in self.orders():
            coffees.add(order.coffee)
        return list(coffees)
    
    # Returns coffee names of coffee ordered by this customer
    def coffees_ordered(self):
        coffees = []
        for coffee in self.coffees():
            coffees.append(coffee.name)
        return coffees
    
    def create_order(self, coffee, price):
        return Order(self, coffee, price)