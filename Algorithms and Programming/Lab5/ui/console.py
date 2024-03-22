from data_examples import dataExamples
from application.controller import Controller


def printMenu():
    print("MENU:")
    print("-2 - Print data examples")
    print("-1 - Print menu")
    print(" 0 - Exit program")
    print("1 - Sort the patients in a department by personal numerical code")
    print("2 - Sort departments by the number of patients")
    print("3 - Sort departments by the number of patients having the age above a given limit")
    print("4 - Sort departments by the number of patients and the patients in a department alphabetically")
    print("5 - Identify departments where there are patients under a given age")
    print("6 - Identify patients from a given department for which the first name or last name contain a given string")
    print("7 - Identify department/departments where there are patients with a given first name")
    print("8 - Form groups of k patients from the same department and the same disease")
    print("9 - Form groups of k departments having at most p patients suffering from the same disease")


def start(controller: Controller):
    print()
    printMenu()
    command = None
    while command != 0:
        try:
            command = int(input(">>> "))
            if command == -2:
                print(dataExamples())
            elif command == -1:
                printMenu()
            elif command == 0:
                print("Program ended!")
            if command == 1:
                department_id = input("Enter the name id of department: ")
                try:
                    print(controller.sort_by_number_of_patients(department_id))
                except ValueError as ve:
                    print(ve)
            elif command == 2:
                try:
                    print(controller.sort_by_number_of_patients())
                except ValueError as ve:
                    print(ve)
            elif command == 3:
                age = int(input("Enter an age: "))
                try:
                    print(controller.sort_by_number_of_patients(age))
                except ValueError as ve:
                    print(ve)
            elif command == 4:
                try:
                    print(controller.sort_departments_by_patients_and_name())
                except ValueError as ve:
                    print(ve)
            elif command == 5:
                age = int(input("Enter an age: "))
                try:
                    print(controller.department_under_age(age))
                except ValueError as ve:
                    print(ve)
            elif command == 6:
                index = int(input("Enter an index of an department: "))
                string = input("Enter a string: ")
                try:
                    print(controller.getAtIndex(index, string))
                except IndexError as ie:
                    print(ie)
            elif command == 7:
                first_name = input("Enter the first name: ")
                try:
                    print(controller.departments_with_patients_name(first_name))
                except ValueError as ve:
                    print(ve)
            elif command == 8:
                k = int(input("Enter a k: "))
                try:
                    print(controller.groups_of_k_with_same_disease(k))
                except ValueError as ve:
                    print(ve)
            elif command == 9:
                k = int(input("Enter a k: "))
                p = int(input("Enter a p: "))
                try:
                    print(controller.groups_of_k_with_p_patients(k, p))
                except ValueError as ve:
                    print(ve)
            else:
                print("Invalid command")
        except ValueError:
            print("Invalid type entered!")
