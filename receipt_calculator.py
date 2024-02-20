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
    if is_exempt_product(product) is False:
        price += basic_sales_tax*price/100
        total_tax += basic_sales_tax*price/100
    if is_imported_product(product):
        price += import_duty*price/100
        total_tax += import_duty*price/100
    return (price, total_tax)


if __name__ == "__main__":
    print(is_exempt_product("book"))
    print(is_exempt_product("music CD"))
    print(is_exempt_product("imported box of CHOCOlates"))
    print(is_imported_product("importED box of CHOCOlates"))
    print(calculate_tax("importED box of CHOCOlates", 10.00))