# Coffee Shop Modelling

## Overview

This project is a domain model of a Coffee Shop built using Python and object-oriented programming (OOP) principles. It simulates customers placing orders for various types of coffee, and tracks customer behaviors and coffee statistics.

The model consists of three main entities:

- `Customer`
- `Coffee`
- `Order`

## Objective

The goal is to demonstrate OOP concepts including:

- Class design
- Relationships (one-to-many, many-to-many)
- Data validation and exception handling

---

## Project Structure

```
└── 📁coffee_shop
    └── coffee.py
    └── customer.py
    └── debug.py
    └── order.py
    └── Pipfile
    └── Pipfile.lock
    └── README.md
```

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/phil-ogutu/coffee_shop.git
cd coffee_shop
```

### 2. Set Up a Virtual Environment
```bash
pipenv install
pipenv shell
```

## Class Responsibilities
### Customer  
-Stores customer information.  

-Validates name (1–15 characters).  

-Can place multiple orders.  

Methods:

 - orders()

 - coffees()

 - create_order(coffee, price)

 - coffees_ordered()


### Coffee  
-Stores coffee information.

-Validates name (min 3 characters).

-Tracks all orders for that coffee.

Methods:

 - orders()

 - customers()

 - num_of_orders()

 - average_price()

### Order
Represents a single transaction between a customer and a coffee.

Validates:

-Customer and coffee instances

-Price

## License
This project is for educational purposes only.

---