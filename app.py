from flask import Flask, redirect, render_template, request
import sqlite3

app = Flask(__name__)

@app.route("/")
def index():
    conn = sqlite3.connect('fortnite_rankings.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM players ORDER BY rank ASC')
    players = cursor.fetchall()

    conn.close()
    return render_template("index.html", players=players)

if __name__ == "__main__":
    app.run(debug=True)

