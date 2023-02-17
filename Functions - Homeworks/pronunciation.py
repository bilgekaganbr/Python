#program that prints the pronunciation of a number

#define lists of units and tenth
units = ["", "bir", "iki", "üç", "dört", "beş", "altı", "yedi", "sekiz", "dokuz"]
tenth = ["", "on", "yirmi", "otuz", "kırk", "elli", "altmış", "yetmiş", "seksen", "doksan"]

def pronunciation(number):

    #units of the number is the remainder of dividing the number by 10
    number_units = number % 10

    #tenth of the number is the integer division of the number by 10
    number_tenth = number // 10

    #return correct indices from the units and the tenth list
    return tenth[number_tenth] + " " + units[number_units]

while True:

    number = input("Number(q for exit): ")

    if number == "q":

        print("Farewell")
        break

    else:

        number = int(number)

        print(pronunciation(number))