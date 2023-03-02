#program that combines names and surnames and returns them in alphabetical order

#given names and surnames
names = ["Kerim","Tarık","Ezgi","Kemal","İlkay","Şükran","Merve"]
surnames = ["Yılmaz","Öztürk","Dağdeviren","Atatürk","Dikmen","Kaya","Polat"]

#combine names and surnames with zip
name_list = list(zip(names, surnames))

#sort the name_list
name_list.sort()

for i,j in name_list:

    print(i, j)