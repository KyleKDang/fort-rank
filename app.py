from flask import Flask, redirect, render_template, request
import sqlite3

app = Flask(__name__)

@app.route("/")
def index():
    conn = sqlite3.connect('fortnite_rankings.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM players ORDER BY rank ASC')
    player_rows = cursor.fetchall()

    players = []

    for row in player_rows:
        player = {
            'id': row[0],
            'username': row[1],
            'name': row[2],
            'date_of_birth': row[3],
            'country': row[4],
            'total_earnings': row[5],
            'rank': row[6],
            'image_url': row[7]
        }
        players.append(player)

    conn.close()
    return render_template("index.html", players=players)

if __name__ == "__main__":
    app.run(debug=True)

