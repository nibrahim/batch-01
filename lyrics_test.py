import sys

import psycopg2


def get_lyrics(sid):
    conn = psycopg2.connect("dbname=lyrics")
    curs = conn.cursor()
    curs.execute("SELECT song.name, song.lyrics FROM song WHERE song.id = %s", (sid,))
    return curs.fetchone()

def get_all_artists():
    conn = psycopg2.connect("dbname=lyrics")
    curs = conn.cursor()
    curs.execute("SELECT artist.id, artist.name FROM artist")
    return curs.fetchall()

def get_all_songs(artist_id):
    conn = psycopg2.connect("dbname=lyrics")
    curs = conn.cursor()
    curs.execute("SELECT song.id, song.name FROM song, artist WHERE artist.id = song.artist AND artist.id=%s", (artist_id,))
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
