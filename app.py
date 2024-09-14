from flask import Flask, redirect, render_template, request
from datetime import date
import sqlite3
from helpers import calculate_age

app = Flask(__name__)

@app.route("/")
def index():
    with sqlite3.connect('fortnite_rankings.db') as conn:
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM players ORDER BY id ASC')
        player_rows = cursor.fetchall()

        players = []
        rank = 0

        for row in player_rows:
            rank += 1
            player = {
                'rank': rank,
                'id': row[0],
                'username': row[1],
                'name': row[2],
                'age': calculate_age(row[3]),
                'country': row[4],
                'total_earnings': f"${row[5]:,.2f}",
                'image_url': row[7]
            }
            players.append(player)

    return render_template("index.html", players=players)

if __name__ == "__main__":
    app.run(debug=True, port=5001)

