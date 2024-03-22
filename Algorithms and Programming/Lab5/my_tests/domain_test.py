from unittest import TestCase
from domain import person as p


class TestPatient(TestCase):
    def setUp(self):
        self.patient = p.Patient("Peter", "Parker", "5020714225895", "covid")

    def testCreatePatient(self):
        self.assertEqual(self.patient.get_first_name(), "Peter")
        self.assertEqual(self.patient.get_last_name(), "Parker")
        self.assertEqual(self.patient.get_personal_numeric_code(), "5020714225895")
        self.assertEqual(self.patient.get_disease(), "covid")

    def testGetFirstName(self):
        self.assertEqual(self.patient.get_first_name(), "Peter")
        self.patient = p.Patient("Polly", "Pop", "5020714225895", "covid")
        self.assertEqual(self.patient.get_first_name(), "Polly")
        self.patient = p.Patient("Serban", "Marin", "5020714225895", "covid")
        self.assertEqual(self.patient.get_first_name(), "Serban")

    def testGetLastName(self):
        self.assertEqual(self.patient.get_last_name(), "Parker")
        self.patient = p.Patient("Polly", "Pop", "5020714225895", "covid")
        self.assertEqual(self.patient.get_last_name(), "Pop")
        self.patient = p.Patient("Serban", "Marin", "5020714225895", "covid")
        self.assertEqual(self.patient.get_last_name(), "Marin")

    def testGetPersonalNumericCode(self):
        self.assertEqual(self.patient.get_personal_numeric_code(), "5020714225895")
        self.patient = p.Patient("Polly", "Pop", "5020714225895", "covid")
        self.assertEqual(self.patient.get_personal_numeric_code(), "5020714225895")
        self.patient = p.Patient("Serban", "Marin", "5020714225895", "covid")
        self.assertEqual(self.patient.get_personal_numeric_code(), "5020714225895")

    def testGetDisease(self):
        self.assertEqual(p.Patient("Polly", "Pop", "5020714225895", "cancer").get_disease(), "cancer")
        self.patient = p.Patient("Serban", "Marin", "5020714225895", "flu")
        self.assertEqual(self.patient.get_disease(), "flu")

    def testSetFirstName(self):
        self.patient.first_name = "Octavian"
        self.assertEqual(self.patient.first_name, "Octavian")
        self.patient.first_name = "Laura"
        self.assertEqual(self.patient.first_name, "Laura")
        self.patient.first_name = "Sabin"
        self.assertTrue(self.patient.first_name, "Sabin")

    def testSetLastName(self):
        self.patient.last_name = "Popov"
        self.assertTrue(self.patient.last_name == "Popov")
        self.patient.last_name = "Dean"
        self.assertTrue(self.patient.last_name == "Dean")
        self.patient.last_name = "Gog"
        self.assertTrue(self.patient.last_name == "Gog")

    def testSetPersonalNumericCode(self):
        self.patient.personal_numeric_code = "5020714225895"
        self.assertTrue(self.patient.personal_numeric_code == "5020714225895")
        self.patient.personal_numeric_code = "5020714225895"
        self.assertTrue(self.patient.personal_numeric_code == "5020714225895")
        self.patient.personal_numeric_code = "5020714225895"
        self.assertTrue(self.patient.personal_numeric_code == "5020714225895")

    def test_set_disease(self):
        self.patient.disease = "cancer"
        self.assertTrue(self.patient.disease == "cancer")
        self.patient.disease = "depression"
        self.assertTrue(self.patient.disease == "depression")
        self.patient.disease = "flu"
        self.assertTrue(self.patient.disease == "flu")
