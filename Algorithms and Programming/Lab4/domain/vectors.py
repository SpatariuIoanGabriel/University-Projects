import matplotlib.pyplot as plt
import utils.helpers as h
import numpy as np


class MyVector:
    def __init__(self, name_id, colour, vector_type, values):
        """
        Create a vector object with name_id, colour, vector_type and values.
        :param name_id: name_id
        :param colour: colour
        :param vector_type: vector_type
        :param values: values
        """
        self.__name_id = name_id
        if h.checkColour(colour):
            self.__colour = colour
        else:
            raise ValueError("The colour is not in the list!")
        if h.checkType(vector_type):
            self.__vector_type = vector_type
        else:
            raise TypeError("The vector type is not correct!")
        if h.checkValue(values):
            self.__values = np.array(values)
        else:
            raise ValueError("The value is not correct!")

    @property
    def name_id(self):
        """
        Get the name_if of the vector.
        :return: The name_id
        """
        return self.__name_id

    @property
    def colour(self):
        """
        Get the colour of the vector.
        :return: The colour
        """
        return self.__colour

    @property
    def vector_type(self):
        """
        Get the vector_type of the vector.
        :return: The vector_type
        """
        return self.__vector_type

    @property
    def values(self):
        """
        Get the values of the vector
        :return: values
        """
        return self.__values[:]

    @name_id.setter
    def name_id(self, new_name_id):
        """
        Set the name_id of the vector.
        :param new_name_id: new_name_id
        :return: The new_name_id
        """
        self.__name_id = new_name_id

    @colour.setter
    def colour(self, new_colour):
        """
        Set the colour of the vector.
        :param new_colour: colour
        :return:The new_colour
        """
        if h.checkColour(new_colour):
            self.__colour = new_colour
        else:
            raise ValueError("The colour is not in the list!")

    @vector_type.setter
    def vector_type(self, new_vector_type):
        """
        Set the vector_type of the vector.
        :param new_vector_type: new_vector_type
        :return: The new_vector_type
        """
        if h.checkType(new_vector_type):
            self.__vector_type = new_vector_type
        else:
            raise ValueError("The vector type is not correct!")

    @values.setter
    def values(self, new_values):
        """
        Set the values of the vector.
        :param new_values: new_values
        :return: The new_values
        """
        if h.checkValue(new_values):
            self.__values = np.array(new_values)
        else:
            raise ValueError("The value is not correct!")

    def add_scalar(self, scalar):
        """
        ex. 1.
        Scalar operations:
        a) Add a scalar to a vector:
        :param scalar: scalar
        :return: The new_vector
        """
        if type(scalar) == int or type(scalar) == float:
            for i in range(0, len(self.__values)):
                self.__values[i] += scalar
        else:
            raise ValueError("The scalar is not a number!")
        return self.__values

    def add_two_vectors(self, other):
        """
        ex. 2.
        Vector operations:
        a) Add two vectors:
        :param other: other vector
        :return: The sum of two vectors
        """
        if len(self.__values) == len(other.__values):
            return np.add(self.__values, other.__values)
        else:
            raise ValueError("The lengths should be the same!")

    def subtract(self, other):
        """
        ex 2.
        Vector operations:
        b) Subtract two vectors:
        :param other: other vector
        :return: The result
        """
        if len(self.__values) == len(other.__values):
            return np.subtract(self.__values, other.__values)
        else:
            raise ValueError("The lengths should be the same!")

    def multiplication(self, other):
        """
        ex. 2.
        Vector operations:
        c) Multiplication:
        :param other: other vector
        :return: The dot product of the two vectors
        """
        if len(self.__values) == len(other.__values):
            return np.dot(self.__values, other.__values)
        else:
            raise ValueError("The lengths should be the same!")

    def sum_of_values(self):
        """
        ex. 3.
        Reduction operations:
        a) Sum of elements in a vector:
        :return: The sum
        """
        if len(self.__values) > 0:
            return np.sum(self.__values)
        else:
            raise ValueError("The list is empty!")

    def product_of_elements(self):
        """
        ex. 3.
        Reduction operations:
        b) Product of elements in a vector:
        :return: The product
        """
        if len(self.__values) > 0:
            return np.product(self.__values)
        else:
            raise ValueError("The list is empty!")

    def average_of_elements(self):
        """
        ex. 3.
        Reduction operations:
        c) Average of elements in a vector:
        :return: The average
        """
        if len(self.__values) > 0:
            return np.average(self.__values)
        else:
            raise ValueError("The list is empty!")

    def min_of_vector(self):
        """
        ex. 3.
        Reduction operations:
        d) Minimum of a vector
        :return: The minimum element inside a given vector
        """
        if len(self.__values) > 0:
            return np.min(self.values)
        else:
            raise ValueError("The list is empty!")

    def max_of_vector(self):
        """
        ex. 3.
        Reduction operations:
        e) Maximum of a vector
        :return: The maximum element inside a given vector
        """
        if len(self.__values) > 0:
            return np.max(self.values)
        else:
            raise ValueError("The list is empty!")

    def __repr__(self):
        """
        Return the string representation of the vector.
        :return: The string representation of the point
        """
        return f"Vector({self.__name_id}, {self.__colour}, {self.__vector_type}, {self.__values})"

    def __str__(self):
        """
        Function called when converting object into string.
        :return:
        """
        return self.__repr__()

    def __eq__(self, other):
        """
        Check if two vectors objects are equal by comparing their properties.
        :param other: other
        :return:
        """
        return self.__name_id == other.__name_id and self.__colour == other.__colour and self.__vector_type == other.__vector_type and self.__values == other.__values


class VectorRepository:
    def __init__(self, initialVectors=None):
        """
        Creating a repository containing vectors.
        """
        self.__list_of_vectors = []
        if initialVectors is not None:
            # Check if the name_ids are unique
            for vector in initialVectors:
                if isinstance(vector, MyVector) and self.__isNameIdUnique(vector.name_id):
                    self.__list_of_vectors.append(vector)
                else:
                    raise ValueError("Vector is not correct!")

    def __isNameIdUnique(self, name_id):
        """
        Check if the given name_id is already in the list.
        :param name_id: name_id
        :return:
        """
        for vector in self.__list_of_vectors:
            if vector.name_id == name_id:
                return False
        return True

    def addVector(self, name_id, colour, vector_type, values):
        """
        ex. 1.
        Add a vector to the repository.
        :param name_id: name_id
        :param colour: colour
        :param vector_type: type
        :param values: values
        :return: The list
        """
        if self.__isNameIdUnique(name_id):
            if h.checkValue(values):
                self.__list_of_vectors.append(MyVector(name_id, colour, vector_type, values))
            else:
                raise ValueError("This value is not a number!")
        else:
            raise ValueError("NameId already exists in our repository!")
        return self.__list_of_vectors[:]

    def getAllVectors(self):
        """
        ex. 2.
        Get all vectors.
        :return: The list
        """
        return self.__list_of_vectors[:]

    def getAtIndex(self, index):
        """
        ex. 3.
        Get a vector at a given index.
        :param index: index
        :return: The vector
        """
        if 0 <= index < len(self.__list_of_vectors):
            return self.__list_of_vectors[index]
        else:
            raise IndexError("Index is not correct!")

    def updateVectorAtIndex(self, index, new_name_id, new_colour, new_vector_type, new_values):
        """
        ex. 4.
        Update a vector at a given index.
        :param index: index
        :param new_name_id: new_name_id
        :param new_colour: new_colour
        :param new_vector_type: new_vector_type
        :param new_values: new_values
        :return: The list with the new vector.
        """
        if 0 <= index < len(self.__list_of_vectors):
            vector = self.getAtIndex(index)
            if self.__isNameIdUnique(new_name_id):
                vector.name_id = new_name_id
                vector.colour = new_colour
                vector.vector_type = new_vector_type
                vector.values = new_values
            else:
                raise ValueError("NameId already exists in our repository!")
        else:
            raise IndexError("Index is not correct!")
        return self.__list_of_vectors[:]

    def getIndexByNameID(self, name_id):
        """
        Get the index of a vector by name_id.
        :param name_id: name_id
        :return: The index
        """
        for index, v in enumerate(self.__list_of_vectors):
            if v.name_id == name_id:
                return index
        return -1

    def updateByNameID(self, name_id, new_name, new_colour, new_vector_type, new_values):
        """
        ex. 5.
        Update a vector identified by name_id.
        :param name_id: name_id
        :param new_name: new_name
        :param new_colour: new_colour
        :param new_vector_type: new_vector_type
        :param new_values: new_values
        :return: The list with the new vector.
        """
        index = self.getIndexByNameID(name_id)
        if 0 <= index < len(self.__list_of_vectors):
            self.updateVectorAtIndex(index, new_name, new_colour, new_vector_type, new_values)
        else:
            raise IndexError("There is no point with this name_id!")
        return self.__list_of_vectors[:]

    def deleteVectorAtIndex(self, index):
        """
        ex. 6.
        Delete a vector by index.
        :param index: index
        :return: The list
        """
        if 0 <= index < len(self.__list_of_vectors):
            del self.__list_of_vectors[index]
        else:
            raise IndexError("Index is not correct!")
        return self.__list_of_vectors[:]

    def deleteVectorByNameId(self, name_id):
        """
        ex. 7.
        Delete a vector by name_id.
        :param name_id: name_id
        :return: The list
        """
        index = self.getIndexByNameID(name_id)
        if 0 <= index < len(self.__list_of_vectors):
            self.deleteVectorAtIndex(index)
        else:
            raise IndexError("There is no point with these coordinates!")
        return self.__list_of_vectors[:]

    def plotAllVectors(self):
        """
        ex. 8.
        Plot all vectors in a chart.
        :return:
        """
        for vector in self.__list_of_vectors:
            vector_type = vector.vector_type
            vector_colour = vector.colour
            vector_values = vector.values
            vector_indices = []
            for _ in range(len(vector_values)):
                vector_indices.append(_)
            if vector_type == 1:
                m = "o"
            elif vector_type == 2:
                m = "s"
            elif vector_type == 3:
                m = "^"
            else:
                m = "d"
            plt.scatter(vector_indices, vector_values, s=20, c=vector_colour, marker=m)
        plt.show()

    def __repr__(self):
        """
        Return the string representation of the class
        """
        if len(self.__list_of_vectors) == 0:
            return "There are no points!"
        else:
            str_repr = ""
            for vector in self.__list_of_vectors:
                str_repr += str(vector) + "\n"
            return str_repr

    def __eq__(self, other):
        """
        Check if two vectors objects are equal by comparing their properties.
        :param other: other
        :return:
        """
        index = 0
        while index < len(self.__list_of_vectors):
            if self.__list_of_vectors[index] != other.__list_of_points[index]:
                return False
            index += 1
        return True
