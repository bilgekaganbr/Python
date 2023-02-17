#program that prints all pisagor triangles for numbers between 1 and 100

def pisagor():

    #define an empty list
    pisagor_list = list()

    for a in range(1, 101):

        for b in range(1, 101):

            #calculate hypotenuse
            c = (a ** 2 + b ** 2) ** 0.5

            if c == int(c):

                #if hypotenuse is an integer, add a, b, and hypotenuse to the list as tuple
                pisagor_list.append((a, b, int(c)))

    return pisagor_list


for i in pisagor():

    #print all elements in the pisagor list
    print(i)



