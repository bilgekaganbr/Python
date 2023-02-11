#program that prints all numbers which can be divided by 3 from 1 to 100

for i in range(1, 101):

    if i % 3 == 0:

        print(i)

    else:

        #skip numbers that can not be divided by 3
        continue