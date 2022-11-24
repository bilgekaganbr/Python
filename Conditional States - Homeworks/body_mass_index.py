#Program that calculates body mass index

#Take height(m) and weight(kg)

height = float(input("Height: "))
weight = float(input("Weight: "))

#Calculate body mass index as bmi = weight / (height * height)

bmi = weight / (height * height)

if bmi < 18.5:

    #If bmi is less than 18.5, print thin
    print("Thin!")

elif bmi >= 18.5 and bmi < 25:

    #Else if bmi is between 18.5 and 25, print normal
    print("Normal!")

elif bmi >= 25 and bmi < 30:

    #Else if bmi is between 25 and 30, print overweight
    print("Overweight!")

else:

    #Else, bmi greater than or equal than 30, print obese
    print("Obese!")