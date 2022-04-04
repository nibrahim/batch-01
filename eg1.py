# Flask application to serve lyrics
from flask import Flask, render_template

app = Flask(__name__)

import lyrics_test

@app.route("/lyrics/<int:aid>")
def list_all_songs(aid):
    songs = lyrics_test.get_all_songs(aid)
    return render_template("songlist.html", 
                           artist="", 
                           songs=songs)

@app.route("/")
def hello():
    artists = lyrics_test.get_all_artists()
    return render_template("index.html", artists=artists)


if __name__ == "__main__":
    app.run(debug=True)





        
