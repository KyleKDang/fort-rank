from flask import Flask, redirect, render_template, request, session
from datetime import date
import sqlite3
from helpers import calculate_age, get_ordinal

app = Flask(__name__)
app.secret_key = 'familyfriendly'

current_selected = None

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        sort_by = request.form.get('sort_by')
        if sort_by == "rank":
            direction = "ASC"
        else:
            direction = "DESC"
        session['current_selected'] = (sort_by, direction)
    else:
        current_selected = session.get('current_selected')
        if current_selected:
            sort_by, direction = current_selected
        else:
            sort_by = "rank"
            direction = "ASC"

    with sqlite3.connect('fortnite_rankings.db') as conn:
        cursor = conn.cursor()

        query = f'SELECT * FROM players ORDER BY {sort_by} {direction}, total_earnings DESC'
        cursor.execute(query)
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
                'image': f"../static/images/{row[6]}",
                'rank': row[7]
            }
            players.append(player)

    return render_template("index.html", players=players, sort_by=sort_by)


@app.route('/player/<username>')
def player_details(username):
    player, placements = get_player_details(username)
    return render_template('player_details.html', player=player, placements=placements)


def get_player_details(username):
    with sqlite3.connect('fortnite_rankings.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM players WHERE username = ?', (username,))
        player_row = cursor.fetchone()
        if player_row is None:
            return None, []

        player = {
            "username": player_row[1],
            "name": player_row[2],
            "date_of_birth": player_row[3],
            "age": calculate_age(player_row[3]),
            "country": player_row[4],
            "total_earnings": f"${player_row[5]:,.2f}",
            "image": f"../static/images/{player_row[6]}",
        }

        cursor.execute('''
            SELECT * FROM placements WHERE player_name = ? ORDER BY placement_rank, earnings DESC, placement_date DESC
        ''', (username,))
        placement_rows = cursor.fetchall()

        placements = []
        for row in placement_rows:
            placements.append({
                "placement_date": row[2],
                "placement_rank": get_ordinal(row[3]),
                "tournament_name": row[4],
                "region": row[5],
                "earnings": f"${row[6]:,.2f}",
            })

        return player, placements


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

