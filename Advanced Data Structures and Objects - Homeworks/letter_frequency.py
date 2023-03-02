#program that finds the frequency of letters in a given string

#given string
s = "ProgramlamaÖdeviİleriSeviyeVeriYapılarıveObjeleripynb"

#empty dictionary
letter_dict = dict()

for i in s:

    #if letter in letter_dict, increase its frequency by 1
    if i in letter_dict:

        letter_dict[i] += 1

    #else, initialize its frequency from 1
    else:

        letter_dict[i] = 1

for letter, frequency in letter_dict.items():

    print(letter, frequency)
    print("----------------------------")