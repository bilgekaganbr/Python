#Program that determines letter grade of a student

#Take exam grades as input

midterm1 = int(input("Midterm 1:"))
midterm2 = int(input("Midterm 2:"))
final = int(input("Final:"))

#The total grade will be the sum of thirty percent midterm1, thirty percent of midterm2 and forty percent of final

total_grade = midterm1 * 0.3 + midterm2 * 0.3 + final * 0.4

#If the total grade greater than or equal 90, print AA
if total_grade >= 90:

    print("AA")

#Else if the total grade greater than or equal 85, print BA
elif total_grade >= 85:

    print("BA")

#Else if the total grade greater than or equal 80, print BB
elif total_grade >= 80:

    print("BB")

#Else if the total grade greater than or equal 75, print CB
elif total_grade >= 75:

    print("CB")

#Else if the total grade greater than or equal 70, print CC
elif total_grade >= 70:

    print("CC")

#Else if the total grade greater than or equal 65, print DC
elif total_grade >= 65:

    print("DC")

#Else if the total grade greater than or equal 70, print DD
elif total_grade >= 60:

    print("DD")

#Else, the total grade is less than 60 print "Failed!"
else:

    print("Failed!")