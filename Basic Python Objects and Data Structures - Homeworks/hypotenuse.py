#Program that calculates hypotenuse

#Get perpendicular sides

a = float(input("a: "))
b = float(input("b: "))

#Calculate the hypotenuse as c = (a ** 2 + b ** 2) ** 0.5

c = (a ** 2 + b ** 2) ** 0.5

#Print the hypotenuse

print("Hypotenuse: ", c)