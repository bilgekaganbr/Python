#program that determines prime numbers from 1 to 1000 and determines perfect numbers from 1 to 1000 as a decorator

def is_perfect(func):

    def wrapper():

        print("Perfect Numbers;")

        for number in range(1, 1001):

            #initialize the sum from 0
            sum = 0

            #initialize the loop variable by 1
            i = 1

            while i < number:

                if number % i == 0:

                    #if the number can be divided by i, increase the sum by i
                    sum += i

                #increase the loop variable by 1
                i += 1

            #if the number is equal to sum, it is a perfect number
            if number == sum:

                print(number)

        #call the func object
        func()

    return wrapper

#decoration annotation
@is_perfect
def is_prime():

    print("Prime Numbers;")

    for number in range(2, 1001):

        #initialize the loop variable from 2
        i = 2

        #initialize the count from 0
        count = 0

        while i < number:

            if number % i == 0:

                #if the number can be divided by i, increase the count by 1
                count += 1

            #increase the loop variable by 1
            i += 1

        #if the count stays 0 then the number is a prime
        if count == 0:

            print(number)

is_prime()

