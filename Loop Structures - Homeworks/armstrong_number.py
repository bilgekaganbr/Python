#program that determines whether a number is armstrong or not

while True:

    #initialize sum as 0
    sum = 0

    #take the number from user
    number = input("Number(q for exit): ")

    #if number is q, end program
    if number == "q":

        print("Farewell")
        break

    else:

        #Else, calculate the number of digits
        digit = len(number)

        for i in number:

            #convert digits to int and take their powers by the number of digits and add to sum
            sum += int(i) ** digit

        #if the number is equal to sum, it is an armstrong number
        if int(number) == sum:

            print("{} is an armstrong number!".format(number))

        #else, it is not an armstrong number
        else:

            print("{} is not an armstrong number!".format(number))

