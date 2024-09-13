from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

@app.route("/")
def index():
    conn = sqlite3.connect('fortnite_rankings.db')
    cursor = conn.cursor()

    players = []

    cursor.execute('SELECT * FROM players')
    player_rows = cursor.fetchall()

    for row in player_rows:
        id = row[0]
        username = row[1]
        name = row[2]
        date_of_birth = row[3]
        country = row[4]
        total_earnings = row[5]
        image_url = row[6]
        players.append({"id":id,
                        "username":username,
                        "name":name,
                        "date_of_birth":date_of_birth,
                        "country":country,
                        "total_earnings":total_earnings,
                        "image_url":image_url})

    return render_template("index.html", players=players)

@app.route('/add_player', methods=['POST'])
def add_player():
    username = request.form['username']
    name = request.form.get('name')
    date_of_birth = request.form.get('date_of_birth')
    country = request.form.get('country')
    total_earnings = request.form['total_earnings']
    image_url = request.form.get('image_url', 'https://www.esportsearnings.com/images/unknown_player.png')

    try:
        conn = sqlite3.connect('fortnite_rankings.db')
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO players (username, name, date_of_birth, country, total_earnings, image_url)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (username, name, date_of_birth, country, total_earnings, image_url))

        conn.commit()

    except sqlite3.Error as e:
        print(f"An error occurred: {e}")

    finally:
        conn.close()

    return redirect("/")


if __name__ == '__main__':
    app.run(debug=True)