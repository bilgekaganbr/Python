

def is_prime():

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

        #if the count stays 0 then the number is prime
        if count == 0:

            yield number

for number in is_prime():

    print(number)