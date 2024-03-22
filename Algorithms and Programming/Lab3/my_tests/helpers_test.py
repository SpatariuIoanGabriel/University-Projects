from unittest import TestCase
from utils import helpers as h


class HelperTestCLass(TestCase):
    def testCheckColour(self):
        self.assertTrue(h.checkColour("red"))
        self.assertRaises(ValueError, h.checkColour, "pink")
