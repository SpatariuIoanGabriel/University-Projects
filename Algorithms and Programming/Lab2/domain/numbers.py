# Problem 1


# Exercise 1


def add(my_list, value):
    """
    ex. 1.
    Add value as last element of my list
    :param my_list: my list
    :param value: value
    :return: add a value to the end of the list
    """

    my_list.append(value)
    return my_list


def insert(my_list, index, value):
    """
    ex. 2.
    Insert number value at index
    :param my_list: my list
    :param index: index
    :param value: value
    :return: insert number value at index
    """
    if index > len(my_list):
        raise ValueError("The index is not valid!")
    else:
        my_list.insert(index, value)
    return my_list


# Exercise 2


def remove(my_list, index):
    """
    ex. 3.
    Remove the element at index
    :param my_list: my list
    :param index: index
    :return: remove the element at index
    """
    if index > len(my_list):
        raise ValueError("The index is not valid!")
    else:
        del my_list[index]
    return my_list


def remove_interval(my_list, from_index, to_index):
    """
    ex. 4.
    Remove elements between the two given index
    :param my_list: my list
    :param from_index: from index
    :param to_index: to index
    :return: remove the elements between the two given index
    """
    if from_index > len(my_list) or to_index > len(my_list):
        raise ValueError("The index is not valid!")
    else:
        del my_list[from_index:to_index + 1]
    return my_list


def replace(my_list, old_value, new_value):
    """
    ex. 5.
    Replace all old_values occurrences with new_value
    :param my_list: my list
    :param old_value: old value
    :param new_value: new value
    :return: replace old_value with new_value
    """

    if len(my_list) == 0:
        raise ValueError("The list has no values!")
    else:
        for i in range(0, len(my_list) - len(old_value)):
            if my_list[i:i + len(old_value)] == old_value:
                my_list[i:i + len(old_value)] = new_value
    return my_list


# Exercise 3


def isPrime(value):
    is_prime = 0
    if value < 2:
        is_prime = 1
        return is_prime
    elif value == 2:
        is_prime = 0
        return is_prime
    else:
        for i in range(2, value):
            if value % i == 0:
                is_prime = 1
                return is_prime
    return is_prime


def prime(my_list, from_index, to_index):
    """
    ex. 6.
    Get the prime numbers between the two given index
    :param my_list: my list
    :param from_index: from index
    :param to_index: to index
    :return: get the prime numbers between the two given index
    """

    new_array = []
    if from_index > len(my_list) or to_index > len(my_list):
        raise ValueError("The index is not valid!")
    else:
        for i in range(from_index, to_index):
            if isPrime(my_list[i]) % 2 == 0:
                new_array.append(my_list[i])
    return new_array


def odd(my_list, from_index, to_index):
    """
    ex. 7.
    Get the odd numbers between the two given index
    :param my_list: my list
    :param from_index: from index
    :param to_index: to index
    :return: get the odd numbers between the two given index
    """

    new_array = []
    if from_index > len(my_list) or to_index > len(my_list):
        raise ValueError("The index is not valid!")
    else:
        for i in range(from_index, to_index + 1):
            if my_list[i] % 2 == 1:
                new_array.append(my_list[i])
    return new_array


def sequence_sum(my_list, from_index, to_index):
    """
    ex. 8.
    Get the sum of elements between the two given index
    :param my_list: my list
    :param from_index: from index
    :param to_index: to index
    :return: get the sum of elements between the two given index
    """
    theSum = 0
    if from_index > len(my_list) or to_index > len(my_list):
        raise ValueError("The index is not valid!")
    else:
        for i in range(from_index, to_index + 1):
            theSum += my_list[i]
    return theSum


def gcd(my_list, from_index, to_index):
    """
    ex. 9.
    Get the greatest common divisor of the elements between two given index
    :param my_list: my list
    :param from_index: starting index
    :param to_index: final index
    :return: the greatest common divisor of the elements between two given index
    """

    if from_index > len(my_list) or to_index > len(my_list):
        raise ValueError("The index is not valid!")
    else:
        a = int(my_list[from_index])
        for i in range(from_index, to_index + 1):
            b = int(my_list[i])
            while b != 0:
                c = a % b
                a = b
                b = c
    return a


def sequence_max(my_list, from_index, to_index):
    """
    ex. 10.
    Get the maximum of elements between the two given index
    :param my_list: my_list
    :param from_index: from index
    :param to_index: to index
    :return: get the maximum of elements between the two given index
    """

    MAX = 0
    if from_index > len(my_list) or to_index > len(my_list):
        raise ValueError("The index is not valid!")
    else:
        for i in range(from_index, to_index + 1):
            if my_list[i] > MAX:
                MAX = my_list[i]
    return MAX


# Exercise 5


def filter_prime(my_list):
    """
    ex. 11.
    Keep only prime numbers, remove the other elements
    :param my_list: my list
    :return: the list of prime numbers
    """
    i = 0
    while i < len(my_list):
        if isPrime(my_list[i]) % 2 == 1:
            my_list.pop(i)
        else:
            i = i + 1
    return my_list


def filter_negative(my_list):
    """
    ex. 12.
    Keep only negative numbers, remove the other elements
    :param my_list: my list
    :return: the list of negative numbers
    """

    i = 0
    while i < len(my_list):
        if my_list[i] >= 0:
            my_list.pop(i)
        else:
            i = i + 1
    return my_list


# Exercise 6


def undo(my_list, before_list):
    """
    ex. 13.
    Undo the last operation that modified the array
    :param my_list:my list
    :param before_list: before list
    :return: undo the last operation that modified the array
    """
    my_list[:] = before_list[:]
    return my_list
