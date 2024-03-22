from domain import numbers as n


def printMenu():
    print("MENU:")
    print(" -2 - print data examples")
    print(" -1 - print menu")
    print(" 0 - exit program")
    print(" 1 - add a point to the repository")
    print(" 2 - get all points")
    print(" 3 - get a point at a given index")
    print(" 4 - get all points of a given colour")
    print(" 5 - get all points that are inside a given square")
    print(" 6 - get the minimum distance between two points")
    print(" 7 - update a point at a given index")
    print(" 8 - delete a point by index")
    print(" 9 - delete all points that are inside a given square")
    print(" 10 - plot all points in a chart")
    print(" 11 - get all points that are inside a given circle")
    print(" 12 - update the colour of a point given its coordinates")
    print(" 13 - delete a point by coordinates")


def dataExamples():
    repo = n.PointRepository([n.MyPoint(1, 2, "red"), n.MyPoint(2, 3, "green"), n.MyPoint(3, 4, "blue"),
                              n.MyPoint(5, 6, "yellow"), n.MyPoint(6, 7, "magenta"), n.MyPoint(10, 11, "red"),
                              n.MyPoint(10, 12, "blue"), n.MyPoint(15, 16, "green"), n.MyPoint(20, 21, "red"),
                              n.MyPoint(-10, -1, "magenta")])

    print(repo)

    print("ex. 1.")
    print("Add a point to the repository.")
    print("\nAdd a new point: MyPoint(10, 4, \"green\")")
    print(repo.addPoint(10, 4, "green"))
    print("\nAdd a new point: MyPoint(1, -1, \"black\")")
    try:
        repo.addPoint(1, -1, "black")
    except ValueError as ve:
        print(ve)
    print("\nAdd a new point: MyPoint(2, 21, \"red\")")
    print(repo.addPoint(2, 21, "red"))

    print("\nex. 2.")
    print("Get all points.")
    print(repo.getAllPoints())

    print("\nex. 3.")
    print("Get a point at a given index.")
    print("\nGet the point at index -3:")
    try:
        repo.getPointAtIndex(-3)
    except IndexError as ie:
        print(ie)
    print(f"\nThe point at index 5 is {repo.getPointAtIndex(5)}")
    print(f"\nThe point at index 2 is {repo.getPointAtIndex(2)}")

    print("\nex. 4.")
    print("Get all points of a given colour.")
    print("\nGet all points of colour black.")
    colour = "black"
    try:
        repo.getPointsOfGivenColour(colour)
    except ValueError as ve:
        print(ve)
    colour = "red"
    print(f"All the points of colour blue are: {repo.getPointsOfGivenColour(colour)}")
    colour = "green"
    print(f"All the points of colour green are: {repo.getPointsOfGivenColour(colour)}")

    print("\nex. 5.")
    print("Get all points that are inside a given square.")
    print("\nAll points that are inside the square with coord_x = 1 coord_y = 1 of the up-left corner and length of 10 are:")
    print(repo.getPointsInsideSquare(1, 1, 10))
    print("\nAll points that are inside the square with coord_x = -1 coord_y = 5 of the up-left corner and length of 6 are:")
    print(repo.getPointsInsideSquare(-1, 5, 6))
    print("\nAll points that are inside the square with coord_x = 1 coord_y = 10 of the up-left corner and length of 20 are:")
    print(repo.getPointsInsideSquare(1, 10, 20))

    print("\nex. 6.")
    print("Get the minimum distance between two points.")
    try:
        if repo:
            print(f"The minimum distance between two points is: {repo.minimumDistanceBetweenTwoPoints()}")
    except ValueError as ve:
        print(ve)

    print("\nex. 7.")
    print("Update a point at a given index.")
    print("\nUpdate the point at index 1.")
    colour = "green"
    print(f"The list with the updated point is: {repo.updatePoint(1, 11, 23, colour)}")
    colour = "red"
    print("\nUpdate the point at index -10.")
    try:
        repo.updatePoint(-10, 1, 3, colour)
    except IndexError as ie:
        print(ie)
    print("\nUpdate the point at index 3.")
    colour = "yellow"
    print(f"The list with the updated point is: {repo.updatePoint(3, 1, -3, colour)}")

    print("\nex. 8.")
    print("Delete a point by index")
    print("\nDelete the point at index 1.")
    print(f"This is the list after deleting the point at index 1: {repo.deletePoint(1)}")
    print("\nDelete the point at index -20.")
    try:
        repo.deletePoint(-20)
    except IndexError as ie:
        print(ie)
    print("\nDelete the point at index 0.")
    print(f"This is the list after deleting the point at index 0: {repo.deletePoint(0)}")

    print("\nex. 9.")
    print("Delete all points that are inside a given square.")
    print("\nThe list after deleting all points inside the square with coord_x = 1 coord_y = 1 of the up-left corner and length of 10 is:")
    print(repo.deleteAllPointsInSquare(1, 1, 20))
    print("\nThe list after deleting all points inside the square with coord_x = -1 coord_y = 5 of the up-left corner and length of 6 is:")
    print(repo.deleteAllPointsInSquare(-10, 5, 6))
    print("\nThe list after deleting all points inside the square with coord_x = 1 coord_y = 10 of the up-left corner and length of 20 is:")
    print(repo.deleteAllPointsInSquare(1, 10, 20))

    print("\nex. 10.")
    print("This is the chart representation of the points:")
    repo.plotAllPoints()

    print("\nex. 11.")
    print("Get all points that are inside a given circle.")
    print("\nAll points that are inside the circle with circle_x = 1 circle_y = 1 and radius = 100 are:")
    print(repo.getAllPointsInsideCircle(1, 1, 100))
    print("\nAll points that are inside the circle with circle_x = 0 circle_y = 0 and radius = 8 are:")
    print(repo.getAllPointsInsideCircle(0, 0, 8))
    print("\nAll points that are inside the circle with circle_x = 10 circle_y = 2 and radius = -1 are:")
    try:
        repo.getAllPointsInsideCircle(1, 2, -1)
    except ValueError as ve:
        print(ve)

    print("\nex. 15.")
    print("Update the colour of a point given its coordinates.")
    print("\nUpdate the point of coord_x = 2 and coord_y = 21 with colour = green")
    colour = "green"
    print(f"This is the list with the updated point: {repo.updateColour(2, 21, colour)}")
    print("\nUpdate the point of coord_x = 15 and coord_y = 16 with colour = black")
    colour = "black"
    try:
        repo.updateColour(15, 16, colour)
    except ValueError as ve:
        print(ve)
    print("\nUpdate the point of coord_x = 15 and coord_y = 16 with colour = magenta")
    colour = "magenta"
    print(f"This is the list with the updated point: {repo.updateColour(15, 16, colour)}")

    print("\nex. 18.")
    print("Delete a point by coordinates.")
    print(f"\nThe list after deleting the point with coord_x = 10 and coord_y = 11 is: {repo.deletePointByCoordinates(10, 11)}")
    print(f"\nThe list after deleting the point with coord_x = 10 and coord_y = 12 is: {repo.deletePointByCoordinates(10, 12)}")
    print(f"\nThe list after deleting the point with coord_x = 15 and coord_y = 16 is: {repo.deletePointByCoordinates(15, 16)}")


def start():
    the_point_repository = n.PointRepository()
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
                coord_x = int(input("coord_x:"))
                coord_y = int(input("coord_y:"))
                colour = input("colour:")
                try:
                    print(the_point_repository.addPoint(coord_x, coord_y, colour))
                except ValueError as ve:
                    print(ve)
            elif command == 2:
                print(the_point_repository.getAllPoints())
            elif command == 3:
                index = int(input("What is the index of the point?"))
                try:
                    print(the_point_repository.getPointAtIndex(index))
                except IndexError as ie:
                    print(ie)
            elif command == 4:
                colour = input("What is the colour?")
                try:
                    print(the_point_repository.getPointsOfGivenColour(colour))
                except ValueError as ve:
                    print(ve)
            elif command == 5:
                coord_x = int(input("What is the coord_x of the corner?"))
                coord_y = int(input("What is the coord_y of the corner?"))
                length = int(input("What is the length of the square?"))
                print(n.PointRepository.getPointsInsideSquare(the_point_repository, coord_x, coord_y, length))
            elif command == 6:
                try:
                    print(the_point_repository.minimumDistanceBetweenTwoPoints())
                except ValueError as ve:
                    print(ve)
            elif command == 7:
                index = int(input("What is the index of the point?"))
                new_coord_x = int(input("What is the new_coord_x?"))
                new_coord_y = int(input("What is the new_coord_y?"))
                new_colour = input("What is the new_colour?")
                try:
                    print(the_point_repository.updatePoint(index, new_coord_x, new_coord_y, new_colour))
                except IndexError as ie:
                    print(ie)
                except ValueError as ve:
                    print(ve)
            elif command == 8:
                index = int(input("What is the index of the point?"))
                try:
                    print(the_point_repository.deletePoint(index))
                except IndexError as ie:
                    print(ie)
            elif command == 9:
                coord_x = int(input("What is the coord_x of the corner?"))
                coord_y = int(input("What is the coord_y of the corner?"))
                length = int(input("What is the length of the square?"))
                print(the_point_repository.deleteAllPointsInSquare(coord_x, coord_y, length))
            elif command == 10:
                the_point_repository.plotAllPoints()
            elif command == 11:
                circle_x = int(input("What is the coord_x of the center of circle?"))
                circle_y = int(input("What is the coord_y of the center of circle?"))
                radius = int(input("What is the radius of the circle?"))
                try:
                    print(the_point_repository.getAllPointsInsideCircle(circle_x, circle_y, radius))
                except ValueError as ve:
                    print(ve)
            elif command == 12:
                coord_x = int(input("What is the coord_x?"))
                coord_y = int(input("What is the coord_y?"))
                new_colour = input("What is the new colour?")
                try:
                    print(the_point_repository.updateColour(coord_x, coord_y, new_colour))
                except IndexError as ie:
                    print(ie)
                except ValueError as ve:
                    print(ve)
            elif command == 13:
                coord_x = int(input("What's the coord_x of the point?"))
                coord_y = int(input("What's the coord_y of the point?"))
                try:
                    print(the_point_repository.deletePointByCoordinates(coord_x, coord_y))
                except IndexError as ie:
                    print(ie)
            else:
                print("Invalid command!")
        except ValueError:
            print("Invalid type entered!")
