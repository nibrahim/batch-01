# Flask application to serve lyrics
from flask import Flask, render_template

app = Flask(__name__)

import lyrics_test

@app.route("/lyrics/<int:aid>/song/<int:sid>")
def get_lyrics(aid, sid):
    song, lyrics = lyrics_test.get_lyrics(sid)
    artists = lyrics_test.get_all_artists()
    songs = lyrics_test.get_all_songs(aid)
    return render_template("lyrics.html",
                           artists=artists,
                           current=aid,
                           artist="", 
                           songs = songs,
                           song = song,
                           csong = sid,
                           lyrics = lyrics)


@app.route("/lyrics/<int:aid>")
def list_all_songs(aid):
    artists = lyrics_test.get_all_artists()
    songs = lyrics_test.get_all_songs(aid)
    return render_template("songlist.html", 
                           artists=artists,
                           current=aid,
                           artist="", 
                           songs=songs)

@app.route("/")
def hello():
    artists = lyrics_test.get_all_artists()
    return render_template("index.html", artists=artists)


if __name__ == "__main__":
    app.run(debug=True)





        
