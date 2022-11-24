#Program that determines the geometric shape

#Take the shape from the user
shape = input("Shape: ").lower()

#Check the shape is quadrilateral or triangle
if shape == "quadrilateral":

    #If the shape is quadrilateral, take four edges as an input
    a = float(input("Edge 1: "))
    b = float(input("Edge 2: "))
    c = float(input("Edge 3: "))
    d = float(input("Edge 4: "))

    #Check if the shape is square
    if a == b and a == c and a == d:

        print("Square")

    #Else if, check the shape is rectangle
    elif a == c and b == d:

        print("Rectangle")

    #Else if check the shape is ordinary quadrilateral
    else:

        print("Ordinary quadrilateral")

#Else if, check the shape is triangle
elif shape == "triangle":

    #If the shape is triangle, take 3 edges as input
    a = float(input("Edge 1: "))
    b = float(input("Edge 2: "))
    c = float(input("Edge 3: "))

    #Check if the shape is valid triangle
    if abs(a + b) > c and abs(a + c) > b and abs(b + c) > a:

        #If valid, check if it is equilateral
        if a == b and a == c:

            print("Equilateral triangle")

        #Else if, check it is isosceles
        elif (a == b and a != c) or (a == c and a != b) or (b == c and b != a):

            print("Isosceles triangle")

        #Else, check it is scalene
        else:

            print("Scalene triangle")

    #Else, it is an invalid triangle
    else:

        print("Invalid triangle")

#Else, the shape is invalid
else:

    print("Invalid shape")
