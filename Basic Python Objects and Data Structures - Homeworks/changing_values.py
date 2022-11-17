#Program that swaps the values of two numbers with each other

#Take two numbers from user

a = float(input("a: "))
b = float(input("b: "))

#Before

print("a: {} and b: {}".format(a, b))

#Swap the values of two numbers with each other

a, b = b, a

#After

print("a: {} and b: {}".format(a, b))

