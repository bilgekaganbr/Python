#Program that Calculates Body Mass Index

#Take height(m) and weight(kg)

height = float(input("Height(m): "))
weight = float(input("Weight(kg): "))

#Calculate body mass index as bmi = weight / (height * height)

bmi = weight / (height * height)

#Print the result

print("Your body mass index: ", bmi)