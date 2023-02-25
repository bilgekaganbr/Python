#program that returns strings containing only numbers

#the list is given
list = ["345","sadas","324a","14","kemal"]

for i in list:

    #try if element i can be converted to int. If so, print i
    try:

        if int(i):

            print(i)

    except:

        pass