import sqlite3

def create_database():
    conn = sqlite3.connect('fortnite_rankings.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS players (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            name TEXT,
            age INTEGER,
            country TEXT,
            region TEXT DEFAULT 'EU',
            image_url TEXT DEFAULT 'https://www.esportsearnings.com/images/unknown_player.png',
            total_earnings INTEGER DEFAULT 0,
            player_url TEXT UNIQUE
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS placements (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            player_id INTEGER,
            date TEXT,
            place INTEGER,
            tournament TEXT,
            earnings INTEGER,
            FOREIGN KEY (player_id) REFERENCES players(id)
        )
    ''')

    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_database()