import sqlite3

def create_database():
    conn = sqlite3.connect('fortnite_rankings.db')
    cursor = conn.cursor()

    cursor.execute('DROP TABLE IF EXISTS players')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS players (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            name TEXT DEFAULT NULL,
            date_of_birth DATE DEFAULT NULL,
            country TEXT DEFAULT NULL,
            total_earnings INTEGER NOT NULL,
            rank INTEGER NOT NULL UNIQUE,
            image_url TEXT
        )
    ''')

    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_database()