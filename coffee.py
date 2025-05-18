from order import Order

class Coffee:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        if len(value) > 3:
            self.__name = value
        else:
            raise ValueError ("Coffee Name should be at least 3 characters long")
        
    # All orders made for specific coffee
    def orders(self):
        orders = []
        for order in Order.all_orders:
            if order.coffee == self:
                orders.append(order)
        return orders
    
    # Customers who ordered specific coffee as objects
    def customers(self):
        customers = set()
        for order in self.orders():
            customers.add(order.customer)
        return list(customers)
    
    # Customer names who ordered specific coffee
    def customer_names(self):
        customers = []
        for customer in self.customers():
            customers.append(customer.name)
        return customers  
        
    def num_of_orders(self):
        return len(self.orders())
    
    def average_price(self):
        orders = self.orders()
        if not orders:
            return 0
        return sum(order.price for order in orders) / len(orders)