#program that combines and prints the initials of rows in a text

#empty string
initials = ""

with open("poem.txt", "r", encoding="utf-8") as file:

    for row in file:

        initials += row[0]

print(initials)