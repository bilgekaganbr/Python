#program that calculates the area of a rectangle from given values

#define a function which takes a tuple as a parameter, and return the multiplication of elements of the tuple
def area(tuple):

    return tuple[0] * tuple[1]

#given valus
values = [(3,4), (10,3), [5,6], [1,9]]

#use the map function for all elements of values list
areas = list(map(area, values))
print(areas)
