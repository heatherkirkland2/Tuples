'''
Objective: The goal of this assignment is to deepen your understanding of tuple packing and unpacking in Python.

Task 1: Customer Order Processing Refine your skills in tuple unpacking by managing customer orders.

Problem Statement: You are given a list of tuples, each representing a customer's order. Each tuple contains the customer's name, the product ordered, and the quantity. Your task is to unpack each tuple and print the order details in a user-friendly format.

Sample Order Data:

orders = [
    ("Alice", "Laptop", 1),
    ("Bob", "Camera", 2),
    # More orders...
]
- Write a function to iterate over the list of orders. - Unpack each tuple in the list and format the details for display.
'''
def process_orders(orders):
    for order_number, (customer_name, product, quantity) in enumerate(orders, start=1):
        print(f"Order {order_number}: {customer_name} ordered {quantity} unit(s) of {product}.")

# Sample Order Data
orders = [
    ("Alice", "Laptop", 1),
    ("Bob", "Camera", 2),
    # More orders...
]

# Call the function to process orders
process_orders(orders)

# Output: Order 1: Alice ordered 1 unit(s) of Laptop. Order 2: Bob ordered 2 unit(s) of Camera.
