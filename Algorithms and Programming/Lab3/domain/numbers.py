import matplotlib.pyplot as plt
import utils.helpers as h


class MyPoint:
    def __init__(self, coord_x, coord_y, colour):
        """
        Create a point object with coord_x, coord_y and colour.
        :param coord_x: coord_x
        :param coord_y: coord_y
        :param colour: colour
        """
        self.__coord_x = coord_x
        self.__coord_y = coord_y
        if h.checkColour(colour):
            self.__colour = colour
        else:
            raise ValueError("The colour is not in the list!")

    @property
    def coord_x(self):
        """
        Get the coord_x of the point.
        :return: The coord_x
        """
        return self.__coord_x

    @property
    def coord_y(self):
        """
        Get the coord_y of the point.
        :return: The coord_y
        """
        return self.__coord_y

    @property
    def colour(self):
        """
        Get the colour of the point.
        :return: The colour
        """
        return self.__colour

    @coord_x.setter
    def coord_x(self, new_coord_x):
        """
        Set the coord_x of the point.
        :param new_coord_x: new_coord_x
        :return: The new_coord_x
        """
        self.__coord_x = new_coord_x

    @coord_y.setter
    def coord_y(self, new_coord_y):
        """
        Set the coord_y of the point.
        :param new_coord_y: new_coord_y
        :return: The new_coord_y
        """
        self.__coord_y = new_coord_y

    @colour.setter
    def colour(self, new_colour):
        """
        Set the colour of the point.
        :param new_colour: new_colour
        :return: The new_colour
        """
        if h.checkColour(new_colour):
            self.__colour = new_colour
        else:
            raise ValueError("The colour is not in the list!")

    def __repr__(self):
        """
        Return the string representation of the point.
        :return: The string representation of the point
        """
        return f"Point({self.__coord_x}, {self.__coord_y}, {self.__colour})"

    def __str__(self):
        """
        Function called when converting object into string.
        :return:
        """
        return self.__repr__()

    def __eq__(self, other):
        """
        Check if two points objects are equal by comparing their properties.
        :param other: other
        :return:
        """
        return self.__coord_x == other.__coord_x and self.__coord_y == other.__coord_y and self.__colour == other.__colour


class PointRepository:
    def __init__(self, initialPoints=None):
        """
        Creating a repository containing points.
        """
        self.__list_of_points = []
        if initialPoints is not None:
            # Check if the point is already in our repository and if the point is unique
            for point in initialPoints:
                if isinstance(point, MyPoint) and self.__isPointUnique(point.coord_x, point.coord_y, point.colour):
                    self.__list_of_points.append(point)
                else:
                    raise ValueError("The point is not correct!")

    def __isPointUnique(self, coord_x, coord_y, new_colour):
        """
        Check if a point has only one colour.
        :param new_colour: new_colour
        :return:
        """
        if h.checkColour(new_colour):
            for point in self.__list_of_points:
                if point.coord_x == coord_x and point.coord_y == coord_y and point.colour != new_colour:
                    raise ValueError("A point can't have two colours!")
        else:
            raise ValueError("The colour is not in the list!")
        return True

    def addPoint(self, coord_x, coord_y, colour):
        """
        ex. 1.
        Add a new point to the repository.
        :param coord_x: The coord_x of the point
        :param coord_y: The coord_y of the point
        :param colour: The colour of our point
        :return: The new point
        """
        if not self.__isPointUnique(coord_x, coord_y, colour):
            raise ValueError("A point can't have two colour!")
        if not self.__isInList(coord_x, coord_y, colour):
            self.__list_of_points.append(MyPoint(coord_x, coord_y, colour))
        else:
            raise ValueError("The point is already in the list!")
        return self.__list_of_points[:]

    def getAllPoints(self):
        """
        ex. 2.
        Get all points.
        :return: The list
        """
        return self.__list_of_points[:]

    def getPointAtIndex(self, index):
        """
        ex. 3.
        Get a point at a given index.
        :return: The point at a given index
        """
        if 0 <= index < len(self.__list_of_points):
            return self.__list_of_points[index]
        else:
            raise IndexError("The index is not correct!")

    def getPointsOfGivenColour(self, colour):
        """
        ex. 4.
        Get all points of a given colour
        :param colour: The colour of the points we're searching for
        :return: A list of all points of given colour
        """
        new_array = []
        if h.checkColour(colour):
            for point in self.__list_of_points:
                if point.colour == colour:
                    new_array.append(point)
            return PointRepository(new_array)
        else:
            raise ValueError("The colour is not in the list!")

    def getPointsInsideSquare(self, corner_x, corner_y, length):
        """
        ex. 5.
        Get all points that are inside a given square.
        :param corner_x: The coord_x of the up-left corner of our square
        :param corner_y: The coord_y of the up-left corner of our square
        :param length: length
        :return: A list containing all the points inside our given square
        """
        selected_points = []
        for point in self.__list_of_points:
            if corner_x <= point.coord_x and corner_y >= point.coord_y and abs(corner_x) + length >= abs(point.coord_x) and abs(corner_y) - length <= abs(point.coord_y):
                selected_points.append(point)
        return PointRepository(selected_points)

    def minimumDistanceBetweenTwoPoints(self):
        """
        ex. 6.
        Get the minimum distance between two points
        :return: The minimum distance between two points
        """
        if len(self.__list_of_points) == 1:
            minimumDistance = 0
        elif len(self.__list_of_points) >= 2:
            minimumDistance = h.distanceBetweenTwoPoints(self.__list_of_points[0], self.__list_of_points[1])
            for i in range(0, len(self.__list_of_points) - 1):
                for j in range(i + 1, len(self.__list_of_points)):
                    if h.distanceBetweenTwoPoints(self.__list_of_points[i], self.__list_of_points[j]) < minimumDistance:
                        minimumDistance = h.distanceBetweenTwoPoints(self.__list_of_points[i], self.__list_of_points[j])
        else:
            raise ValueError("The list is empty!")
        return minimumDistance

    def updatePoint(self, index, new_coord_x, new_coord_y, new_colour):
        """
        ex. 7.
        Update a point at a given index.
        :param index: index
        :param new_coord_x: new_coord_x
        :param new_coord_y: new coord_y
        :param new_colour: new_colour
        :return: The new point
        """
        if 0 <= index < len(self.__list_of_points):
            point = self.getPointAtIndex(index)
            point.coord_x = new_coord_x
            point.coord_y = new_coord_y
            point.colour = new_colour
        else:
            raise IndexError("Index is not correct!")
        return self.__list_of_points[:]

    def deletePoint(self, index):
        """
        ex. 8.
        Delete a point by index
        :param index: index
        :return: The list of point with the point at given index removed
        """
        if 0 <= index < len(self.__list_of_points):
            del self.__list_of_points[index]
        else:
            raise IndexError("Index is not correct!")
        return self.__list_of_points[:]

    def deleteAllPointsInSquare(self, corner_x, corner_y, length):
        """
        ex. 9.
        Delete all points that are inside a given square
        :return:
        """
        _ = 0
        while _ < len(self.__list_of_points):
            if corner_x <= self.__list_of_points[_].coord_x and corner_y >= self.__list_of_points[_].coord_y and abs(corner_x) + length >= abs(self.__list_of_points[_].coord_x) and abs(corner_y) - length <= abs(self.__list_of_points[_].coord_y):
                del self.__list_of_points[_]
            else:
                _ += 1
        return PointRepository(self.__list_of_points)

    def plotAllPoints(self):
        """
        ex. 10.
        Plot all points in a chart.
        :return:
        """
        coord_x = []
        coord_y = []
        colour = []
        for point in self.__list_of_points:
            coord_x.append(point.coord_x)
        for point in self.__list_of_points:
            coord_y.append(point.coord_y)
        for point in self.__list_of_points:
            colour.append(point.colour)
        plt.scatter(coord_x, coord_y, c=colour)
        plt.show()

    def __isInList(self, coord_x, coord_y, colour):
        """
        This function verifies if a point is in a list based on its coordinates and colour
        :param coord_x: The coord_x coordinate of the point
        :param coord_y: The coord_y coordinate of the point
        :param colour: The colour of our point
        :return: True if the point already exists in our list or False in case it doesn't
        """
        if h.checkColour(colour):
            for point in self.__list_of_points:
                if point.colour == colour and point.coord_x == coord_x and point.coord_y == coord_y:
                    return True
        else:
            raise ValueError("The colour is not in the list!")

    def getAllPointsInsideCircle(self, circle_x, circle_y, rad):
        """
        ex. 11.
        Get all points that are inside a given circle.
        :param circle_x: coord x of the center of circle
        :param circle_y: coord y of the center of circle
        :param rad: radius of circle
        :return:
        """
        points_inside_circle = []
        for point in self.__list_of_points:
            if rad > 0:
                coord_x = point.coord_x
                coord_y = point.coord_y
                if (coord_x - circle_x) * (coord_x - circle_x) + (coord_y - circle_y) * (coord_y - circle_y) < rad * rad:
                    points_inside_circle.append(point)
            else:
                raise ValueError("Radius is not correct!")
        return PointRepository(points_inside_circle)

    def getIndexOfPoint(self, coord_x, coord_y):
        """
        Get the index of a point by its coordinates.
        :param coord_x: coord_x
        :param coord_y: coord_y
        :return:
        """
        for index, point in enumerate(self.__list_of_points):
            if point.coord_x == coord_x and point.coord_y == coord_y:
                return index
        return -1

    def updateAtIndex(self, index, new_colour):
        """
        Update a point by index.
        :param index: index
        :param new_colour: new_colour
        :return:
        """
        if 0 <= index < len(self.__list_of_points):
            point = self.getPointAtIndex(index)
            point.colour = new_colour
        else:
            raise IndexError("This point is not in the list!")

    def updateColour(self, coord_x, coord_y, new_colour):
        """
        ex. 15.
        Update the colour of a point given its coordinates.
        :param coord_x: coord x
        :param coord_y: coord y
        :param new_colour: new colour
        :return:
        """
        if h.checkColour(new_colour):
            self.updateAtIndex(self.getIndexOfPoint(coord_x, coord_y), new_colour)
        else:
            raise ValueError("The colour is not in the list!")
        return self.__list_of_points[:]

    def deletePointByCoordinates(self, given_coord_x, given_coord_y):
        """
        ex. 18.
        Delete a point by coordinates.
        :param given_coord_x: given coord x
        :param given_coord_y: given coord y
        :return:
        """
        index = self.getIndexOfPoint(given_coord_x, given_coord_y)
        if 0 <= index < len(self.__list_of_points):
            self.deletePoint(index)
        else:
            raise IndexError("There is no point with these coordinates!")
        return self.__list_of_points[:]

    def __repr__(self):
        """
        Return the string representation of the class
        """
        if len(self.__list_of_points) == 0:
            return "There are no points!"
        else:
            str_repr = ""
            for point in self.__list_of_points:
                str_repr += str(point) + "\n"
            return str_repr

    def __eq__(self, other):
        """
        Check if two points objects are equal by comparing their properties.
        :param other: other
        :return:
        """
        index = 0
        while index < len(self.__list_of_points):
            if self.__list_of_points[index] != other.__list_of_points[index]:
                return False
            index += 1
        return True
