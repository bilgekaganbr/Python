#program that calculates sum of numbers that given by user

#initialize sum as 0
sum = 0

while True:

    #take the number from user
    number = input("Number(q for exit): ")

    if number == "q":

        #if the number is q, print sum and end the loop
        print(sum)
        break

    else:

        #else, convert the number to int
        number = int(number)

        #increase sum by number
        sum += number