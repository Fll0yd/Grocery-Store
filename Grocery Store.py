import tkinter as tk
from tkinter import simpledialog, messagebox
from collections import namedtuple

PriceData = namedtuple('PriceData', ['name', 'price'])
Discount = namedtuple('Discount', ['membership', 'rate'])

PRODUCT_PRICES = {
    'Biscuit': PriceData('Biscuit', 3),
    'Chicken': PriceData('Chicken', 5),
    'Egg': PriceData('Egg', 1),
    'Fish': PriceData('Fish', 3),
    'Coke': PriceData('Coke', 2),
    'Bread': PriceData('Bread', 2),
    'Apple': PriceData('Apple', 3),
    'Onion': PriceData('Onion', 3),
}

DISCOUNT_RATES = {
    'Gold': 0.1,
    'Silver': 0.05,
    'Bronze': 0,
}

# Function to prompt user for product details
def enter_products():
    buying_data = {}
    while True:
        details = simpledialog.askstring("Product Input", "Press A to add a product or Q to quit").strip().upper()
        if details == 'A':
            try:
                product = simpledialog.askstring("Product Input", "Enter Product: ").strip()
                price_data = PRODUCT_PRICES[product]
            except KeyError:
                messagebox.showerror("Error", "Invalid product. Please try again.")
                continue
            try:
                quantity = int(simpledialog.askstring("Product Input", "Enter Quantity: "))
                if quantity < 1:
                    raise ValueError('Quantity must be greater than 0.')
                if product in buying_data:
                    buying_data[product] += quantity
                else:
                    buying_data[product] = quantity
            except ValueError:
                messagebox.showerror("Error", "Invalid quantity. Please enter a positive integer.")
                continue
        elif details == 'Q':
            break
        else:
            messagebox.showerror("Error", "Please select either A to enter another product or Q to quit.")
    return buying_data

# Function to prompt user for product details
def enter_products():
    buying_data = {}
    while True:
        details = simpledialog.askstring("Product Input", "Press A to add a product or Q to quit").strip().upper()
        if details == 'A':
            try:
                product = simpledialog.askstring("Product Input", "Enter Product: ").strip()
                price_data = PRODUCT_PRICES[product]
            except KeyError:
                messagebox.showerror("Error", "Invalid product. Please try again.")
                continue
            try:
                quantity = int(simpledialog.askstring("Product Input", "Enter Quantity: "))
                if quantity < 1:
                    raise ValueError('Quantity must be greater than 0.')
                if product in buying_data:
                    buying_data[product] += quantity
                else:
                    buying_data[product] = quantity
            except ValueError:
                messagebox.showerror("Error", "Invalid quantity. Please enter a positive integer.")
                continue
        elif details == 'Q':
            break
        else:
            messagebox.showerror("Error", "Please select either A to enter another product or Q to quit.")
    return buying_data

def get_price(product, quantity):
    """Calculate the subtotal for a product based on its price and quantity."""
    price_data = PRODUCT_PRICES[product]
    subtotal = price_data.price * quantity
    print(f'{product}: ${price_data.price} x {quantity} = {subtotal}')
    return subtotal


def make_bill(buying_data, membership):
    """Calculate the total bill amount based on the product quantities and
    the customer's membership status, and print the discounted amount."""
    bill_amount = 0
    for product, quantity in buying_data.items():
        bill_amount += get_price(product, quantity)
    if bill_amount == 0:
        print("The bill amount is $0.00")
        return None
    try:
        discount_rate = DISCOUNT_RATES[membership]
    except KeyError:
        raise ValueError("Invalid membership type. Please enter Gold, Silver, or Bronze.")

    discount_amount = bill_amount * discount_rate
    discounted_bill_amount = bill_amount - discount_amount

    print(f'The bill amount is ${bill_amount:.2f}')
    print(f'The discount rate for {membership} is {discount_rate:.0%}')
    print(f'The discount amount is ${discount_amount:.2f}')
    return discounted_bill_amount

buying_data = enter_products()
while not buying_data:
    print("No items entered. Please try again.")
    buying_data = enter_products()

membership = input("Enter customer membership: ")
while membership not in ["Gold", "Silver", "Bronze"]:
    print("Invalid membership type. Please enter Gold, Silver, or Bronze.")
    membership = input("Enter customer membership: ")

discounted_bill_amount = make_bill(buying_data, membership)
if discounted_bill_amount is not None:
    print(f'The discounted amount is ${discounted_bill_amount:.2f}')
