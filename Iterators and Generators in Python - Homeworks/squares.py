#program that calculates square of numbers from an iterable class

class Squares:

    #'max' represents the maximum number we will square
    def __init__(self,max):

        self.max = max

        #initialize the first number from 1
        self.number = 1

    def __iter__(self):

        #iter function must return the object's itself
        return self

    def __next__(self):

        if self.number <= self.max:

            #if the number is smaller than the maximum calculate the square of it and increase it by 1
            result = self.number ** 2
            self.number += 1

            return result

        else:

            raise StopIteration

#'30' is an example
squares = Squares(30)

#create an iterator from squares object
iterator = iter(squares)

for i in squares:

    print(i)