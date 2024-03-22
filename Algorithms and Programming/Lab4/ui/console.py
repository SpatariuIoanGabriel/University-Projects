import domain.vectors as v


def dataExamples():
    v1 = v.MyVector("A", "r", 1, [1, 2, 3, 4, 5])
    v2 = v.MyVector("B", "b", 2, [5.1, 2.3, 2.28, 1.14, 1.8])
    v3 = v.MyVector("C", "y", 3, [4, 5, 6, 7, 8])
    v4 = v.MyVector("D", "m", 4, [7, 8, 9, 10, 11])
    v5 = v.MyVector("E", "y", 5, [5, 4, 3, 2, 1])
    v6 = v.MyVector("F", "r", 8, [1, 2, 3])

    print("Iteration 1:")
    print("\nex. 1. Scalar operations:")
    print("\na.")
    print("Add a scalar to a vector: scalar is 5, vector is v1:")
    print(v1.add_scalar(5))
    print("\nAdd a scalar to a vector: scalar is \"abc\", vector is v2:")
    try:
        v2.add_scalar("abc")
    except ValueError as ve:
        print(ve)
    print("\nAdd a scalar to a vector: scalar is 10, vector is v2:")
    print(v2.add_scalar(10))

    print("\nex. 2. Vector operations:")
    print("\na.")
    print("Add two vectors: v1 + v2:")
    print(v1.add_two_vectors(v2))
    print("\nAdd two vectors: v5 + v6:")
    try:
        v5.add_two_vectors(v6)
    except ValueError as ve:
        print(ve)
    print("\nAdd two vectors: v3 + v4:")
    print(v3.add_two_vectors(v4))

    print("\nb.")
    print("Subtract two vectors: v5 - v4:")
    print(v5.subtract(v4))
    print("\nSubtract two vectors: v1 - v6:")
    try:
        v1.subtract(v6)
    except ValueError as ve:
        print(ve)
    print("\nSubtract two vectors: v3 - v4:")
    print(v3.subtract(v4))

    print("\nc.")
    print("Multiplication of two vectors: v1 * v5:")
    print(v1.multiplication(v5))
    print("\nMultiplication of two vectors: v2 * v6:")
    try:
        v2.multiplication(v6)
    except ValueError as ve:
        print(ve)
    print("\nMultiplication of two vectors: v2 * v4:")
    print(v2.multiplication(v4))

    print("\nex. 3. Reduction operations:")
    print("\na.")
    print("Sum of elements in a vector: in vector v3:")
    print(v3.sum_of_values())
    print("\nSum of elements in a vector: in vector v1:")
    print(v1.sum_of_values())

    print("\nb.")
    print("Product of elements in a vector: in vector v5:")
    print(v5.product_of_elements())
    print("\nProduct of elements in a vector: in vector v2:")
    print(v2.product_of_elements())

    print("\nc.")
    print("Average of elements in a vector: in vector v1")
    print(v1.average_of_elements())
    print("\nAverage of elements in a vector: in vector v2")
    print(v2.average_of_elements())

    print("\nd.")
    print("Minimum of a vector: in vector v2")
    print(v2.min_of_vector())
    print("\nMinimum of a vector: in vector v6")
    print(v6.min_of_vector())

    print("\ne.")
    print("Maximum of a vector: in vector v3")
    print(v3.max_of_vector())
    print("\nMaximum of a vector: in vector v1")
    print(v1.max_of_vector())

    repo = v.VectorRepository([v.MyVector("A", "r", 1, [1, 2, 3, 4, 5]), v.MyVector("B", "b", 2, [3.2, 4.5, 5.7, 6.1]),
                            v.MyVector("C", "g", 3, [4, 5, 6, 7, 8]), v.MyVector("D", "m", 4, [7, 8, 9, 10])])

    print(repo)

    print("\nIteration 2:")
    print("ex. 1.")
    print("Add a vector to the repository:")
    print("\nAdd a new vector: MyVector(\"E\", \"m\", 4, [1, -1, 10])")
    print(repo.addVector("E", "m", 4, [1, -1, 10]))
    print("\nAdd a new vector: MyVector(\"E\", \"r\", 2, [-1, 10])")
    try:
        repo.addVector("E", "r", 2, [-1, 10])
    except ValueError as ve:
        print(ve)
    print("\nAdd a new vector: MyVector(\"F\", \"y\", 11, [1, 2, 10])")
    print(repo.addVector("F", "y", 11, [1, 2, 10]))

    print("\nex. 2.")
    print("Get all vectors:")
    print(repo.getAllVectors())

    print("\nex. 3.")
    print("Get a vector at a given index.")
    print("\nGet the vector at index -3:")
    try:
        repo.getAtIndex(-3)
    except IndexError as ie:
        print(ie)
    print(f"\nThe vector at index 0 is {repo.getAtIndex(0)}")
    print(f"\nThe vector at index 1 is {repo.getAtIndex(1)}")

    print("\nex. 4.")
    print("Update a vector at a given index.")
    print("\nUpdate the vector at index 0.")
    name_id = "Z"
    colour = "m"
    print(f"The list with the updated vector is: {repo.updateVectorAtIndex(0, name_id, colour, 21, [0, -1, -5])}")
    name_id = "X"
    colour = "r"
    print("\nUpdate the vector at index -10.")
    try:
        repo.updateVectorAtIndex(-10, name_id, colour, 2, [8])
    except IndexError as ie:
        print(ie)
    print("\nUpdate the point at index 1.")
    name_id = "X"
    colour = "r"
    print(f"The list with the updated vector is: {repo.updateVectorAtIndex(1, name_id, colour, 1, [10, -1])}")
    
    print("\nex. 5.")
    print("Update a vector identified by name_id.")
    name_id = "X"
    new_name_id = "A2"
    colour = "m"
    print(f"\nThe list with the updated vector is: {repo.updateByNameID(name_id, new_name_id, colour, 12, [1, 2 , 3] )}")
    name_id = "Z"
    new_name_id = "A3"
    colour = "r"
    print(f"\nThe list with the updated vector is: {repo.updateByNameID(name_id, new_name_id, colour, 2, [121, 3])}")
    name_id = "C"
    new_name_id = "A5"
    colour = "g"
    print(f"\nThe list with the updated vector is: {repo.updateByNameID(name_id, new_name_id, colour, 30, [5, 6, 3])}")

    print("\nex. 6.")
    print("Delete a vector by index.")
    print("\nDelete the vector at index -3:")
    try:
        repo.deleteVectorAtIndex(-3)
    except IndexError as ie:
        print(ie)
    print(f"\nThe list after deleting the vector at index 0 is {repo.deleteVectorAtIndex(0)}")
    print(f"\nThe list after deleting the vector at index 1 is {repo.deleteVectorAtIndex(1)}")

    print("\nex. 7.")
    print("Delete a vector by name_id.")
    name_id = "A2"
    print(f"\nThe list after deleting the vector with name_id = A2 is: {repo.deleteVectorByNameId(name_id)}")
    name_id = "A3"
    try:
        repo.deleteVectorByNameId(name_id)
    except IndexError as ie:
        print(ie)
    name_id = "D"
    print(f"\nThe list after deleting the vector with name_id = D is: {repo.deleteVectorByNameId(name_id)}")

    print("\nex. 8.")
    print("This is the chart representation of the points:")
    repo.plotAllVectors()


def printMenu():
    print("MENU:")
    print("-2 - Print data examples")
    print("-1 - Print menu")
    print(" 0 - Exit program")
    print(" 1 - Add a vector to the repository")
    print(" 2 - Get all vectors")
    print(" 3 - Get a vector at a given index")
    print(" 4 - Update a vector at a given index")
    print(" 5 - Update a vector identified by name_id")
    print(" 6 - Delete a vector by index")
    print(" 7 - Delete a vector by name_id")
    print(" 8 - Plot all vectors")


def start():
    print()
    vector_repo = v.VectorRepository()
    printMenu()
    command = None
    while command != 0:
        try:
            command = int(input(">>> "))
            if command == -2:
                dataExamples()
            elif command == -1:
                printMenu()
            elif command == 0:
                print("Program ended!")
            elif command == 1:
                name_id = input("name_id:")
                colour = input("colour:")
                vector_type = int(input("vector_type:"))
                try:
                    values = []
                    while True:
                        value = input("values:")
                        if "." in value:
                            values.append(float(value))
                        else:
                            values.append(int(value))
                except:
                    print()
                try:
                    print(vector_repo.addVector(name_id, colour, vector_type, values))
                except ValueError as ve:
                    print(ve)
            elif command == 2:
                print(vector_repo.getAllVectors())
            elif command == 3:
                index = int(input("index:"))
                try:
                    print(vector_repo.getAtIndex(index))
                except IndexError as ie:
                    print(ie)
            elif command == 4:
                try:
                    index = int(input("index:"))
                    name_id = input("new_name_id:")
                    colour = input("new_colour:")
                    vector_type = int(input("new_type:"))
                    try:
                        values = []
                        while True:
                            value = input("values:")
                            if "." in value:
                                values.append(float(value))
                            else:
                                values.append(int(value))
                    except:
                        print()
                    try:
                        print(vector_repo.updateVectorAtIndex(index, name_id, colour, vector_type, values))
                    except ValueError as ve:
                        print(ve)
                except IndexError as ie:
                    print(ie)
            elif command == 5:
                try:
                    name_id = input("name_id:")
                    new_name_id = input("new_name_id:")
                    colour = input("new_colour:")
                    vector_type = int(input("new_type:"))
                    try:
                        values = []
                        while True:
                            value = input("values:")
                            if "." in value:
                                values.append(float(value))
                            else:
                                values.append(int(value))
                    except:
                        print()
                    try:
                        print(vector_repo.updateByNameID(name_id, new_name_id, colour, vector_type, values))
                    except ValueError as ve:
                        print(ve)
                except IndexError as ie:
                    print(ie)
            elif command == 6:
                index = int(input("What is the index of the point?"))
                try:
                    print(vector_repo.deleteVectorAtIndex(index))
                except IndexError as ie:
                    print(ie)
            elif command == 7:
                name_id = input("name_id: ")
                try:
                    print(vector_repo.deleteVectorByNameId(name_id))
                except IndexError as ie:
                    print(ie)
            elif command == 8:
                vector_repo.plotAllVectors()
            else:
                print("Invalid command")
        except ValueError:
            print("Invalid type entered!")
