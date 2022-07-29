import unittest
from models.product import Product

class TestProduct(unittest.TestCase):

    def setUp(self):
        self.product = Product("Nike Cortez", "Navy/White", 4, 90, 135, "Nike")
    
    def test_product_has_name(self):
        self.assertEqual("Nike Cortez", self.product.name)

    def test_product_has_description(self):
        self.assertEqual("Navy/White", self.product.description)

    def test_product_stock_quantity(self):
        self.assertEqual(4, self.product.stock_quantity)

    def test_product_buying_cost(self):
        self.assertEqual(90, self.product.buying_cost)

    def test_product_selling_price(self):
        self.assertEqual(135, self.product.selling_price)

    def test_product_has_manufacturer(self):
        self.assertEqual("Nike", self.product.manufacturer)
    
    def test_product_has_id(self):
        self.assertEqual = (None, self.product.id)
