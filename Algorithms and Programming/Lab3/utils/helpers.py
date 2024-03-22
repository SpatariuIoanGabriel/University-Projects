possible_colours = ["red", "green", "blue", "yellow", "magenta"]


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


def distanceBetweenTwoPoints(firstPoint, secondPoint):
    """
    Finds the distance between two points using a mathematical formula
    :return: The distance between two points
    """
    distance = ((secondPoint.coord_x - firstPoint.coord_x) ** 2 + (secondPoint.coord_y - firstPoint.coord_y) ** 2) ** (1/2)
    return distance
