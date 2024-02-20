"""List for store bought goods that are exempt of basic sales tax (10%).
Important note: the values in this list are based on the given inputs.
In case of new inputs this list might need further expansion of specific
food, book or medical product based goods."""
exempt_goods = ["book", "chocolate", "headache pills"]

"""Function that evaluates if given product is exempt of basic sales tax.
By iterating through the exempt_goods list, if an item can be found as a
substring inside the product name, then the product will be considered exempt."""
def is_exempt_product(product):
    for object in exempt_goods:
        if object in product:
            return True
    return False

"""returns a tuple containing the new price and the sales tax amount."""
def calculate_tax(product, price):
    pass


if __name__ == "__main__":
    print(is_exempt_product("book"))
    print(is_exempt_product("music CD"))
    print(is_exempt_product("imported box of chocolates"))