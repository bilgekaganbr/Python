#program that creates player files by teams

#create empty lists of teams
gs = list()
fb = list()
bjk = list()

def players_by_teams(row):

    #get comma separated elements of the row
    list = row.split(",")

    #name the elements of list appropriately
    name = list[0]
    team = list[1]

    #append player names by team name to the relevant lists
    if team == "Galatasaray\n":

        gs.append(name + "\n")

    elif team == "Fenerbahçe\n":

        fb.append(name + "\n")

    elif team == "Beşiktaş\n":

        bjk.append(name + "\n")

with open("player.txt", "r", encoding="utf-8") as file:

    for i in file:

        #send each element of the file to the players_by_teams function
        players_by_teams(i)

    with open("gs.txt", "w", encoding="utf-8") as file2:

        #write all elements of the gs list to the gs file
        for i in gs:

            file2.write(i)

    with open("fb.txt", "w", encoding="utf-8") as file3:

        #write all elements of the fb list to the fb file
        for i in fb:

            file3.write(i)

    with open("bjk.txt", "w", encoding="utf-8") as file4:

        #write all elements of the bjk list to the bjk file
        for i in bjk:

            file4.write(i)
