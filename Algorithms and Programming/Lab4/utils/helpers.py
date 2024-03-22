possible_colours = ['r', 'g', 'b', 'y', 'm']


def checkColour(colour):
    """
    Check if the colour is in the list of possible colours.
    :param colour: colour
    :return:
    """
    if colour in possible_colours:
        return True
    else:
        raise ValueError("The colour is not in the list!")


def checkType(vector_type):
    """
    Check if the vector_type is an integer greater or equal to 1.
    :param vector_type: vector_type
    :return:
    """
    if type(vector_type) is int:
        return vector_type >= 1
    else:
        raise TypeError("The vector_type is not correct!")


def checkValue(values):
    """
    Check if the value is a number.
    :param values: value
    :return:
    """
    for value in values:
        if type(value) is int or type(value) is float:
            return True
        else:
            raise ValueError("This value is not a number!")
