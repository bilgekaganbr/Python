#programme that creates students' letter grades, passing and failing files

def calculate_grade(row):

    #erase the extra \n
    row = row[:-1]

    #get comma separated elements of the row
    list = row.split(",")

    #name the elements of list appropriately
    name = list[0]
    grade1 = int(list[1])
    grade2 = int(list[2])
    grade3 = int(list[3])

    #calculate the final grade
    final_grade = grade1 * 0.3 + grade2 * 0.3 + grade3 * 0.4

    #determine the appropriate letter grades
    if final_grade >= 90:

        letter = "AA"

    elif final_grade >= 85:

        letter = "BA"

    elif final_grade >= 80:

        letter = "BB"

    elif final_grade >= 75:

        letter = "CB"

    elif final_grade >= 70:

        letter = "CC"

    elif final_grade >= 65:

        letter = "DC"

    elif final_grade >= 60:

        letter = "DD"

    else:

        letter = "FF"

    return name + ":" + letter + "\n"

def passed_failed(row):

    #get colon separated elements of the row
    list = row.split(":")

    #there are two elements in the list: name of the student and his/her letter grade with an additional \n
    letter_grade = list[1]

    #if the element in the first index a.k.a letter grade with an additional \n is FF\n return True
    if letter_grade != "FF\n":

        return True

    #else return False
    else:

        return False


with open("file.txt", "r", encoding="utf-8") as file:

    #create three empty lists as grades, passed and failed
    grades = list()
    passed_list = list()
    failed_list = list()

    for i in file:

        #send each element of the file to the calculate_grade function and append the result to the grade list
        grades.append(calculate_grade(i))

    with open("grades.txt", "r+", encoding="utf-8") as file2:

        #write all elements of the grade list to the grades file
        for i in grades:

            file2.write(i)

        for i in file2:

            #send each element of the grades file to the passed_failed function, if the result is True
            #append it to the passed_list
            if passed_failed(i):

                passed_list.append(i)

            #if the reuslt is False, append it to the failed_list
            else:

                failed_list.append(i)

        with open("passed.txt", "w", encoding="utf-8") as file3:

            #write all elements of the passed_list to the passed file
            for i in passed_list:

                file3.write(i)

        with open("failed.txt", "w", encoding="utf-8") as file4:

            #write all elements of the failed_list to the failed file
            for i in failed_list:

                file4.write(i)








