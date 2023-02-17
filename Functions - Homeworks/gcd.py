#program that calculates the gcd of two numbers


def gcd(x, y):

    #initialize the loop variable as 2
    i = 2

    #initialize the gcd(the greatest common factor) as 1
    gcd = 1

    #continue looping until both numbers become 1
    while x > 1 or y > 1:

        #if both numbers can be divided by i, divide both of them and multiply gcd by i
        if x % i == 0 and y % i == 0:

            x = x / i
            y = y / i

            gcd *= i

        #if only one of numbers can be divided by i, only divide it
        elif x % i == 0 and y % i != 0:

            x = x / i

        elif x % i != 0 and y % i == 0:

            y = y / i

        #if both of numbers can not be divided by i, increase the loop variable by 1
        else:

            i += 1

    return gcd

while True:

    x = input("x(q for exit): ")
    y = input("y(q for exit): ")

    if x == "q" or y == "q":

        print("Farewell")
        break

    else:

        x = int(x)
        y = int(y)

        print("gcd of {} and {} is {}".format(x, y, gcd(x, y)))