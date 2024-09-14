from flask import Flask, redirect, render_template, request
from datetime import date
import sqlite3
from helpers import calculate_age

app = Flask(__name__)

@app.route("/")
def index():
    with sqlite3.connect('fortnite_rankings.db') as conn:
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM players ORDER BY rank ASC')
        player_rows = cursor.fetchall()

        players = []
        position = 0

        for row in player_rows:
            position += 1
            player = {
                'position': position,
                'id': row[0],
                'username': row[1],
                'name': row[2],
                'age': calculate_age(row[3]),
                'country': row[4],
                'total_earnings': f"${row[5]:,.2f}",
                'image_url': row[6],
                'rank': row[7]
            }
            players.append(player)

    return render_template("index.html", players=players)


def swap_ranks(player1_id, player2_id):
    with sqlite3.connect('fortnite_rankings.db') as conn:
        cursor = conn.cursor()

        cursor.execute('SELECT rank FROM players WHERE id = ?', (player1_id,))
        player1_rank = cursor.fetchone()[0]

        cursor.execute('SELECT rank FROM players WHERE id = ?', (player2_id,))
        player2_rank = cursor.fetchone()[0]

        cursor.execute('UPDATE players SET rank = ? WHERE id = ?', (player2_rank, player1_id))
        cursor.execute('UPDATE players SET rank = ? WHERE id = ?', (player1_rank, player2_id))

        conn.commit()


@app.route("/move_up/<int:rank>", methods=["POST"])
def move_up(rank):
    with sqlite3.connect('fortnite_rankings.db') as conn:
        cursor = conn.cursor()

        cursor.execute('SELECT id FROM players WHERE rank = ?', (rank,))
        player_id = cursor.fetchone()[0]

        if rank > 1:
            cursor.execute('SELECT id FROM players WHERE rank = ?', (rank - 1,))
            player_above_id = cursor.fetchone()[0]

            swap_ranks(player_id, player_above_id)

    return redirect("/")


@app.route("/move_down/<int:rank>", methods=["POST"])
def move_down(rank):
    with sqlite3.connect('fortnite_rankings.db') as conn:
        cursor = conn.cursor()

        cursor.execute('SELECT id FROM players WHERE rank = ?', (rank,))
        player_id = cursor.fetchone()[0]

        cursor.execute('SELECT MAX(rank) FROM players')
        max_rank = cursor.fetchone()[0]

        if rank < max_rank:
            cursor.execute('SELECT id FROM players WHERE rank = ?', (rank + 1,))
            player_below_id = cursor.fetchone()[0]

            swap_ranks(player_id, player_below_id)

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True, port=5001)

