#program that prints valid mails

with open("mails.txt", "r", encoding="utf-8") as file:

    for mail in file:

        mail = mail[:-1]

        #if the mail contains '@' anywhere except at the beginning and endswith '.com', print the mail
        if mail.find("@") > 0 and mail.endswith(".com"):

            print(mail)