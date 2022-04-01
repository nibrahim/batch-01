# Flask application to serve lyrics
from flask import Flask, render_template

app = Flask(__name__)

import lyrics_test

@app.route("/lyrics")
def list_all_songs(artist="A"):
    songs = lyrics_test.get_all_songs(artist)
    return render_template("songlist.html", artist=artist, songs=songs)

@app.route("/")
def hello():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)


