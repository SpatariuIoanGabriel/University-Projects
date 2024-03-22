from unittest import TestCase
from domain import vectors as v


class MyVectorTestClass(TestCase):
    def setUp(self):
        self.vector = v.MyVector("A", "r", 1, [3])

    def testCreatePoint(self):
        self.assertEqual(self.vector.name_id, "A")
        self.assertEqual(self.vector.colour, "r")
        self.assertEqual(self.vector.vector_type, 1)
        self.assertEqual(self.vector.values, [3])

    def testSetNameID(self):
        self.vector.name_id = "A"

    def testSetColour(self):
        self.vector.colour = "r"

    def testSetVectorType(self):
        self.vector.vector_type = 1

    def testValues(self):
        self.vector.values = [3]

    def testStringRepresentation(self):
        self.assertEqual(str(self.vector), "Vector(A, r, 1, [3])")

    def testAddScalar(self):
        self.assertEqual(v.MyVector("A", "b", 1, [1]).add_scalar(5), [6])
        self.assertRaises(ValueError, v.MyVector("A", "b", 1, [1]).add_scalar, "111")
        self.assertEqual(v.MyVector("B", "b", 1, [120]).add_scalar(-10), [110])

    def testAddTwoVectors(self):
        self.assertEqual(v.MyVector("A", "m", 1, [1]).add_two_vectors(v.MyVector("B", "b", 12, [10])), [11])
        self.assertRaises(ValueError, v.MyVector("A", "b", 1, [1]).add_two_vectors, v.MyVector("B", "b", 12, [10, 110]))
        self.assertEqual(v.MyVector("C", "b", 1, [120]).add_two_vectors(v.MyVector("D", "g", 12, [1])), [121])

    def testSubtract(self):
        self.assertEqual(v.MyVector("A", "m", 1, [1]).subtract(v.MyVector("B", "b", 12, [10])), [-9])
        self.assertRaises(ValueError, v.MyVector("A", "b", 1, [1]).subtract, v.MyVector("B", "b", 12, [10, 110]))
        self.assertEqual(v.MyVector("C", "b", 1, [120]).subtract(v.MyVector("D", "g", 12, [1])), [119])

    def testMultiplication(self):
        self.assertEqual(v.MyVector("A", "m", 1, [1]).multiplication(v.MyVector("B", "b", 12, [10])), [10])
        self.assertRaises(ValueError, v.MyVector("A", "b", 1, [1]).multiplication, v.MyVector("B", "b", 12, [10, 110]))
        self.assertEqual(v.MyVector("C", "b", 1, [120]).multiplication(v.MyVector("D", "g", 12, [1])), [120])

    def testSumOfValues(self):
        self.assertEqual(v.MyVector("A", "m", 1, [1, 2, 3, 4]).sum_of_values(), 10)
        self.assertEqual(v.MyVector("X", "y", 1, [121, 4]).sum_of_values(), 125)
        self.assertEqual(v.MyVector("B", "r", 10, [11, 12]).sum_of_values(), 23)

    def testProductOfElements(self):
        self.assertEqual(v.MyVector("A", "m", 1, [1, 2, 3, 4]).product_of_elements(), 24)
        self.assertEqual(v.MyVector("B", "r", 5, [10, 4]).product_of_elements(), 40)
        self.assertEqual(v.MyVector("C", "y", 9, [5, 6, 10]).product_of_elements(), 300)

    def testAverageOfElements(self):
        self.assertEqual(v.MyVector("A", "m", 1, [1, 2, 3, 4, 5]).average_of_elements(), 3)
        self.assertEqual(v.MyVector("B", "r", 12, [5, 7]).average_of_elements(), 6)
        self.assertEqual(v.MyVector("C", "b", 3, [10, 30]).average_of_elements(), 20)

    def testMinOfVector(self):
        self.assertEqual(v.MyVector("A", "m", 1, [1, 2, 3, 4, 5]).min_of_vector(), 1)
        self.assertEqual(v.MyVector("B", "r", 12, [5, 7]).min_of_vector(), 5)
        self.assertEqual(v.MyVector("C", "b", 3, [10, 30]).min_of_vector(), 10)

    def testMaxOfVector(self):
        self.assertEqual(v.MyVector("A", "m", 1, [1, 2, 3, 4, 5]).max_of_vector(), 5)
        self.assertEqual(v.MyVector("B", "r", 12, [5, 7]).max_of_vector(), 7)
        self.assertEqual(v.MyVector("C", "b", 3, [10, 30]).max_of_vector(), 30)


class PointRepositoryTestClass(TestCase):
    def setUp(self):
        self.emptyRepository = v.VectorRepository()
        self.repository = v.VectorRepository([v.MyVector("A", "r", 1, [5]), v.MyVector("B", "b", 2, [6.1]),
                          v.MyVector("C", "g", 3, [8]), v.MyVector("D", "m", 4, [10])])

    def testCreatePointRepository(self):
        self.assertEqual(self.repository.getAllVectors(), [v.MyVector("A", "r", 1, [5]), v.MyVector("B", "b", 2, [6.1]),
                          v.MyVector("C", "g", 3, [8]), v.MyVector("D", "m", 4, [10])])

    def testAddVector(self):
        self.assertEqual(self.repository.addVector("X", "r", 1, [12]), [v.MyVector("A", "r", 1, [5]), v.MyVector("B", "b", 2, [6.1]),
                          v.MyVector("C", "g", 3, [8]), v.MyVector("D", "m", 4, [10]), v.MyVector("X", "r", 1, [12])])
        self.assertRaises(ValueError, self.repository.addVector, "X", "y", 1, [1])
        self.assertEqual(self.repository.addVector("ASD", "y", 1, [129]), [v.MyVector("A", "r", 1, [5]),
                          v.MyVector("B", "b", 2, [6.1]), v.MyVector("C", "g", 3, [8]), v.MyVector("D", "m", 4, [10]),
                          v.MyVector("X", "r", 1, [12]), v.MyVector("ASD", "y", 1, [129])])

    def testGetAllVectors(self):
        self.assertEqual(self.repository.getAllVectors(), [v.MyVector("A", "r", 1, [5]),
                          v.MyVector("B", "b", 2, [6.1]), v.MyVector("C", "g", 3, [8]), v.MyVector("D", "m", 4, [10])])

    def testGeAtIndex(self):
        self.assertEqual(self.repository.getAtIndex(0), v.MyVector("A", "r", 1, [5]))
        self.assertEqual(self.repository.getAtIndex(1), v.MyVector("B", "b", 2, [6.1]))
        self.assertRaises(IndexError, self.repository.getAtIndex, -20)

    def testUpdateVectorAtIndex(self):
        self.assertEqual(self.repository.updateVectorAtIndex(0, "UU", "y", 12, [1]), [v.MyVector("UU", "y", 12, [1]),
                          v.MyVector("B", "b", 2, [6.1]), v.MyVector("C", "g", 3, [8]), v.MyVector("D", "m", 4, [10])])
        self.assertEqual(self.repository.updateVectorAtIndex(1, "AZ", "b", 1, [121]), [v.MyVector("UU", "y", 12, [1]),
                          v.MyVector("AZ", "b", 1, [121]), v.MyVector("C", "g", 3, [8]), v.MyVector("D", "m", 4, [10])])
        self.assertRaises(IndexError, self.repository.updateVectorAtIndex, -1, "A12", "b", 1, [11])

    def testUpdateByNameID(self):
        self.assertEqual(self.repository.updateByNameID("A", "ASDF", "y", 12, [1]), [v.MyVector("ASDF", "y", 12, [1]),
                          v.MyVector("B", "b", 2, [6.1]), v.MyVector("C", "g", 3, [8]), v.MyVector("D", "m", 4, [10])])
        self.assertEqual(self.repository.updateByNameID("B", "AZ", "b", 1, [121]), [v.MyVector("ASDF", "y", 12, [1]),
                          v.MyVector("AZ", "b", 1, [121]), v.MyVector("C", "g", 3, [8]), v.MyVector("D", "m", 4, [10])])
        self.assertRaises(IndexError, self.repository.updateVectorAtIndex, -1, "A12", "b", 1, [11])

    def testDeleteVectorAtINdex(self):
        self.assertEqual(self.repository.deleteVectorAtIndex(0), [v.MyVector("B", "b", 2, [6.1]),
                          v.MyVector("C", "g", 3, [8]), v.MyVector("D", "m", 4, [10])])
        self.assertEqual(self.repository.deleteVectorAtIndex(2), [v.MyVector("B", "b", 2, [6.1]),
                          v.MyVector("C", "g", 3, [8])])
        self.assertRaises(IndexError, self.repository.deleteVectorAtIndex, -1)

    def testDeleteVectorByNameID(self):
        self.assertEqual(self.repository.deleteVectorByNameId("A"), [v.MyVector("B", "b", 2, [6.1]),
                          v.MyVector("C", "g", 3, [8]), v.MyVector("D", "m", 4, [10])])
        self.assertEqual(self.repository.deleteVectorByNameId("D"), [v.MyVector("B", "b", 2, [6.1]),
                          v.MyVector("C", "g", 3, [8])])
        self.assertRaises(IndexError, self.repository.deleteVectorByNameId, "123")