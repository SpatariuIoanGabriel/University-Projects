from infrastructure.repositories import *
from domain.person import Patient


def dataExamples():
    """
    Return data examples.
    :return:
    """
    repo = Hospital([Department("dep1", "dis1", 13, [Patient("Andrei", "Pop", "5020714225890", "cancer"),
                                             Patient("David", "Maria", "5020714225891", "covid"),
                                             Patient("Alex", "Stefan", "5020714225892", "tuberculosis")]),
                     Department("dep2", "dis2", 10,  [Patient("Marin", "Chad", "5020714225893", "covid"),
                                             Patient("Raul", "Marc", "5020714225894", "covid"),
                                             Patient("Paul", "Apostol", "5020714225895", "covid"),
                                             Patient("Tudor", "Lung", "5020714225896", "sida"),
                                             Patient("Anca", "Serban", "5020714225897", "flu")]),
                     Department("dep3", "dis3", 20, [Patient("Nicu", "Alb", "5020714225898", "cancer"),
                                             Patient("Eugenia", "Nour", "5020714225899", "covid"),
                                             Patient("Sandra", "Dinu", "5020714225805", "covid"),
                                             Patient("Costel", "Virgil", "5020714225815", "malaria"),
                                             Patient("Stefan", "Mircea", "5020714225825", "covid"),
                                             Patient("Anton", "Baltazar", "5020714225835", "hypertension"),
                                             Patient("Cristi", "Chin", "5020714225845", "cancer")]),
                     Department("dep4", "dis4", 5, [Patient("Marcel", "Nica", "5020214225855", "parkinson"),
                                            Patient("Brian", "Maier", "5020114225865", "covid")])])
    print(repo)

    print("\nIteration 1.0:")
    print("ex. 1.")
    print("Add a department to the repository:")
    print("\nAdd a new department: Department(\"dep6\", \"dis11\", 20, [Patient(\"Eugenia\", \"New\", \"5020614221899\", \"covid\")]")
    print(repo.addDepartment("dep6", "dis11", 20, [Patient("Eugenia", "New", "5020614221899", "covid")]))
    try:
        repo.addDepartment("dep6", "dis11", 20, [Patient("Eugenia", "New", "5020614221899", "covid")])
    except ValueError as ve:
        print(ve)
    print("\nAdd a new department: Department(\"dep9\", \"dis12\", 20, [Patient(\"Mircea\", \"Nell\", \"5020714921899\", \"flu\")]")
    print(repo.addDepartment("dep9", "dis12", 20, [Patient("Mircea", "Nell", "5020714921899", "flu")]))

    print("ex. 2.")
    print("Get a department at a given index.")
    print("\nGet the department at index -3:")
    try:
        repo.getDepartmentByIndex(-3)
    except IndexError as ie:
        print(ie)
    print(f"\nThe department at index 0 is {repo.getDepartmentByIndex(0)}")
    print(f"\nThe department at index 1 is {repo.getDepartmentByIndex(1)}")
    print("\nex. 3.")
    print("Update a department at a given index.")
    print("\nUpdate the department at index 5.")
    id_ = "dep21"
    name = "dis01"
    number_of_beds = 11
    list_of_patients = [Patient("Mircea", "Nell", "4090714921899", "flu")]
    print(f"The list with the updated vector is: {repo.updateDepartmentByIndex(5, id_, name, number_of_beds, list_of_patients)}")
    id_ = "dep11"
    name = "dis02"
    number_of_beds = 10
    list_of_patients = [Patient("Michael", "Nell", "2010714921899", "flu")]
    print("\nUpdate the department at index -10.")
    try:
        repo.updateDepartmentByIndex(-10, id_, name, number_of_beds, list_of_patients)
    except IndexError as ie:
        print(ie)
    print("\nUpdate the department at index 5.")
    id_ = "dep18"
    name = "dis03"
    number_of_beds = 20
    list_of_patients = [Patient("Michael", "Larson", "3010714421899", "flu")]
    print(f"The list with the updated vector is: {repo.updateDepartmentByIndex(5, id_, name, number_of_beds, list_of_patients)}")

    print("\nex. 4.")
    print("Delete a department by index.")
    print("\nDelete the department at index -3:")
    try:
        repo.deleteDepartmentAtIndex(-3)
    except IndexError as ie:
        print(ie)
    print(f"\nThe list after deleting the department at index 0 is {repo.deleteDepartmentAtIndex(0)}")
    print(f"\nThe list after deleting the department at index 1 is {repo.deleteDepartmentAtIndex(1)}")

    print("ex. 5.")
    print("Get a department at a given index.")
    print("\nGet the department at index -3:")
    try:
        repo.getDepartmentByIndex(-3)
    except IndexError as ie:
        print(ie)
    print(f"\nThe department at index 0 is {repo.getDepartmentByIndex(0)}")
    print(f"\nThe department at index 1 is {repo.getDepartmentByIndex(1)}")
    print("\nex. 6.")
    print("Update a department at a given index.")
    print("\nUpdate the department at index 5.")
    id_ = "dep21"
    name = "dis01"
    number_of_beds = 11
    list_of_patients = [Patient("Mircea", "Nell", "4090714921899", "flu")]
    try:
        repo.updateDepartmentByIndex(-10, id_, name, number_of_beds, list_of_patients)
    except IndexError as ie:
        print(ie)
    print("ex. 5.")
    print("Get a department at a given index.")
    print("\nGet the department at index -3:")
    try:
        repo.getDepartmentByIndex(-3)
    except IndexError as ie:
        print(ie)
    print(f"\nThe department at index 0 is {repo.getDepartmentByIndex(0)}")
    print(f"\nThe department at index 1 is {repo.getDepartmentByIndex(1)}")
    print("\nex. 6.")
    print("Update a department at a given index.")
    print("\nUpdate the department at index 5.")
    id_ = "dep21"
    name = "dis01"
    number_of_beds = 11
    list_of_patients = [Patient("Mircea", "Nell", "4090714921899", "flu")]
    try:
        repo.updateDepartmentByIndex(-10, id_, name, number_of_beds, list_of_patients)
    except IndexError as ie:
        print(ie)
    print("ex. 5.")
    print("Get a department at a given index.")
    print("\nGet the department at index -3:")
    try:
        repo.getDepartmentByIndex(-3)
    except IndexError as ie:
        print(ie)
    print(f"\nThe department at index 0 is {repo.getDepartmentByIndex(0)}")
    print(f"\nThe department at index 1 is {repo.getDepartmentByIndex(1)}")
    print("\nex. 6.")
    print("Update a department at a given index.")
    print("\nUpdate the department at index 5.")
    id_ = "dep21"
    name = "dis01"
    number_of_beds = 11
    list_of_patients = [Patient("Mircea", "Nell", "4090714921899", "flu")]
    try:
        repo.updateDepartmentByIndex(-10, id_, name, number_of_beds, list_of_patients)
    except IndexError as ie:
        print(ie)
    print("\nex. 7.")
    print("Delete a department by index.")
    print("\nDelete the department at index -3:")
    try:
        repo.deleteDepartmentAtIndex(-3)
    except IndexError as ie:
        print(ie)
    print(f"\nThe list after deleting the department at index 0 is {repo.deleteDepartmentAtIndex(0)}")
    print(f"\nThe list after deleting the department at index 1 is {repo.deleteDepartmentAtIndex(1)}")
    print("\nex. 8.")
    print("sort")
    print(repo.sort_departments_by_number_of_patients())
    print("\nex. 9.")
    print(repo)
    print(repo.sort_by_age(30))
    print(repo)
    print(repo.sort_departments_by_patients_and_name())
    print(repo)
    print(repo.department_under_age(50))
    print(repo.get_patients_with_string_name2(1, "r"))


dataExamples()