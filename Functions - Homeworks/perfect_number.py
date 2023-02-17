#Program that prints perfect numbers from 1 to 1000

def is_perfect(number):

    #initialize sum as 0
    sum = 0

    for i in range(1, number):

        #if the number can be divided by i
        if number % i == 0:

            #increase sum by i
            sum += i

    #if sum is equal to the number, return true
    if sum == number:

        return True


for i in range(1, 1001):

    #if is_perfect is true, print the number
    if is_perfect(i):

        print(i)

