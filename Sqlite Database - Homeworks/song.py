import sqlite3
import time
import datetime

class Song:

    def __init__(self,name,artist,album,production_company,duration):

        self.name = name
        self.artist = artist
        self.album = album
        self.production_company = production_company
        self.duration = duration

    def __str__(self):

        return "Song Name : {}\nArtist : {}\nAlbum : {}\nProduction Company : {}\nDuration : {}\n".format(self.name,self.artist
                                                                                                          ,self.album
                                                                                                          ,self.production_company
                                                                                                          ,self.duration)

class SongLibrary:

    def __init__(self):

        self.connect()

    #connect to the database
    def connect(self):

        #define the database
        self.connection = sqlite3.connect("SongLibrary.db")

        #define the cursor
        self.cursor = self.connection.cursor()

        query = "CREATE TABLE IF NOT EXISTS songs (Name TEXT,Artist TEXT,Album TEXT,Production Company TEXT,Duration TEXT)"

        #execute the query
        self.cursor.execute(query)

        #commit changes
        self.connection.commit()

    #disconnect from the database
    def disconnect(self):

        self.connection.close()

    def show_songs(self):

        query = "SELECT * FROM songs"

        #execute the query
        self.cursor.execute(query)

        #define the list of all songs
        songs = self.cursor.fetchall()

        if len(songs) == 0:

            print("There are no song in the library...")

        else:

            for i in songs:

                #create song object
                song = Song(i[0],i[1],i[2],i[3],i[4])
                print(song)

    def find_song(self,name):

        query = "SELECT * FROM songs WHERE Name = ?"

        #execute the query by using name
        self.cursor.execute(query,(name,))

        #define the list of the particular song
        songs = self.cursor.fetchall()

        if len(songs) == 0:

            print("There is no such song...")

        else:

            #create song object
            song = Song(songs[0][0],songs[0][1],songs[0][2],songs[0][3],songs[0][4])
            print(song)

    def add_song(self,song):

        query = "INSERT INTO songs VALUES(?,?,?,?,?)"

        #execute the query by using fields of song object
        self.cursor.execute(query, (song.name,song.artist,song.album,song.production_company,song.duration))

        #commit changes
        self.connection.commit()

    def delete_song(self,name):

        query = "DELETE FROM songs WHERE Name = ?"

        #execute the query by using name
        self.cursor.execute(query,(name,))

        #commit changes
        self.connection.commit()

    #calculate total duration of songs that is contained by the database
    def total_duration(self):

        total = datetime.timedelta()
        query = "SELECT * FROM songs"

        #execute the query
        self.cursor.execute(query)

        #define the list of all songs
        songs = self.cursor.fetchall()

        if len(songs) == 0:

            print("There is no song in the library...")

        else:

            for i in songs:

                #split the minutes and seconds part of the duration
                (min, sec) = i[4].split(":")

                #define the time that want to be add
                t = datetime.timedelta(minutes=int(min), seconds=int(sec))
                total += t

            return total


