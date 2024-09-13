import sqlite3

def create_database():
    conn = sqlite3.connect('fortnite_rankings.db')
    cursor = conn.cursor()

    cursor.execute('DROP TABLE IF EXISTS players')
    cursor.execute('DROP TABLE IF EXISTS placements')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS players (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            name TEXT DEFAULT NULL,
            date_of_birth DATE DEFAULT NULL,
            country TEXT DEFAULT NULL,
            total_earnings INTEGER NOT NULL,
            image_url TEXT DEFAULT 'https://www.esportsearnings.com/images/unknown_player.png'
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS placements (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            player_id INTEGER NOT NULL,
            date DATE NOT NULL,
            place INTEGER NOT NULL,
            tournament TEXT NOT NULL,
            region TEXT NOT NULL,
            earnings INTEGER NOT NULL,
            FOREIGN KEY (player_id) REFERENCES players(id)
        )
    ''')

    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_database()