class Order:
    all_orders = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order.all_orders.append(self)

    @property
    def customer(self):
        return self.__customer
    
    @customer.setter
    def customer(self, value):
        from customer import Customer
        if isinstance(value, Customer):
            self.__customer = value
        else:
            raise ValueError("customer must be an instance of Customer")
        
    @property
    def coffee(self):
        return self.__coffee
    
    @coffee.setter
    def coffee(self, value):
        from coffee import Coffee
        if isinstance(value, Coffee):
            self.__coffee = value
        else:
            raise ValueError("coffee must be an instance of Coffee")
        
    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, value):
        if 1 <= value <=10:
            self.__price = value
        else:
            raise ValueError("Price must be between 1 ad 10")
    
