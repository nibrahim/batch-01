import sys

import psycopg2

def get_all_songs(artist):
    conn = psycopg2.connect("dbname=lyrics")
    curs = conn.cursor()
    curs.execute("SELECT song.name FROM song, artist WHERE artist.id = song.artist AND artist.name=%s", (artist,))
    songs = curs.fetchall()
    return songs

def cmd():
    try:
        artist = sys.argv[1]
        print(artist)
        songs = get_all_songs(artist)
        for i in songs:
            print ("   ", (i[0]))

    except IndexError:
        print ("Usage : lyrics_test.py artist")

def main():
    cmd()

if __name__ == "__main__":
    main()
