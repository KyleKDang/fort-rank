import sqlite3
from helpers import calculate_all_time

def create_database():
    conn = sqlite3.connect('fortnite_rankings.db')
    cursor = conn.cursor()

    cursor.execute('DROP TABLE IF EXISTS players')
    cursor.execute('DROP TABLE IF EXISTS placements')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS players (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            name TEXT NOT NULL,
            date_of_birth DATE NOT NULL,
            country TEXT NOT NULL,
            total_earnings REAL NOT NULL,
            image TEXT,
            rank INTEGER,
            all_time INTEGER
        )
    ''')

    players = [
        ('PeterBot', 'Peter Kata', '2007-06-20', 'United States', 643724.17, 'peterbot.png'),
        ('Bugha', 'Kyle Giersdorf', '2002-12-30', 'United States', 3740425.05, 'bugha.png'),
        ('Mero', 'Matthew Faitel', '2004-09-18', 'Canada', 1014450.0, 'mero.png'),
        ('Queasy', 'Aleksa Cvetkovic', '2002-04-17', 'Serbia', 1195358.0, 'queasy.png'),
    ]

    cursor.executemany('''
        INSERT INTO players (username, name, date_of_birth, country, total_earnings, image)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', players)

    cursor.execute('''
        UPDATE players SET rank = id
    ''')

    cursor.execute('''
            CREATE TABLE IF NOT EXISTS placements (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                player_name TEXT NOT NULL,
                placement_date DATE NOT NULL,
                placement_rank INTEGER NOT NULL,
                tournament_name TEXT NOT NULL,
                region TEXT NOT NULL,
                earnings REAL NOT NULL,
                FOREIGN KEY (player_name) REFERENCES players(username)
            )
        ''')
    
    placements = [
        ('PeterBot', '2024-09-08', 1, 'Fortnite Champion Series 2024 - Global Championship', 'Global', 200000.00),
        ('PeterBot', '2024-05-19', 1, 'Fortnite Championship Series: Major 2 2024 - Grand Finals', 'NA', 70000.00),
        ('PeterBot', '2024-07-28', 1, 'Fortnite Championship Series: Major 3 2024 - Grand Finals', 'NA', 700000.00),
        ('PeterBot', '2024-05-29', 1, 'Fortnite Championship Series: Chapter 3 Season 2 - Grand Finals', 'NAE', 65000.00),
        ('PeterBot', '2024-02-25', 2, 'Fortnite Championship Series: Major 1 2024 - Grand Finals', 'NA', 45000.00),
        ('PeterBot', '2024-08-11', 2, 'Esports World Cup 2024', 'Global', 40000.00),
        ('PeterBot', '2021-11-21', 4, 'Fortnite Championship Series: Grand Royale 2021', 'NAE', 28000.00),
        ('PeterBot', '2021-06-26', 8, 'Fortnite Championship Series: All-Star Showdown 2021 - Solo Final', 'NAE', 18000.00),
        ('PeterBot', '2022-08-14', 6, 'Fortnite Championship Series: Chapter 3 Season 3 - Grand Finals', 'NA', 16000.00),
        ('PeterBot', '2024-06-02', 2, 'DreamHack Dallas 2024', 'Global', 11000.00),
        ('Bugha', '2019-07-28', 1, 'Fortnite World Cup Finals 2019 - Solo', 'Global', 3000000.00),
        ('Bugha', '2021-11-21', 1, 'Fortnite Championship Series: Grand Royale 2021', 'NAE', 95000.00),
        ('Bugha', '2022-03-06', 1, 'Fortnite Championship Series: Chapter 3 Season 1 - Grand Finals', 'NAE', 65000.00),
        ('Bugha', '2022-08-14', 2, 'Fortnite Championship Series: Chapter 3 Season 3 - Grand Finals', 'NAE', 50000.00),
        ('Bugha', '2023-08-13', 2, 'Fortnite Championship Series: Major 3 2023 - Grand Finals', 'NA', 47500.00),
        ('Bugha', '2021-10-31', 1, 'Fortnite Championship Series: Chapter 2 Season 8 - Grand Finals', 'NAE', 45000.00),
        ('Bugha', '2022-05-29', 3, 'Fortnite Championship Series: Chapter 3 Season 2 - Grand Finals', 'NAE', 35000.00),
        ('Bugha', '2024-02-25', 3, 'Fortnite Championship Series: Major 1 2024 - Grand Finals', 'NA', 35000.00),
        ('Bugha', '2020-08-16', 4, 'Fortnite Championship Series: Chapter 2 Season 3 - Grand Finals', 'NAE', 25000.00),
        ('Bugha', '2023-05-14', 5, 'Fortnite Championship Series: Major 2 2023 - Grand Finals', 'NA', 20000.00),
        ('Bugha', '2021-03-14', 5, 'Fortnite Championship Series: Chapter 2 Season 5 - Grand Finals', 'NAE', 18000.00),
        ('Bugha', '2020-11-01', 3, 'Fortnite Championship Series: Chapter 2 Season 4 - Grand Finals', 'NAE', 15000.00),
        ('Bugha', '2024-07-28', 7, 'Fortnite Championship Series: Major 3 2024 - Grand Finals', 'NA', 15000.00),
        ('Bugha', '2020-04-19', 5, 'Fortnite Championship Series: Chapter 2 Season 2 - Grand Finals', 'NAE', 12500.00),
        ('Mero', '2023-10-15', 1, 'Fortnite Champion Series: Global Chamionship 2023', 'Global', 500000.00),
        ('Mero', '2021-11-21', 1, 'Fortnite Championship Series: Grand Royale 2021', 'NAE', 95000.00),
        ('Mero', '2022-03-06', 1, 'Fortnite Championship Series: Chapter 3 Season 1 - Grand Finals', 'NAE', 650000.00),
        ('Mero', '2021-05-30', 1, 'Fortnite Championship Series: Chapter 2 Season 6 - Grand Finals', 'NAE', 500000.00),
        ('Mero', '2022-08-14', 2, 'Fortnite Championship Series: Chapter 3 Season 3 - Grand Finals', 'NAE', 50000.00),
        ('Queasy', '2022-03-06', 1, 'Fortnite Championship Series: Chapter 3 Season 1 - Grand Finals', 'EU', 150000.00),
        ('Queasy', '2024-09-08', 2, 'Fortnite Champion Series 2024 - Global Championship', 'Global', 150000.00),
        ('Queasy', '2021-05-30', 1, 'Fortnite Championship Series: Chapter 2 Season 6 - Grand Finals', 'EU', 100000.00),
        ('Queasy', '2022-03-06', 1, 'Fortnite Championship Series: Major 2 2023 - Grand Finals', 'EU', 100000.00),
        ('Queasy', '2022-03-06', 3, 'Fortnite Championship Series: Grand Royale 2021', 'EU', 90000.00),
    ]

    cursor.executemany('''
        INSERT INTO placements (player_name, placement_date, placement_rank, tournament_name, region, earnings)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', placements)

    cursor.execute('SELECT * FROM players')
    player_rows = cursor.fetchall()
    for row in player_rows:
        username = row[1]
        cursor.execute('SELECT * FROM placements WHERE player_name = ?', (username,))
        placements = cursor.fetchall()
        all_time = calculate_all_time(placements)
        cursor.execute('''
            UPDATE players SET all_time = ? WHERE username = ?
        ''', (all_time, username))
        


    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_database()