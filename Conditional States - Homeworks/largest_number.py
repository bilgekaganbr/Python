#Program that takes three numbers as input and print the largest one

x = float(input("x: "))
y = float(input("y: "))
z = float(input("z: "))

#If x is greater than others
if x > y and x > z:

    print("The largest:", x)

#If y is greater than others
elif y > x and y > z:

    print("The largest:", y)

#If z is greater than others
elif z > x and z > y:

    print("The largest:", z)

#If two of numbers are equal and greater than the third one or all three numbers are equal
else:

    print("Equality occured!")