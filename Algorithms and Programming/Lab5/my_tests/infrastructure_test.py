from unittest import TestCase
from infrastructure.repositories import *
from domain.person import Patient


class DepartmentTest(TestCase):
    def setUp(self):
        self.department = Department("dep1", "dis1", 13, [Patient("Andrei", "Pop", "5020714225890", "cancer"),
                                             Patient("David", "Maria", "5020714225891", "covid"),
                                             Patient("Alex", "Stefan", "5020714225892", "tuberculosis")])

    def testCreateDepartment(self):
        self.assertEqual(self.department.get_id_(), "dep1")
        self.assertEqual(self.department.get_name(), "dis1")
        self.assertEqual(self.department.get_number_of_beds(), 13)
        self.assertEqual(self.department.get_list_of_patients(), [Patient("Andrei", "Pop", "5020714225890", "cancer"),
                                             Patient("David", "Maria", "5020714225891", "covid"),
                                             Patient("Alex", "Stefan", "5020714225892", "tuberculosis")])

    def testGetId(self):
        self.assertEqual(self.department.get_id_(), "dep1")
        self.department = Department("dep2", "dis1", 13, [Patient("Andrei", "Pop", "5020714225890", "cancer"),
                                             Patient("David", "Maria", "5020714225891", "covid"),
                                             Patient("Alex", "Stefan", "5020714225892", "tuberculosis")])
        self.assertEqual(self.department.get_id_(), "dep2")
        self.department = Department("dep2", "dis1", 13, [Patient("Andrei", "Pop", "5020714225890", "cancer"),
                                                         Patient("David", "Maria", "5020714225891", "covid"),
                                                         Patient("Alex", "Stefan", "5020714225892", "tuberculosis")])
        self.assertEqual(self.department.get_id_(), "dep2")

    def testGetName(self):
        self.assertEqual(self.department.get_name(), "dis1")
        self.department = Department("dep2", "dis22", 13, [Patient("Andrei", "Pop", "5020714225890", "cancer"),
                                                          Patient("David", "Maria", "5020714225891", "covid"),
                                                          Patient("Alex", "Stefan", "5020714225892", "tuberculosis")])
        self.assertEqual(self.department.get_name(), "dis22")
        self.department = Department("dep3", "dis11", 13, [Patient("Andrei", "Pop", "5020714225890", "cancer"),
                                                          Patient("David", "Maria", "5020714225891", "covid"),
                                                          Patient("Alex", "Stefan", "5020714225892", "tuberculosis")])
        self.assertEqual(self.department.get_name(), "dis11")

    def testGetNrBeds(self):
        self.assertEqual(self.department.get_number_of_beds(), 13)
        self.department = Department("dep2", "dis22", 22, [Patient("Andrei", "Pop", "5020714225890", "cancer"),
                                                          Patient("David", "Maria", "5020714225891", "covid"),
                                                          Patient("Alex", "Stefan", "5020714225892", "tuberculosis")])
        self.assertEqual(self.department.get_number_of_beds(), 22)
        self.department = Department("dep3", "dis11", 13, [Patient("Andrei", "Pop", "5020714225890", "cancer"),
                                                          Patient("David", "Maria", "5020714225891", "covid"),
                                                          Patient("Alex", "Stefan", "5020714225892", "tuberculosis")])
        self.assertEqual(self.department.get_number_of_beds(), 13)

    def testGetListOfPatients(self):
        self.assertEqual(self.department.get_list_of_patients(), [Patient("Andrei", "Pop", "5020714225890", "cancer"),
                                                           Patient("David", "Maria", "5020714225891", "covid"),
                                                           Patient("Alex", "Stefan", "5020714225892", "tuberculosis")])
        self.department = Department("dep2", "dis22", 22, [Patient("Andrei", "Pop", "5020714225890", "cancer"),
                                                           Patient("David", "Maria", "5020714225891", "covid"),
                                                           Patient("Alex", "Stefan", "5020714225892", "tuberculosis")])
        self.assertEqual(self.department.get_list_of_patients(), [Patient("Andrei", "Pop", "5020714225890", "cancer"),
                                                           Patient("David", "Maria", "5020714225891", "covid"),
                                                           Patient("Alex", "Stefan", "5020714225892", "tuberculosis")])
        self.department = Department("dep3", "dis11", 13, [Patient("Andrei", "Pop", "5020714225890", "cancer"),
                                                          Patient("David", "Maria", "5020714225891", "covid"),
                                                          Patient("Alex", "Stefan", "5020714225892", "tuberculosis")])
        self.assertEqual(self.department.get_list_of_patients(), [Patient("Andrei", "Pop", "5020714225890", "cancer"),
                                                           Patient("David", "Maria", "5020714225891", "covid"),
                                                           Patient("Alex", "Stefan", "5020714225892", "tuberculosis")])

    def testAddPatient(self):
        self.assertEqual(self.department.addPatient("Mihai", "Stefan", "1020714225892", "tuberculosis"),
                         [Patient("Andrei", "Pop", "5020714225890", "cancer"),
                          Patient("David", "Maria", "5020714225891", "covid"),
                          Patient("Alex", "Stefan", "5020714225892", "tuberculosis"),
                          Patient("Mihai", "Stefan", "1020714225892", "tuberculosis")])
        self.assertRaises(ValueError, self.department.addPatient, "Mihai", "Stefan", "1020714225892", "tuberculosis")
        self.assertEqual(self.department.addPatient("Mircea", "Stefan", "2020714225892", "tuberculosis"),
                         [Patient("Andrei", "Pop", "5020714225890", "cancer"),
                          Patient("David", "Maria", "5020714225891", "covid"),
                          Patient("Alex", "Stefan", "5020714225892", "tuberculosis"),
                          Patient("Mihai", "Stefan", "1020714225892", "tuberculosis"),
                          Patient("Mircea", "Stefan", "2020714225892", "tuberculosis")])

    def testGetAtIndex(self):
        self.assertEqual(self.department.getPatientByIndex(0), Patient("Andrei", "Pop", "5020714225890", "cancer"))
        self.assertEqual(self.department.getPatientByIndex(1), Patient("David", "Maria", "5020714225891", "covid"))
        self.assertRaises(IndexError, self.department.getPatientByIndex, -10)

    def testUpdateAtIndex(self):
        self.assertEqual(self.department.updatePatientByIndex(0, "Rares", "Stefan", "tuberculosis"),
                         [Patient("Rares", "Stefan", "5020714225890", "tuberculosis"),
                          Patient("David", "Maria", "5020714225891", "covid"),
                          Patient("Alex", "Stefan", "5020714225892", "tuberculosis")])
        self.assertEqual(self.department.updatePatientByIndex(0, "Victor", "Stefan", "tuberculosis"),
                         [Patient("Victor", "Stefan", "5020714225890", "tuberculosis"),
                          Patient("David", "Maria", "5020714225891", "covid"),
                          Patient("Alex", "Stefan", "5020714225892", "tuberculosis")])
        self.assertRaises(IndexError, self.department.updatePatientByIndex, -1, "Rares", "Stefan", "tuberculosis")

    def testDeleteAtIndex(self):
        self.assertEqual(self.department.deletePatientAtIndex(0), [Patient("David", "Maria", "5020714225891", "covid"),
                          Patient("Alex", "Stefan", "5020714225892", "tuberculosis")])
        self.assertEqual(self.department.deletePatientAtIndex(0), [Patient("Alex", "Stefan", "5020714225892", "tuberculosis")])
        self.assertRaises(IndexError, self.department.deletePatientAtIndex, 10)


class HospitalTest(TestCase):
    def setUp(self):
        self.hospital = Hospital([Department("dep1", "dis1", 13, [Patient("Andrei", "Pop", "5020714225890", "cancer"),
                                             Patient("David", "Maria", "5020714225891", "covid"),
                                             Patient("Alex", "Stefan", "5020714225892", "tuberculosis")]),
                                  Department("dep2", "dis2", 10,  [Patient("Marin", "Chad", "5020714225893", "covid"),
                                             Patient("Raul", "Marc", "5020714225894", "covid"),
                                             Patient("Paul", "Apostol", "5020714225895", "covid"),
                                             Patient("Tudor", "Lung", "5020714225896", "sida"),
                                             Patient("Anca", "Serban", "5020714225897", "flu")]),
                                  Department("dep3", "dis3", 20, [Patient("Nicu", "Alb", "5020714225898", "cancer"),
                                             Patient("Eugenia", "Nour", "5020714225899", "covid"),
                                             Patient("Sandra", "Dinu", "5020714225805", "covid"),
                                             Patient("Costel", "Virgil", "5020714225815", "malaria"),
                                             Patient("Stefan", "Mircea", "5020714225825", "covid"),
                                             Patient("Anton", "Baltazar", "5020714225835", "hypertension"),
                                             Patient("Cristi", "Chin", "5020714225845", "cancer")]),
                                  Department("dep4", "dis4", 5, [Patient("Marcel", "Nica", "5020214225855", "parkinson"),
                                            Patient("Brian", "Maier", "5020114225865", "covid")])])

    def testCreateHospital(self):
        self.assertEqual(self.hospital.getAllDepartments(), [Department("dep1", "dis1", 13,
                                            [Patient("Andrei", "Pop", "5020714225890", "cancer"),
                                             Patient("David", "Maria", "5020714225891", "covid"),
                                             Patient("Alex", "Stefan", "5020714225892", "tuberculosis")]),
                                Department("dep2", "dis2", 10,  [Patient("Marin", "Chad", "5020714225893", "covid"),
                                             Patient("Raul", "Marc", "5020714225894", "covid"),
                                             Patient("Paul", "Apostol", "5020714225895", "covid"),
                                             Patient("Tudor", "Lung", "5020714225896", "sida"),
                                             Patient("Anca", "Serban", "5020714225897", "flu")]),
                                Department("dep3", "dis3", 20, [Patient("Nicu", "Alb", "5020714225898", "cancer"),
                                             Patient("Eugenia", "Nour", "5020714225899", "covid"),
                                             Patient("Sandra", "Dinu", "5020714225805", "covid"),
                                             Patient("Costel", "Virgil", "5020714225815", "malaria"),
                                             Patient("Stefan", "Mircea", "5020714225825", "covid"),
                                             Patient("Anton", "Baltazar", "5020714225835", "hypertension"),
                                             Patient("Cristi", "Chin", "5020714225845", "cancer")]),
                                Department("dep4", "dis4", 5, [Patient("Marcel", "Nica", "5020214225855", "parkinson"),
                                            Patient("Brian", "Maier", "5020114225865", "covid")])])

    def testGetListOfDepartments(self):
        self.assertEqual(self.hospital.get_list_of_departments(), [Department("dep1", "dis1", 13,
                                            [Patient("Andrei", "Pop", "5020714225890", "cancer"),
                                             Patient("David", "Maria", "5020714225891", "covid"),
                                             Patient("Alex", "Stefan", "5020714225892", "tuberculosis")]),
                                  Department("dep2", "dis2", 10,  [Patient("Marin", "Chad", "5020714225893", "covid"),
                                             Patient("Raul", "Marc", "5020714225894", "covid"),
                                             Patient("Paul", "Apostol", "5020714225895", "covid"),
                                             Patient("Tudor", "Lung", "5020714225896", "sida"),
                                             Patient("Anca", "Serban", "5020714225897", "flu")]),
                                  Department("dep3", "dis3", 20, [Patient("Nicu", "Alb", "5020714225898", "cancer"),
                                             Patient("Eugenia", "Nour", "5020714225899", "covid"),
                                             Patient("Sandra", "Dinu", "5020714225805", "covid"),
                                             Patient("Costel", "Virgil", "5020714225815", "malaria"),
                                             Patient("Stefan", "Mircea", "5020714225825", "covid"),
                                             Patient("Anton", "Baltazar", "5020714225835", "hypertension"),
                                             Patient("Cristi", "Chin", "5020714225845", "cancer")]),
                                  Department("dep4", "dis4", 5, [Patient("Marcel", "Nica", "5020214225855", "parkinson"),
                                            Patient("Brian", "Maier", "5020114225865", "covid")])])

    def testAddDepartment(self):
        self.assertEqual(self.hospital.addDepartment("dep5", "dis4", 5, [Patient("Marcel", "Nica", "5020214225855", "parkinson"),
                                                          Patient("Brian", "Maier", "5020114225865", "covid")]),
                         [Department("dep1", "dis1", 13, [Patient("Andrei", "Pop", "5020714225890", "cancer"),
                                                          Patient("David", "Maria", "5020714225891", "covid"),
                                                          Patient("Alex", "Stefan", "5020714225892", "tuberculosis")]),
                         Department("dep2", "dis2", 10, [Patient("Marin", "Chad", "5020714225893", "covid"),
                                                         Patient("Raul", "Marc", "5020714225894", "covid"),
                                                         Patient("Paul", "Apostol", "5020714225895", "covid"),
                                                         Patient("Tudor", "Lung", "5020714225896", "sida"),
                                                         Patient("Anca", "Serban", "5020714225897", "flu")]),
                         Department("dep3", "dis3", 20, [Patient("Nicu", "Alb", "5020714225898", "cancer"),
                                                         Patient("Eugenia", "Nour", "5020714225899", "covid"),
                                                         Patient("Sandra", "Dinu", "5020714225805", "covid"),
                                                         Patient("Costel", "Virgil", "5020714225815", "malaria"),
                                                         Patient("Stefan", "Mircea", "5020714225825", "covid"),
                                                         Patient("Anton", "Baltazar", "5020714225835", "hypertension"),
                                                         Patient("Cristi", "Chin", "5020714225845", "cancer")]),
                         Department("dep4", "dis4", 5, [Patient("Marcel", "Nica", "5020214225855", "parkinson"),
                                                        Patient("Brian", "Maier", "5020114225865", "covid")]),
                         Department("dep5", "dis4", 5, [Patient("Marcel", "Nica", "5020214225855", "parkinson"),
                                            Patient("Brian", "Maier", "5020114225865", "covid")])])
        self.assertRaises(ValueError, self.hospital.addDepartment, "dep5", "dis4", 5,
                         [Patient("Marcel", "Nica", "5020214225855", "parkinson"),
                         Patient("Brian", "Maier", "5020114225865", "covid")])

    def testGetAtIndex(self):
        self.assertEqual(self.hospital.getDepartmentByIndex(0), Department("dep1", "dis1", 13,
                                                        [Patient("Andrei", "Pop", "5020714225890", "cancer"),
                                                         Patient("David", "Maria", "5020714225891", "covid"),
                                                         Patient("Alex", "Stefan", "5020714225892", "tuberculosis")]))
        self.assertEqual(self.hospital.getDepartmentByIndex(1), Department("dep2", "dis2", 10,
                                                        [Patient("Marin", "Chad", "5020714225893", "covid"),
                                                         Patient("Raul", "Marc", "5020714225894", "covid"),
                                                         Patient("Paul", "Apostol", "5020714225895", "covid"),
                                                         Patient("Tudor", "Lung", "5020714225896", "sida"),
                                                         Patient("Anca", "Serban", "5020714225897", "flu")]))
        self.assertRaises(IndexError, self.hospital.getDepartmentByIndex, -10)

    def testUpdateAtIndex(self):
        self.assertEqual(self.hospital.updateDepartmentByIndex(0,
                        "dep7", "dis4", 5, [Patient("Marcel", "Nica", "5020219125855", "parkinson"),
                                            Patient("Brian", "Maier", "5020114225865", "covid")]),
                        [Department("dep7", "dis4", 5, [Patient("Marcel", "Nica", "5020219125855", "parkinson"),
                                            Patient("Brian", "Maier", "5020114225865", "covid")]),
                        Department("dep2", "dis2", 10, [Patient("Marin", "Chad", "5020714225893", "covid"),
                                                        Patient("Raul", "Marc", "5020714225894", "covid"),
                                                        Patient("Paul", "Apostol", "5020714225895", "covid"),
                                                        Patient("Tudor", "Lung", "5020714225896", "sida"),
                                                        Patient("Anca", "Serban", "5020714225897", "flu")]),
                        Department("dep3", "dis3", 20, [Patient("Nicu", "Alb", "5020714225898", "cancer"),
                                                        Patient("Eugenia", "Nour", "5020714225899", "covid"),
                                                        Patient("Sandra", "Dinu", "5020714225805", "covid"),
                                                        Patient("Costel", "Virgil", "5020714225815", "malaria"),
                                                        Patient("Stefan", "Mircea", "5020714225825", "covid"),
                                                        Patient("Anton", "Baltazar", "5020714225835", "hypertension"),
                                                        Patient("Cristi", "Chin", "5020714225845", "cancer")]),
                        Department("dep4", "dis4", 5, [Patient("Marcel", "Nica", "5020214225855", "parkinson"),
                                                       Patient("Brian", "Maier", "5020114225865", "covid")])])
        self.assertEqual(self.hospital.updateDepartmentByIndex(0,
                         "dep22", "dis5", 5, [Patient("Mihai", "Nica", "5120219125855", "parkinson")]),
                         [Department("dep22", "dis5", 5, [Patient("Mihai", "Nica", "5120219125855", "parkinson")]),
                         Department("dep2", "dis2", 10, [Patient("Marin", "Chad", "5020714225893", "covid"),
                                                         Patient("Raul", "Marc", "5020714225894", "covid"),
                                                         Patient("Paul", "Apostol", "5020714225895", "covid"),
                                                         Patient("Tudor", "Lung", "5020714225896", "sida"),
                                                         Patient("Anca", "Serban", "5020714225897", "flu")]),
                         Department("dep3", "dis3", 20, [Patient("Nicu", "Alb", "5020714225898", "cancer"),
                                                         Patient("Eugenia", "Nour", "5020714225899", "covid"),
                                                         Patient("Sandra", "Dinu", "5020714225805", "covid"),
                                                         Patient("Costel", "Virgil", "5020714225815", "malaria"),
                                                         Patient("Stefan", "Mircea", "5020714225825", "covid"),
                                                         Patient("Anton", "Baltazar", "5020714225835", "hypertension"),
                                                         Patient("Cristi", "Chin", "5020714225845", "cancer")]),
                         Department("dep4", "dis4", 5, [Patient("Marcel", "Nica", "5020214225855", "parkinson"),
                                                        Patient("Brian", "Maier", "5020114225865", "covid")])])
        self.assertRaises(IndexError, self.hospital.updateDepartmentByIndex, -1,
                          "dep5", "dis4", 5, [Patient("Marcel", "Nica", "5020214225855", "parkinson"),
                                              Patient("Brian", "Maier", "5020114225865", "covid")])

    def testDeleteAtIndex(self):
        self.assertEqual(self.hospital.deleteDepartmentAtIndex(0),
                         [Department("dep2", "dis2", 10,  [Patient("Marin", "Chad", "5020714225893", "covid"),
                                             Patient("Raul", "Marc", "5020714225894", "covid"),
                                             Patient("Paul", "Apostol", "5020714225895", "covid"),
                                             Patient("Tudor", "Lung", "5020714225896", "sida"),
                                             Patient("Anca", "Serban", "5020714225897", "flu")]),
                         Department("dep3", "dis3", 20, [Patient("Nicu", "Alb", "5020714225898", "cancer"),
                                             Patient("Eugenia", "Nour", "5020714225899", "covid"),
                                             Patient("Sandra", "Dinu", "5020714225805", "covid"),
                                             Patient("Costel", "Virgil", "5020714225815", "malaria"),
                                             Patient("Stefan", "Mircea", "5020714225825", "covid"),
                                             Patient("Anton", "Baltazar", "5020714225835", "hypertension"),
                                             Patient("Cristi", "Chin", "5020714225845", "cancer")]),
                         Department("dep4", "dis4", 5, [Patient("Marcel", "Nica", "5020214225855", "parkinson"),
                                             Patient("Brian", "Maier", "5020114225865", "covid")])])
        self.assertEqual(self.hospital.deleteDepartmentAtIndex(0),
                        [Department("dep3", "dis3", 20, [Patient("Nicu", "Alb", "5020714225898", "cancer"),
                                                         Patient("Eugenia", "Nour", "5020714225899", "covid"),
                                                         Patient("Sandra", "Dinu", "5020714225805", "covid"),
                                                         Patient("Costel", "Virgil", "5020714225815", "malaria"),
                                                         Patient("Stefan", "Mircea", "5020714225825", "covid"),
                                                         Patient("Anton", "Baltazar", "5020714225835", "hypertension"),
                                                         Patient("Cristi", "Chin", "5020714225845", "cancer")]),
                        Department("dep4", "dis4", 5, [Patient("Marcel", "Nica", "5020214225855", "parkinson"),
                                                      Patient("Brian", "Maier", "5020114225865", "covid")])])
        self.assertRaises(IndexError, self.hospital.deleteDepartmentAtIndex, 10)