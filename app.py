from flask import Flask, render_template, request, redirect, url_for, session
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_bcrypt import Bcrypt
import sqlite3

app = Flask(__name__)
app.secret_key = 'your_secret_key'
login_manager = LoginManager()
login_manager.init_app(app)
bcrypt = Bcrypt(app)

# User class for Flask-Login
class User(UserMixin):
    def __init__(self, id, username):
        self.id = id
        self.username = username

@login_manager.user_loader
def load_user(user_id):
    conn = sqlite3.connect('players.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id, username FROM users WHERE id = ?', (user_id,))
    user = cursor.fetchone()
    conn.close()
    if user:
        return User(id=user[0], username=user[1])
    return None

def get_players():
    conn = sqlite3.connect('players.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM players ORDER BY rank')
    players = cursor.fetchall()
    conn.close()
    return players

@app.route("/")
@login_required
def index():
    players = get_players()
    return render_template("index.html", players=players, user=current_user)

@app.route('/move/<int:player_id>/<direction>', methods=['POST'])
@login_required
def move_player(player_id, direction):
    conn = sqlite3.connect('players.db')
    cursor = conn.cursor()

    cursor.execute('SELECT rank FROM players WHERE id = ?', (player_id,))
    current_rank = cursor.fetchone()[0]

    if direction == 'up':
        new_rank = current_rank - 1
    elif direction == 'down':
        new_rank = current_rank + 1
    else:
        return redirect('/')

    if new_rank < 1:
        new_rank = 1

    cursor.execute('SELECT id FROM players WHERE rank = ?', (new_rank,))
    other_player_id = cursor.fetchone()

    if other_player_id:
        other_player_id = other_player_id[0]
        cursor.execute('UPDATE players SET rank = ? WHERE id = ?', (current_rank, other_player_id))

    cursor.execute('UPDATE players SET rank = ? WHERE id = ?', (new_rank, player_id))
    conn.commit()
    conn.close()

    return redirect('/')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        conn = sqlite3.connect('players.db')
        cursor = conn.cursor()
        cursor.execute('SELECT id, password FROM users WHERE username = ?', (username,))
        user = cursor.fetchone()
        conn.close()

        if user and bcrypt.check_password_hash(user[1], password):
            user_obj = User(id=user[0], username=username)
            login_user(user_obj)
            return redirect(url_for('index'))
        else:
            return "Invalid username or password", 401

    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

        conn = sqlite3.connect('players.db')
        cursor = conn.cursor()
        try:
            cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, hashed_password))
            conn.commit()
        except sqlite3.IntegrityError:
            conn.close()
            return "Username already exists", 400
        conn.close()

        return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
