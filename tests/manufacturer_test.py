import unittest
from models.manufacturer import Manufacturer

class TestManufacturer (unittest.TestCase):

    def setUp(self):
        self.manufacturer = Manufacturer("Nike", "Fast Shipping")
    
    def test_manufacturer_has_name(self):
        self.assertEqual = ("Nike", self.manufacturer.name)

    def test_manufacturer_shipping_speed(self):
        self.assertEqual = ("Fast Shipping", self.manufacturer.shipping_speed)

    def test_manufacturer_status(self):
        self.assertEqual = (True, self.manufacturer.status)

    def test_manufacturer_has_id(self):
        self.assertEqual = (None, self.manufacturer.id)