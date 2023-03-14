from song import *

print("""
************************************
Welcome to the Song Library

Operations;

1.Show Songs

2.Find Song

3.Add Song

4.Delete Song

5.Total Duration

q for exit
************************************
""")

songLibrary = SongLibrary()

while True:

    operation = input("Operation: ")

    if operation == "q":

        print("Farewell...")

        #if the operation is 'q' end the program
        break

    elif operation == "1":

        songLibrary.show_songs()

    elif operation == "2":

        name = input("Song name: ")

        print("Please wait...")
        time.sleep(2)

        songLibrary.find_song(name)

    elif operation == "3":

        name = input("Name: ")
        artist = input("Artist: ")
        album = input("Album: ")
        production_company = input("Production Company: ")
        duration = input("Duration: ")

        #define new song object by using inputs
        new_song = Song(name,artist,album,production_company,duration)

        print("Please wait...")
        time.sleep(2)

        songLibrary.add_song(new_song)
        print("The song is added...")

    elif operation == "4":

        name = input("Song name: ")

        answer = input("Are you sure(Y/N): ")

        if answer == "Y":

            print("Please wait...")
            time.sleep(2)

            songLibrary.delete_song(name)
            print("The song is deleted...")

    elif operation == "5":

        print("Total duration: ",songLibrary.total_duration())

    else:

        print("Invalid operation...")