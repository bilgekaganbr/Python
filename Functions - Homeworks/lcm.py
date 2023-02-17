#program that calculates the lcm of two numbers

def lcm(x, y):

    #initialize the loop variable as 2
    i = 2

    #initialize the lcm(the lowest common multiple) as 1
    lcm = 1

    #continue looping until both numbers become 1
    while x > 1 or y > 1:

        #if both numbers can be divided by i, divide both of them and multiply lcm by i
        if x % i == 0 and y % i == 0:

            x = x / i
            y = y / i

            lcm *= i

        #if only one of numbers can be divided by i, only divide that number and multiply lcm by i
        elif x % i == 0 and y % i != 0:

            x = x / i

            lcm *= i

        elif x % i != 0 and y % i == 0:

            y = y / i

            lcm *= i

        #if both of numbers can not be divided by i, increase the loop variable by 1
        else:

            i += 1

    return lcm

while True:

    x = input("x(q for exit): ")
    y = input("y(q for exit): ")

    if x == "q" or y == "q":

        print("Farewell")
        break

    else:

        x = int(x)
        y = int(y)

        print("lcm of {} and {} is {}".format(x, y, lcm(x, y)))