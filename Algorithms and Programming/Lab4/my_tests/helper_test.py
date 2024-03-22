from unittest import TestCase
from utils import helpers as h


class HelperTestCLass(TestCase):

    def testCheckColour(self):
        self.assertTrue(h.checkColour("r"))
        self.assertRaises(ValueError, h.checkColour, "p")

    def testCheckType(self):
        self.assertTrue(h.checkType(1))
        self.assertFalse(h.checkType(-10))
        self.assertEqual(h.checkType(5), True)
        self.assertRaises(TypeError, h.checkType, "a")

    def testValues(self):
        self.assertTrue(h.checkValue([2, 7]))
        self.assertRaises(ValueError, h.checkValue, ["abc"])
