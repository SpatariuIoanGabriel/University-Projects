from unittest import TestCase
from domain import numbers as n


class MyPointTestClass(TestCase):
    def setUp(self):
        self.point = n.MyPoint(5, 6, "red")

    def testCreatePoint(self):
        self.assertEqual(self.point.coord_x, 5)
        self.assertEqual(self.point.coord_y, 6)
        self.assertEqual(self.point.colour, "red")

    def testSetCoord_x(self):
        self.point.coord_x = 1

    def testSetCoord_y(self):
        self.point.coord_y = 2

    def testSetColour(self):
        self.point.color = "green"

    def testStringRepresentation(self):
        self.assertEqual(str(self.point), "Point(5, 6, red)")


class PointRepositoryTestClass(TestCase):
    def setUp(self):
        self.emptyRepository = n.PointRepository()
        self.repository = n.PointRepository([n.MyPoint(1, 2, "red"), n.MyPoint(2, 3, "green"), n.MyPoint(3, 4, "blue"),
                              n.MyPoint(5, 6, "yellow"), n.MyPoint(6, 7, "magenta"), n.MyPoint(10, 11, "red"),
                              n.MyPoint(10, 12, "blue"), n.MyPoint(15, 16, "green"), n.MyPoint(20, 21, "red"),
                              n.MyPoint(-10, -1, "magenta")])

    def testCreatePointRepository(self):
        self.assertEqual(self.repository.getAllPoints(), [n.MyPoint(1, 2, "red"), n.MyPoint(2, 3, "green"), n.MyPoint(3, 4, "blue"),
                              n.MyPoint(5, 6, "yellow"), n.MyPoint(6, 7, "magenta"), n.MyPoint(10, 11, "red"),
                              n.MyPoint(10, 12, "blue"), n.MyPoint(15, 16, "green"), n.MyPoint(20, 21, "red"),
                              n.MyPoint(-10, -1, "magenta")])

    def testAddPoint(self):
        self.assertEqual(self.repository.addPoint(11, 10, "red"), [n.MyPoint(1, 2, "red"), n.MyPoint(2, 3, "green"),
                              n.MyPoint(3, 4, "blue"), n.MyPoint(5, 6, "yellow"), n.MyPoint(6, 7, "magenta"),
                              n.MyPoint(10, 11, "red"), n.MyPoint(10, 12, "blue"), n.MyPoint(15, 16, "green"),
                              n.MyPoint(20, 21, "red"), n.MyPoint(-10, -1, "magenta"), n.MyPoint(11, 10, "red")])
        self.assertRaises(ValueError, self.repository.addPoint, 2, 3, "pink")
        self.assertEqual(self.repository.addPoint(-22, 3, "blue"), [n.MyPoint(1, 2, "red"), n.MyPoint(2, 3, "green"), n.MyPoint(3, 4, "blue"),
                              n.MyPoint(5, 6, "yellow"), n.MyPoint(6, 7, "magenta"), n.MyPoint(10, 11, "red"),
                              n.MyPoint(10, 12, "blue"), n.MyPoint(15, 16, "green"), n.MyPoint(20, 21, "red"),
                              n.MyPoint(-10, -1, "magenta"), n.MyPoint(11, 10, "red"), n.MyPoint(-22, 3, "blue")])

    def testGetAllPoints(self):
        self.assertEqual(self.repository.getAllPoints(), [n.MyPoint(1, 2, "red"), n.MyPoint(2, 3, "green"), n.MyPoint(3, 4, "blue"),
                              n.MyPoint(5, 6, "yellow"), n.MyPoint(6, 7, "magenta"), n.MyPoint(10, 11, "red"),
                              n.MyPoint(10, 12, "blue"), n.MyPoint(15, 16, "green"), n.MyPoint(20, 21, "red"),
                              n.MyPoint(-10, -1, "magenta")])

    def testGetPointAtIndex(self):
        self.assertEqual(self.repository.getPointAtIndex(0), n.MyPoint(1, 2, "red"))
        self.assertEqual(self.repository.getPointAtIndex(1), n.MyPoint(2, 3, "green"))
        self.assertRaises(IndexError, self.repository.getPointAtIndex, -20)

    def testGetPointsOfGivenColour(self):
        self.assertEqual(self.repository.getPointsOfGivenColour("red"), [n.MyPoint(1, 2, "red"),
                              n.MyPoint(10, 11, "red"), n.MyPoint(20, 21, "red")])
        self.assertEqual(self.repository.getPointsOfGivenColour("blue"), [n.MyPoint(3, 4, "blue"), n.MyPoint(10, 12, "blue")])
        self.assertRaises(ValueError, self.repository.getPointsOfGivenColour, "black")

    def testGetPointsInsideSquare(self):
        self.assertIsInstance(self.repository.getPointsInsideSquare(1, 1, 10), n.PointRepository)
        self.assertEqual(self.repository.getPointsInsideSquare(1, 2, 2), n.PointRepository([n.MyPoint(1, 2, "red")]))
        self.assertEqual(self.repository.getPointsInsideSquare(1, 4, 3), n.PointRepository([n.MyPoint(1, 2, "red"),
                              n.MyPoint(2, 3, "green"), n.MyPoint(3, 4, "blue")]))

    def testMinimumDistanceBetweenPoints(self):
        self.assertEqual(self.repository.minimumDistanceBetweenTwoPoints(), 1.0)

    def testUpdatePoint(self):
        self.assertEqual(self.repository.updatePoint(1, 10, -1, "blue"), [n.MyPoint(1, 2, "red"), n.MyPoint(10, -1, "blue"),
                              n.MyPoint(3, 4, "blue"), n.MyPoint(5, 6, "yellow"), n.MyPoint(6, 7, "magenta"), n.MyPoint(10, 11, "red"),
                              n.MyPoint(10, 12, "blue"), n.MyPoint(15, 16, "green"), n.MyPoint(20, 21, "red"), n.MyPoint(-10, -1, "magenta")])
        self.assertEqual(self.repository.updatePoint(0, 3, 11, "red"), [n.MyPoint(3, 11, "red"), n.MyPoint(10, -1, "blue"),
                              n.MyPoint(3, 4, "blue"), n.MyPoint(5, 6, "yellow"), n.MyPoint(6, 7, "magenta"), n.MyPoint(10, 11, "red"),
                              n.MyPoint(10, 12, "blue"), n.MyPoint(15, 16, "green"), n.MyPoint(20, 21, "red"), n.MyPoint(-10, -1, "magenta")])
        self.assertRaises(IndexError, self.repository.updatePoint, -1, 3, 11, "red")

    def testDeletePoint(self):
        self.assertEqual(self.repository.deletePoint(0), [n.MyPoint(2, 3, "green"), n.MyPoint(3, 4, "blue"),
                              n.MyPoint(5, 6, "yellow"), n.MyPoint(6, 7, "magenta"), n.MyPoint(10, 11, "red"),
                              n.MyPoint(10, 12, "blue"), n.MyPoint(15, 16, "green"), n.MyPoint(20, 21, "red"),
                              n.MyPoint(-10, -1, "magenta")])
        self.assertEqual(self.repository.deletePoint(2), [n.MyPoint(2, 3, "green"), n.MyPoint(3, 4, "blue"),
                              n.MyPoint(6, 7, "magenta"), n.MyPoint(10, 11, "red"),
                              n.MyPoint(10, 12, "blue"), n.MyPoint(15, 16, "green"), n.MyPoint(20, 21, "red"),
                              n.MyPoint(-10, -1, "magenta")])
        self.assertRaises(IndexError, self.repository.deletePoint, -1)

    def testDeleteAllPointsInSquare(self):
        self.assertEqual(self.repository.deleteAllPointsInSquare(-1, 4, 10), n.PointRepository([n.MyPoint(5, 6, "yellow"),
                              n.MyPoint(6, 7, "magenta"), n.MyPoint(10, 11, "red"), n.MyPoint(10, 12, "blue"),
                              n.MyPoint(15, 16, "green"), n.MyPoint(20, 21, "red"), n.MyPoint(-10, -1, "magenta")]))
        self.assertEqual(self.repository.deleteAllPointsInSquare(1, 12, 7), n.PointRepository([n.MyPoint(10, 11, "red"),
                              n.MyPoint(10, 12, "blue"), n.MyPoint(15, 16, "green"), n.MyPoint(20, 21, "red"),
                              n.MyPoint(-10, -1, "magenta")]))
        self.assertEqual(self.repository.deleteAllPointsInSquare(10, 4, 5), n.PointRepository([n.MyPoint(10, 11, "red"),
                              n.MyPoint(10, 12, "blue"), n.MyPoint(15, 16, "green"), n.MyPoint(20, 21, "red"),
                              n.MyPoint(-10, -1, "magenta")]))

    def testPlotAllPoints(self):
        self.assertEqual(self.repository.plotAllPoints(), None)

    def testGetAllPointsInsideCircle(self):
        self.assertEqual(self.repository.getAllPointsInsideCircle(0, 0, 10), n.PointRepository([n.MyPoint(1, 2, "red"),
                              n.MyPoint(2, 3, "green"), n.MyPoint(3, 4, "blue"), n.MyPoint(5, 6, "yellow"), n.MyPoint(6, 7, "magenta")]))
        self.assertEqual(self.repository.getAllPointsInsideCircle(1, 1, 20), n.PointRepository([n.MyPoint(1, 2, "red"),
                              n.MyPoint(2, 3, "green"), n.MyPoint(3, 4, "blue"), n.MyPoint(5, 6, "yellow"),
                              n.MyPoint(6, 7, "magenta"), n.MyPoint(10, 11, "red"), n.MyPoint(10, 12, "blue"),
                              n.MyPoint(-10, -1, "magenta")]))
        self.assertRaises(ValueError, self.repository.getAllPointsInsideCircle, 1, 12, -1)

    def testUpdateColour(self):
        self.assertEqual(self.repository.updateColour(1, 2, "magenta"), [n.MyPoint(1, 2, "magenta"), n.MyPoint(2, 3, "green"),
                            n.MyPoint(3, 4, "blue"), n.MyPoint(5, 6, "yellow"), n.MyPoint(6, 7, "magenta"), n.MyPoint(10, 11, "red"),
                            n.MyPoint(10, 12, "blue"), n.MyPoint(15, 16, "green"), n.MyPoint(20, 21, "red"), n.MyPoint(-10, -1, "magenta")])
        self.assertEqual(self.repository.updateColour(2, 3, "blue"), [n.MyPoint(1, 2, "magenta"), n.MyPoint(2, 3, "blue"),
                            n.MyPoint(3, 4, "blue"), n.MyPoint(5, 6, "yellow"), n.MyPoint(6, 7, "magenta"), n.MyPoint(10, 11, "red"),
                            n.MyPoint(10, 12, "blue"), n.MyPoint(15, 16, "green"), n.MyPoint(20, 21, "red"), n.MyPoint(-10, -1, "magenta")])
        self.assertRaises(ValueError, self.repository.updateColour, 1, 2, "pink")

    def testDeletePointsByCoordinates(self):
        self.assertEqual(self.repository.deletePointByCoordinates(1, 2), [n.MyPoint(2, 3, "green"),
                              n.MyPoint(3, 4, "blue"), n.MyPoint(5, 6, "yellow"), n.MyPoint(6, 7, "magenta"), n.MyPoint(10, 11, "red"),
                              n.MyPoint(10, 12, "blue"), n.MyPoint(15, 16, "green"), n.MyPoint(20, 21, "red"), n.MyPoint(-10, -1, "magenta")])
        self.assertEqual(self.repository.deletePointByCoordinates(-10, -1), [n.MyPoint(2, 3, "green"),
                              n.MyPoint(3, 4, "blue"), n.MyPoint(5, 6, "yellow"), n.MyPoint(6, 7, "magenta"), n.MyPoint(10, 11, "red"),
                              n.MyPoint(10, 12, "blue"), n.MyPoint(15, 16, "green"), n.MyPoint(20, 21, "red")])
        self.assertRaises(IndexError, self.repository.deletePointByCoordinates, 1, 1)
