#program that determines whether a number is perfect or not

while True:

    #initialize sum as 0
    sum = 0

    #take the number from user
    number = input("Number(q for exit): ")

    #if the number is q, end the program
    if number == "q":

        print("Farewell")
        break

    else:

        #else, convert the number to int
        number = int(number)

        #initialize loop variable i as 1
        i = 1

        while i < number:

            #if the number can be divided by i, increase sum by i
            if number % i == 0:

                sum += i
                i += 1

            else:

                i += 1

        #if the number is equal to sum, it is a perfect number
        if number == sum:

            print("{} is a perfect number!".format(number))

        #else, it is not a perfect number
        else:

            print("{} is not a perfect number!".format(number))

