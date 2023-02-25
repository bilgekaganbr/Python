#programm that returns whether a number is even or not

#function that determines a number is even or not
def is_even(number):

    if number % 2 != 0:

        raise ValueError()

    else:

        return number

list = [20, 58, 10, 76, 45, 92, 2, 73, 78, 3]

for i in list:

    #try is_even function for the element i
    try:

        print(is_even(i))

    except ValueError:

        pass