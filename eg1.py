# Flask application to serve lyrics
from flask import Flask

app = Flask(__name__)

import lyrics_test

@app.route("/lyrics")
def list_all_songs(artist="A"):
    songs = lyrics_test.get_all_songs(artist)
    output = []
    output.append(f"<h1>{artist}</h1>")
    output.append("<ul>")
    for i in songs:
        output.append(f"<li>{i[0]}</li>")
    output.append("</ul>")
    return "".join(output)

@app.route("/")
def hello():
    return "<h1>Hello. World!</h1>"

if __name__ == "__main__":
    app.run(debug=True)
