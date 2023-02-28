#program that returns whether the shape indicates a triangle according to the given values

#define a function which takes a tuple as a parameter and return True if elements of the tuple indicate a triangle, False if not
def is_triangle(tuple):

    if abs(tuple[0] + tuple[1]) > tuple[2] and abs(tuple[1] + tuple[2]) > tuple[0] and abs(tuple[0] + tuple[2]) > tuple[1]:

        return True

    else:

        return False

#given values
values = [(3,4,5),(6,8,10),(3,10,7)]

#use the filter function for all elements of values list
result = list(filter(is_triangle, values))
print(result)