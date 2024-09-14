import sqlite3

def create_database():
    conn = sqlite3.connect('fortnite_rankings.db')
    cursor = conn.cursor()

    cursor.execute('DROP TABLE IF EXISTS players')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS players (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            name TEXT NOT NULL,
            date_of_birth DATE NOT NULL,
            country TEXT NOT NULL,
            total_earnings REAL NOT NULL,
            image_url TEXT
        )
    ''')

    players = [
        ('PeterBot', 'Peter Kata', '2007-06-20', 'United States', 643724.17, 'static/images/peterbot.jpg'),
        ('Queasy', 'Aleksa Cvetkovic', '2002-04-17', 'Serbia', 1195358.0, 'static/images/queasy.jpg'),
        ('Bugha', 'Kyle Giersdorf', '2002-12-30', 'United States', 3740425.05, 'static/images/bugha.jpg'),
        ('Mero', 'Matthew Faitel', '2004-09-18', 'Canada', 1014450.0, 'static/images/mero.webp'),
    ]

    cursor.executemany('''
        INSERT INTO players (username, name, date_of_birth, country, total_earnings, image_url)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', players)

    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_database()