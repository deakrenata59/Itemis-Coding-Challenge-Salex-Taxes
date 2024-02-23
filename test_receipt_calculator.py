import receipt_calculator
import unittest

class Test_ProductType(unittest.TestCase):
    """Class for testing the product evaluating functions in receipt_calculator.py.
    Important note for all classes: all class and function names start with 'test_' so Visual Studio Code's
    testing environment can recognise them as tests. Further information (such as setting up this environment)
    can be found in the README.md file."""

    def test_is_exempt_product(self):
        """Function for testing if given product is exempt of basic sales tax."""
        self.assertEqual(receipt_calculator.is_exempt_product("a BOX of CHOCOlates"), True)
        self.assertEqual(receipt_calculator.is_exempt_product("a bottle of WINE"), False)

    def test_is_imported_product(self):
        """Function for testing if given product is imported."""
        self.assertEqual(receipt_calculator.is_imported_product("an IMPORTED bottle of wine"), True)
        self.assertEqual(receipt_calculator.is_imported_product("a bottle of wine"), False)

class Test_NewPriceAndTax(unittest.TestCase):
    """Class for testing the round_up and calculate_tax funtions in receipt_calculator.py"""

    def test_round_up(self):
        """Function for testing if round_up function is working properly."""
        self.assertEqual(receipt_calculator.round_up(7.125), 7.15)
        self.assertEqual(receipt_calculator.round_up(4.00), 4.00)
        self.assertEqual(receipt_calculator.round_up(4.1985), 4.20)
        self.assertEqual(receipt_calculator.round_up(0.56), 0.60)
        self.assertEqual(receipt_calculator.round_up(2.05), 2.05)

    def test_calculate_tax(self):
        """Function for testing the tax calculator for a given product and its price."""
        self.assertEqual(receipt_calculator.calculate_tax("1 book", 12.49), (12.49, 0.00))
        self.assertEqual(receipt_calculator.calculate_tax("1 music CD", 14.99), (16.49, 1.50))
        self.assertEqual(receipt_calculator.calculate_tax("1 imported box of chocolates", 10.00), (10.50, 0.50))
        self.assertEqual(receipt_calculator.calculate_tax("1 imported bottle of perfume", 47.50), (54.65, 7.15))

class Test_DataHandling(unittest.TestCase):
    """Class for testing the data handling (turning user input or file text to processable data)."""

    def test_handle_data(self):
        """Function for testing the handle_data function."""
        self.assertEqual(receipt_calculator.handle_data("1 book at 12.49"), ("1 book", 12.49))
        self.assertEqual(receipt_calculator.handle_data("    1 book     at      12.49     "), ("1 book", 12.49))
        self.assertEqual(receipt_calculator.handle_data("1 book AT 12.49"), ("1 book", 12.49))

class Test_ReadingFromFile(unittest.TestCase):
    """Class for testing reading from a file."""
    def test_read_from_file(self):
        """Function that tests the reading results from given file."""
        self.assertEqual(receipt_calculator.read_from_file('input1.txt'), [("1 book", 12.49),
                                                                           ("1 music CD", 14.99),
                                                                           ("1 chocolate bar", 0.85)])
        self.assertEqual(receipt_calculator.read_from_file('input2.txt'), [("1 imported box of chocolates", 10.00),
                                                                           ("1 imported bottle of perfume", 47.50)])
        self.assertEqual(receipt_calculator.read_from_file('input3.txt'), [("1 imported bottle of perfume", 27.99),
                                                                           ("1 bottle of perfume", 18.99), 
                                                                           ("1 packet of headache pills", 9.75), 
                                                                           ("1 box of imported chocolates", 11.25)])
        
    def test_filenotfound_error(self):
        try:
            self.assertRaises(FileNotFoundError, receipt_calculator.read_from_file('input4.txt'))
        except SystemExit:
            pass

    def test_value_error(self):
        try:
            self.assertRaises(ValueError, receipt_calculator.read_from_file('incorrect_input.txt'))
        except SystemExit:
            pass

if __name__ == '__main__':
    """Gathers and runs all tests."""
    unittest.main()

