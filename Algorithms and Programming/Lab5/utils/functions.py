def Filter(list_of_values, criterion):
    """
    Filter the elements of the list based on the given condition.
    :param list_of_values: list_of_values
    :param criterion: function having one parameter defining the condition of inclusion of a value in the result list
    :return: the filtered list
    """
    result = []
    for value in list_of_values:
        if criterion(value):
            result.append(value)
    return result


def sort(mylist, relation):
    """
    Sorts the elements from a list by a given relation.
    :param mylist: a list
    :param relation: a function
    :return: a list
    """
    for i in range(0, len(mylist) - 1):
        for j in range(i + 1, len(mylist)):
            if relation(mylist[i], mylist[j]):
                mylist[i], mylist[j] = mylist[j], mylist[i]
    return mylist


def init():
    """
    Initialize the next element of the solution.
    :returns: initial value of the last element of the solution
    """
    return -1


def nextElement(solution, position):
    """
    Get the next possible element of the solution.
    :param solution: list containing the solution
    :param position: position of the element for which the next element should be defined
    :returns: next possible element for the given position
    """
    return solution[position] + 1


def generateRecursiveSolutions(solution, initElementFn, nextElementFn, doesElementExistFn, isConsistentFn, isSolutionFn):
    """
    Generate solutions for a given program with recursive solution.
    :param solution: current state of the solution
    :param initElementFn: function to initialize the next element of the solution
    :param nextElementFn: gets the next value for the last element of the solution
    :param doesElementExistFn: checks if the value of the last element (of the solution) is correct
    :param isConsistentFn: checks if the current solution is consistent
    :param isSolutionFn: checks if the current content of the solution is a final solution
    :returns: a final solution
    """
    solution.append(init())
    # nextElement = nextElementFn(solution, len(solution) - 1)
    nextElementValue = nextElementFn(solution, -1)
    while doesElementExistFn(nextElementValue):
        solution[-1] = nextElementValue
        if isConsistentFn(solution):
            if isSolutionFn(solution):
                yield solution[:]
            else:
                yield from generateRecursiveSolutions(solution[:], initElementFn, nextElementFn, doesElementExistFn,
                                                      isConsistentFn, isSolutionFn)
        nextElementValue = nextElementFn(solution, -1)


def getSolutions(list_of_values, initElementFn=init, nextElementFn=nextElement, doesElementExistFn=lambda element: False,
                 isConsistentFn=lambda solution: False, isSolutionFn=lambda solution: False):
    fn = generateRecursiveSolutions
    args = [[]]
    return [list(map(lambda index: list_of_values[index], solution)) for solution in fn(*args, initElementFn, nextElementFn,
            doesElementExistFn, isConsistentFn, isSolutionFn)]
