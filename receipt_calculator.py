import sys

"""List for store bought goods that are exempt of basic sales tax (10%).
Important note: the values in this list are based on the given inputs.
In case of new inputs this list might need further expansion of specific
food, book or medical product based goods."""
exempt_goods = ["book", "chocolate", "headache pills", "pills"]

basic_sales_tax = 10 #%

import_duty = 5 #%

"""Function that evaluates if given product is exempt of basic sales tax.
By iterating through the exempt_goods list, if an item can be found as a
substring inside the product name, then the product will be considered exempt."""
def is_exempt_product(product):
    for object in exempt_goods:
        if object in product.lower():
            return True
    return False

"""Function that evaluates if given product is imported. If so,
import duty sales tax will need to be applied."""
def is_imported_product(product):
    return "imported" in product.lower()

"""returns a tuple containing the new price and the total sales tax amount
for the given product."""
def calculate_tax(product, price):
    total_tax = 0
    new_price = price
    if is_exempt_product(product) is False:
        total_tax += round_up(basic_sales_tax*price/100)
        new_price += round_up(basic_sales_tax*price/100)
    if is_imported_product(product):
        total_tax += round_up(import_duty*price/100)
        new_price += round_up(import_duty*price/100)
    return (new_price, total_tax)

"""Function that returns tax in the desired format.
we need to round it up to the last two digits. Following this, if 
the last digit is in the (0,5] range, then that means we have to
round it up to the nearest 5 (0.05). Else if the last digit is a 0 or
bigger than 5, then we just round up as normal."""
def round_up(number):
    number = f"{number:.2f}"
    if 0 < int(number[-1]) <= 5:
        return float(number[-len(number):-1]+"5")
    return round(float(number),1)

"""Function that evaluates the whole basket (given list that contains tuples):
prints out the new price for every product, and also the total sales tax and price
for these items."""
def calculate_basket_details(items_list):
    sales_taxes = 0
    total = 0
    for item in items_list:
        new_price, tax = calculate_tax(item[0], item[1])
        sales_taxes += tax
        total += new_price
        print(f"{item[0]}: {new_price:.2f}")
    print(f"Sales Taxes: {sales_taxes:.2f}")
    print(f"Total: {total:.2f}")

"""Function that converts input line (either from text or from terminal)
to a tuple containing the product and its price."""
def handle_data(line):
    data = list(map(lambda x: x.strip(), line.split(' at ')))
    data[1] = float(data[1])
    return tuple(data)

"""Function that reads the content of the shopping list
from given file."""
def read_from_file(file_path):
    basket = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                basket.append(handle_data(line))
        return basket
    except FileNotFoundError:
        print("Error: given file cannot be found.")
        sys.exit()
    except ValueError:
        print("Error: one or more given prices are not convertable.")
        sys.exit()

"""Function that reads user input from terminal until user types 'Done'."""
def read_from_terminal():
    try:
        basket = []
        print('The terminal will now keep reading your input until you type "Done".')
        line = input("> ")
        while line.lower() != "done":
            basket.append(handle_data(line))
            line = input("> ")
        return basket
    except ValueError:
        print("Error: given price is not convertable.")
        sys.exit()
    except KeyboardInterrupt:
        print("\nError: terminal input has been interrupted. Application is closed.")
        sys.exit()


if __name__ == "__main__":
    """print(is_exempt_product("book"))
    print(is_exempt_product("music CD"))
    print(is_exempt_product("imported box of CHOCOlates"))
    print(is_imported_product("importED box of CHOCOlates"))
    print(calculate_tax("importED box of CHOCOlates", 10.00))"""
    """calculate_basket_details([("1 book", 12.49),
                            ("1 music CD", 14.99),
                            ("1 chocolate bar", 0.85)])
    calculate_basket_details([("1 imported box of chocolates", 10.00),
                            ("1 imported bottle of perfume", 47.50)])
    calculate_basket_details([("1 imported bottle of perfume", 27.99),
                              ("1 bottle of perfume", 18.99),
                              ("1 packet of headache pills", 9.75),
                              ("1 box of imported chocolates", 11.25)])"""
    #print(tuple(map(lambda x: x.strip(),"1 book at 56.78".split('at'))))
    """calculate_basket_details(read_from_file('input1.txt'))
    calculate_basket_details(read_from_file('input2.txt'))
    calculate_basket_details(read_from_file('input3.txt'))
    calculate_basket_details(read_from_file('input4.txt'))"""
    calculate_basket_details(read_from_terminal())
