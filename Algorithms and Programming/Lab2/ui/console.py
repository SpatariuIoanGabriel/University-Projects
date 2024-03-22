from domain import numbers
from my_tests.numbers_test import runAllTests


def printMenu():
    print("MENU:")
    print("-2 - print data examples")
    print("-1 - print menu")
    print(" 0 - exit program")
    print(" 1 - add a new number")
    print(" 2 - insert a new value")
    print(" 3 - remove the element at index")
    print(" 4 - remove elements between two given index")
    print(" 5 - replace all all old_values occurrence with new_values")
    print(" 6 - get the prime numbers between two given index")
    print(" 7 - get the odd numbers between two given index")
    print(" 8 - get the sum of elements between two given index")
    print(" 9 - get the greatest common divisor of elements")
    print(" 10 - get maximum of elements between the two given index")
    print(" 11 - keep only prime numbers, remove the others")
    print(" 12 - keep only negatives numbers, remove the others")
    print(" 13 - undo the last operation that modified the array")


def dataExamples():
    listOfNumbers = [2, 5, 14, 7, 81, 94, 21, 77, 147, 56]
    print(listOfNumbers)

    print("ex. 1.")
    numbers.add(listOfNumbers, 91)
    print(listOfNumbers)
    numbers.add(listOfNumbers, 140)
    print(listOfNumbers)

    print("ex. 2.")
    numbers.insert(listOfNumbers, 3, 63)
    print(listOfNumbers)
    numbers.insert(listOfNumbers, 1, 49)
    print(listOfNumbers)

    print("ex. 3.")
    numbers.remove(listOfNumbers, 1)
    print(listOfNumbers)
    numbers.remove(listOfNumbers, 2)
    print(listOfNumbers)

    print("ex. 4.")
    numbers.remove_interval(listOfNumbers, 1, 3)
    print(listOfNumbers)
    numbers.remove_interval(listOfNumbers, 0, 1)
    print(listOfNumbers)

    print("ex. 5.")
    numbers.replace(listOfNumbers, [94, 21], [28, 35])
    print(listOfNumbers)
    numbers.replace(listOfNumbers, [28, 35], [2, 7])
    print(listOfNumbers)

    print("ex. 6.")
    numbers.prime(listOfNumbers, 0, 5)
    print(listOfNumbers)
    numbers.prime(listOfNumbers, 0, 1)
    print(listOfNumbers)

    print("ex. 7.")
    numbers.odd(listOfNumbers, 0, 5)
    print(listOfNumbers)
    numbers.odd(listOfNumbers, 0, 1)
    print(listOfNumbers)

    print("ex. 8.")
    numbers.sequence_sum(listOfNumbers, 0, 2)
    print(listOfNumbers)
    numbers.sequence_sum(listOfNumbers, 0, 5)
    print(listOfNumbers)

    print("ex. 9.")
    numbers.gcd(listOfNumbers, 0, 1)
    print(listOfNumbers)
    numbers.gcd(listOfNumbers, 0, 4)
    print(listOfNumbers)

    print("ex. 10.")
    numbers.sequence_max(listOfNumbers, 1, 4)
    print(listOfNumbers)
    numbers.sequence_max(listOfNumbers, 0, 3)
    print(listOfNumbers)

    print("ex. 11.")
    numbers.filter_prime(listOfNumbers)
    print(listOfNumbers)

    print("ex. 12.")
    numbers.filter_negative(listOfNumbers)
    print(listOfNumbers)

    print("ex. 13.")
    numbers.undo(listOfNumbers, [2, 7])
    print(listOfNumbers)


the_precedent_list = []
theList = [int(number) for number in input("Enter the numbers from the list:").split()]


def start():
    runAllTests()
    print("All tests run successfully!")
    printMenu()
    command = None
    while command != 0:
        command = int(input(">>>"))
        if command == -2:
            dataExamples()
        elif command == -1:
            printMenu()
        elif command == 0:
            print("program ended")
        elif command == 1:
            the_precedent_list[:] = theList[:]
            value = int(input("Add a  new number in the list:"))
            numbers.add(theList, value)
            print(theList)
        elif command == 2:
            the_precedent_list[:] = theList[:]
            index = int(input("What is the index?"))
            try:
                if 0 <= index <= len(theList):
                    value = int(input("What is the value to insert?"))
                    numbers.insert(theList, index, value)
                    print(theList)
                else:
                    print("The index should be less than the length of the list!")
            except ValueError:
                print("The index should be less than than the length of the list!")
        elif command == 3:
            the_precedent_list[:] = theList[:]
            try:
                index = int(input("What is the index?"))
                if 0 <= index <= len(theList):
                    numbers.remove(theList, index)
                    print(theList)
                else:
                    print("The index should be less than the length of the list!")
            except ValueError:
                print("The index should be less than than the length of the list!")
        elif command == 4:
            the_precedent_list[:] = theList[:]
            try:
                from_index = int(input("What is the index to start from?"))
                to_index = int(input("What is the index to end with?"))
                if from_index < len(theList) or to_index <= len(theList):
                    numbers.remove_interval(theList, from_index, to_index)
                    print(theList)
                else:
                    print("The index should be less than the length of the list1")
            except ValueError:
                print("The index should be less than the length of the list!")
        elif command == 5:
            old_value = [int(number) for number in input("Value to replace:").split()]
            new_value = [int(number) for number in input("New value:").split()]
            numbers.replace(theList, old_value, new_value)
            print(theList)
        elif command == 6:
            the_precedent_list[:] = theList[:]
            try:
                from_index = int(input("What is the index to start from?"))
                to_index = int(input("What is the index to end with?"))
                if from_index < len(theList) or to_index <= len(theList):
                    print(numbers.prime(theList, from_index, to_index))
                    print(theList)
                else:
                    print("The index should be less than the length of the list!")
            except ValueError:
                print("The index should be less than the length of the list1")
        elif command == 7:
            the_precedent_list[:] = theList[:]
            try:
                from_index = int(input("What is the index to start from?"))
                to_index = int(input("What is the index to end with?"))
                if from_index < len(theList) or to_index <= len(theList):
                    print(numbers.odd(theList, from_index, to_index))
                    print(theList)
                else:
                    print("The index should be less than the length of the list!")
            except ValueError:
                print("The index should be less than the length of the list!")
        elif command == 8:
            the_precedent_list[:] = theList[:]
            try:
                from_index = int(input("What is the index to start from?"))
                to_index = int(input("What is the index to end with?"))
                if from_index < len(theList) or to_index <= len(theList):
                    print(numbers.sequence_sum(theList, from_index, to_index))
                    print(theList)
                else:
                    print("The index should be less than the length of the list!")
            except ValueError:
                print("The index should be less than the length of the list!")
        elif command == 9:
            the_precedent_list[:] = theList[:]
            try:
                from_index = int(input("What is the index to start from?"))
                to_index = int(input("What is the index to end with?"))
                if from_index < len(theList) or to_index <= len(theList):
                    print(numbers.gcd(theList, from_index, to_index))
                    print(theList)
                else:
                    print("The index should be less than the length of the list!")
            except ValueError:
                print("The index should be less than the length of the list!")
        elif command == 10:
            the_precedent_list[:] = theList[:]
            try:
                from_index = int(input("What is the index to start from?"))
                to_index = int(input("What is the index to end with?"))
                if from_index < len(theList) or to_index <= len(theList):
                    print(numbers.sequence_max(theList, from_index, to_index))
                    print(theList)
                else:
                    print("The index should be less than the length of the list!")
            except ValueError:
                print("The index should be less than the length of the list!")
        elif command == 11:
            the_precedent_list[:] = theList[:]
            numbers.filter_prime(theList)
            print(theList)
        elif command == 12:
            the_precedent_list[:] = theList[:]
            numbers.filter_negative(theList)
            print(theList)
        elif command == 13:
            numbers.undo(theList, the_precedent_list)
            print(theList)
        else:
            print("Invalid command")
