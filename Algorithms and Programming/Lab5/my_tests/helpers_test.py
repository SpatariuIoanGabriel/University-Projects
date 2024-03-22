from unittest import TestCase
from utils import helpers as h
from domain import person as p


class HelperTestCLass(TestCase):

    def testCheckColour(self):
        self.assertTrue(h.checkName("Radu"))
        self.assertRaises(ValueError, h.checkName, "Andre1")

    def testCheckCNP(self):
        self.assertTrue(h.checkPNC("5020714225895"))
        self.assertRaises(ValueError, h.checkPNC, "12345678")

    def testCheckNumberOfBeds(self):
        self.assertTrue(h.checkNumberOfBeds(1))
        self.assertTrue(h.checkNumberOfBeds(20))
        self.assertRaises(TypeError, h.checkNumberOfBeds, "12")

    def testAge(self):
        self.assertEqual(h.calculateAge(p.Patient("Peter", "Parker", "5020714225895", "covid")), 21)
        self.assertEqual(h.calculateAge(p.Patient("Michael", "Floyd", "5000714225895", "covid")), 23)
        self.assertEqual(h.calculateAge(p.Patient("Juan", "Rich", "5010714225895", "covid")), 22)
