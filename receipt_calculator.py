import sys
import re

"""List for store bought goods that are exempt of basic sales tax (10%).
Important note: the values in this list are based on the given inputs.
In case of new inputs this list might need further expansion of specific
food, book or medical product based goods."""
exempt_goods = ["book", "chocolate", "pills"]

basic_sales_tax = 10 #%

import_duty = 5 #%

def is_exempt_product(product):
    """Function that evaluates if given product is exempt of basic sales tax.
    By iterating through the exempt_goods list, if an item can be found as a
    substring inside the product name, then the product will be considered exempt."""
    for object in exempt_goods:
        if object in product.lower():
            return True
    return False

def is_imported_product(product):
    """Function that evaluates if given product is imported. If so,
    import duty sales tax will need to be applied."""
    return "imported" in product.lower()

def calculate_tax(product, price):
    """returns a tuple containing the new price and the total sales tax amount
    for the given product."""
    total_tax = 0
    new_price = price
    if is_exempt_product(product) is False:
        total_tax += round_up(basic_sales_tax*price/100)
        new_price += round_up(basic_sales_tax*price/100)
    if is_imported_product(product):
        total_tax += round_up(import_duty*price/100)
        new_price += round_up(import_duty*price/100)
    return (round(new_price,2), total_tax)

def round_up(number):
    """Function that returns tax in the desired format.
    we need to round it up to the last two digits. Following this, if 
    the last digit is in the (0,5] range, then that means we have to
    round it up to the nearest 5 (0.05). Else if the last digit is a 0 or
    bigger than 5, then we just round up as normal."""
    number = f"{number:.2f}"
    if 0 < int(number[-1]) <= 5:
        return float(number[-len(number):-1]+"5")
    return round(float(number),1)

def calculate_basket_details(items_list):
    """Function that evaluates the whole basket (given list that contains tuples):
    prints out the new price for every product, and also the total sales tax and price
    for these items."""
    sales_taxes = 0
    total = 0
    for item in items_list:
        new_price, tax = calculate_tax(item[0], item[1])
        sales_taxes += tax
        total += new_price
        print(f"{item[0]}: {new_price:.2f}")
    print(f"Sales Taxes: {sales_taxes:.2f}")
    print(f"Total: {total:.2f}")

def handle_data(line):
    """Function that converts input line (either from text or from terminal)
    to a tuple containing the product and its price."""
    data = list(map(lambda x: x.strip(), re.split(' at | AT ', line)))
    data[1] = float(data[1])
    return tuple(data)

def read_from_file(file_name):
    """Function that reads the content of the shopping list
    from given file."""
    basket = []
    try:
        with open(file_name, 'r') as file:
            for line in file:
                basket.append(handle_data(line))
        return basket
    except FileNotFoundError:
        print("Error: given file cannot be found.", file=sys.stderr)
        sys.exit()
    except ValueError:
        print("Error: one or more given prices are not convertible.", file=sys.stderr)
        sys.exit()

def read_from_terminal():
    """Function that reads user input from terminal until user types 'Done'."""
    try:
        basket = []
        print('The terminal will now keep reading your input until you type "Done".')
        line = input("> ")
        while line.lower() != "done":
            basket.append(handle_data(line))
            line = input("> ")
        return basket
    except ValueError:
        print("Error: given price is not convertible.", file=sys.stderr)
        sys.exit()
    except KeyboardInterrupt:
        print("\nError: terminal input has been interrupted. Application is closed.", file=sys.stderr)
        sys.exit()


if __name__ == "__main__":
    print("If you would like to read the shopping list from a file, please type 1.")
    print("If you would like to type in the shopping list from the terminal, please type 2.")
    try:
        number = input("> ").strip()
        while number not in "12":
            print("Incorrect input, please try again:")
            number = input("> ")
        if number == '1':
            print("Please type in the correct file name (make sure that it's in the same folder as the script):")
            file_name = input("> ")
            calculate_basket_details(read_from_file(file_name))
        else:
            calculate_basket_details(read_from_terminal())
    except KeyboardInterrupt:
        print("\nError: terminal input has been interrupted. Application is closed.", file=sys.stderr)
        sys.exit()
