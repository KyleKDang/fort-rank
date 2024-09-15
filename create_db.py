import sqlite3
from helpers import calculate_all_time, calculate_by_year

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
            all_time INTEGER,
            y_2024 INTEGER,
            y_2023 INTEGER,
            y_2022 INTEGER,
            y_2021 INTEGER,
            y_2020 INTEGER,
            y_2019 INTEGER
        )
    ''')

    # flags - https://www.alt-codes.net/flags
    players = [
        ('PeterBot', 'Peter Kata', '2007-06-20', 'United States 🇺🇸', 643724.17, 'peterbot.png'),
        ('Bugha', 'Kyle Giersdorf', '2002-12-30', 'United States 🇺🇸', 3740425.05, 'bugha.png'),
        ('mero', 'Matthew Faitel', '2004-09-18', 'Canada 🇨🇦', 1014450.0, 'mero.png'),
        ('TaySon', 'Tai Starcic', '2004-06-09', 'Slovenia 🇸🇮', 1209089.09, 'tayson.png'),
        ('Queasy', 'Aleksa Cvetkovic', '2002-04-17', 'Serbia 🇷🇸', 1195358.0, 'queasy.png'),
        ('Kami', 'Michal Kaminski', '2005-01-28', 'Poland 🇵🇱', 1483994.19, 'kami.png'),
        ('Setty', 'Iwa Zajac', '2003-09-08', 'Poland 🇵🇱', 1141351.81, 'setty.png'),
        ('Th0masHD', 'Thomas Hoxbro Davidsen', '2002-05-30', 'Denmark 🇩🇰', 1321326.84, 'th0mashd.png'),
        ('Pollo', 'Miguel Moreno', '2008-05-08', 'Mexico 🇲🇽', 480725.00, 'pollo.png'),
        ('Veno', 'Harry Pearson', '2004-11-26', 'United Kingdom 🇬🇧', 824425.96, 'veno.png'),
        ('EpikWhale', 'Shane Cotton', '2002-08-03', 'United States 🇺🇸', 1838487.32, 'epikwhale.png'),
        ('Malibuca', 'Danila Yakovenko', '2005-10-14', 'Russia 🇷🇺', 973063.64, 'malibuca.png'),
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
        ('PeterBot', '2024-07-28', 1, 'Fortnite Championship Series: Major 3 2024 - Grand Finals', 'NA', 70000.00),
        ('PeterBot', '2024-05-29', 1, 'Fortnite Championship Series: Chapter 3 Season 2 - Grand Finals', 'NAE', 65000.00),
        ('PeterBot', '2024-02-25', 2, 'Fortnite Championship Series: Major 1 2024 - Grand Finals', 'NA', 45000.00),
        ('PeterBot', '2024-08-11', 2, 'Esports World Cup 2024', 'Global', 40000.00),
        ('PeterBot', '2021-11-21', 4, 'Fortnite Championship Series: Grand Royale 2021', 'NAE', 28000.00),
        ('PeterBot', '2021-06-26', 8, 'Fortnite Championship Series: All-Star Showdown 2021 - Solo Final', 'NAE', 18000.00),
        ('PeterBot', '2022-08-14', 6, 'Fortnite Championship Series: Chapter 3 Season 3 - Grand Finals', 'NA', 16000.00),
        ('PeterBot', '2024-06-02', 2, 'DreamHack Dallas 2024', 'Global (Third-Party Event)', 11000.00),
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
        ('mero', '2023-10-15', 1, 'Fortnite Champion Series: Global Chamionship 2023', 'Global', 500000.00),
        ('mero', '2021-11-21', 1, 'Fortnite Championship Series: Grand Royale 2021', 'NAE', 95000.00),
        ('mero', '2022-03-06', 1, 'Fortnite Championship Series: Chapter 3 Season 1 - Grand Finals', 'NAE', 650000.00),
        ('mero', '2021-05-30', 1, 'Fortnite Championship Series: Chapter 2 Season 6 - Grand Finals', 'NAE', 500000.00),
        ('mero', '2022-08-14', 2, 'Fortnite Championship Series: Chapter 3 Season 3 - Grand Finals', 'NAE', 50000.00),
        ('mero', '2023-05-14', 2, 'Fortnite Championship Series: Major 2 - Grand Finals', 'NA', 47500.00),
        ('mero', '2021-10-31', 1, 'Fortnite Championship Series: Chapter 2 Season 8 - Grand Finals', 'NAE', 45000.00),
        ('mero', '2022-05-29', 3, 'Fortnite Championship Series: Chapter 3 Season 2 - Grand Finals', 'NAE', 35000.00),
        ('mero', '2020-11-01', 2, 'Fortnite Championship Series: Chapter 2 Season 4 - Grand Finals', 'NAE', 22000.00),
        ('mero', '2021-03-14', 4, 'Fortnite Championship Series: Chapter 2 Season 5 - Grand Finals', 'NAE', 20000.00),
        ('TaySon', '2021-11-21', 1, 'Fortnite Championship Series: Grand Royale 2021', 'EU', 200000.00),
        ('TaySon', '2021-06-26', 1, 'Fortnite Championship Series: All-Star Showdown 2021 - Solo Final', 'EU', 150000.00),
        ('TaySon', '2022-05-29', 2, 'Fortnite Championship Series: Chapter 3 Season 2 - Grand Finals', 'EU', 100000.00),
        ('TaySon', '2023-03-05', 1, 'Fortnite Championship Series: Major 1 2023 - Grand Finals', 'EU', 100000.00),
        ('TaySon', '2020-08-16', 1, 'Fortnite Championship Series: Chapter 2 Season 3 - Grand Finals', 'EU', 80000.00),
        ('TaySon', '2022-03-06', 3, 'Fortnite Championship Series: Chapter 3 Season 1 - Grand Finals', 'EU', 75000.00),
        ('TaySon', '2023-05-14', 2, 'Fortnite Championship Series: Major 2 2023 - Grand Finals', 'EU', 60000.00),
        ('TaySon', '2020-05-24', 5, 'Fortnite Championship Series Invitational - Grand Finals', 'EU', 50000.00),
        ('TaySon', '2021-05-30', 3, 'Fortnite Championship Series: Chapter 2 Season 6 - Grand Finals', 'EU', 45000.00),
        ('TaySon', '2020-11-01', 1, 'Fortnite Championship Series: Chapter 2 Season 4 - Grand Finals', 'EU', 37000.00),
        ('TaySon', '2021-09-05', 5, 'Fortnite Championship Series: Chapter 2 Season 7 - Grand Finals', 'EU', 35000.00),
        ('TaySon', '2024-06-02', 1, 'DreamHack Dallas 2024', 'Global (Third-Party Event)', 25000.00),
        ('TaySon', '2022-07-31', 6, 'Gamers8 2022', 'Global (Third-Party Event)', 20000.00),
        ('Queasy', '2022-03-06', 1, 'Fortnite Championship Series: Chapter 3 Season 1 - Grand Finals', 'EU', 150000.00),
        ('Queasy', '2024-09-08', 2, 'Fortnite Champion Series 2024 - Global Championship', 'Global', 150000.00),
        ('Queasy', '2021-05-30', 1, 'Fortnite Championship Series: Chapter 2 Season 6 - Grand Finals', 'EU', 100000.00),
        ('Queasy', '2023-05-14', 1, 'Fortnite Championship Series: Major 2 2023 - Grand Finals', 'EU', 100000.00),
        ('Queasy', '2021-11-21', 3, 'Fortnite Championship Series: Grand Royale 2021', 'EU', 90000.00),
        ('Queasy', '2022-08-14', 3, 'Fortnite Championship Series: Chapter 3 Season 3', 'EU', 75000.00),
        ('Queasy', '2022-11-13', 2, 'Fortnite Champions Series: Invitational 2022', 'EU', 70000.00),
        ('Queasy', '2024-02-25', 2, 'Fortnite Championship Series: Major 1 2024 - Grand Finals', 'EU', 60000.00),
        ('Queasy', '2023-03-05', 4, 'Fortnite Championship Series: Major 1 2023', 'EU', 40000.00),
        ('Queasy', '2020-04-19', 2, 'Fortnite Championship Series: Chapter 2 Season 2 - Grand Finals', 'EU', 30000.00),
        ('Queasy', '2022-07-31', 5, 'Gamers8 2022', 'Global (Third-Party Event)', 25000.00),
        ('Queasy', '2024-05-19', 7, 'Fortnite Championship Series: Major 2 2024 - Grand Finals', 'EU', 20000.00),
        ('Kami', '2023-10-15', 2, 'Fortnite Champion Series: Global Championship 2023', 'Global', 325000.00),
        ('Kami', '2023-07-09', 1, 'Gamers8 2023', 'Global (Third-Party Event)', 280000.00),
        ('Kami', '2021-11-21', 2, 'Fortnite Championship Series: Grand Royale 2021', 'EU', 150000.00),
        ('Kami', '2021-10-31', 1, 'Fortnite Championship Series: Chapter 2 Season 8 - Grand Finals', 'EU', 100000.00),
        ('Kami', '2021-11-13', 1, 'Fortnite Champions Series: Invitational 2022', 'Global', 100000.00),
        ('Kami', '2022-05-29', 5, 'Fortnite Championship Series: Chapter 3 Season 2 - Grand Finals', 'EU', 50000.00),
        ('Kami', '2024-05-19', 3, 'Fortnite Championship Series: Major 2 2024 - Grand Finals', 'EU', 50000.00),
        ('Kami', '2022-07-31', 3, 'Gamers8 2022', 'Global (Third-Party Event)', 50000.00),
        ('Kami', '2021-09-05', 4, 'Fortnite Championship Series: Chapter 2 Season 7 - Grand Finals', 'EU', 40000.00),
        ('Kami', '2023-08-13', 4, 'Fortnite Championship Series: Major 3 2023 - Grand Finals', 'EU', 40000.00),
        ('Kami', '2021-03-14', 6, 'Fortnite Championship Series: Chapter 2 Season 5 - Grand Finals', 'EU', 30000.00),
        ('Kami', '2023-05-14', 5, 'Fortnite Championship Series: Major 2 2023 - Grand Finals', 'EU', 30000.00),
        ('Kami', '2020-04-19', 5, 'Fortnite Championship Series: Chapter 2 Season 2 - Grand Finals', 'EU', 20000.00),
        ('Kami', '2020-11-01', 4, 'Fortnite Championship Series: Chapter 2 Season 4 - Grand Finals', 'EU', 20000.00),
        ('Setty', '2023-10-15', 2, 'Fortnite Champion Series: Global Championship 2023', 'Global', 325000.00),
        ('Setty', '2021-11-21', 2, 'Fortnite Championship Series: Grand Royale 2021', 'EU', 150000.00),
        ('Setty', '2021-10-31', 1, 'Fortnite Championship Series: Chapter 2 Season 8 - Grand Finals', 'EU', 100000.00),
        ('Setty', '2021-11-13', 1, 'Fortnite Champions Series: Invitational 2022', 'Global', 100000.00),
        ('Setty', '2022-05-29', 5, 'Fortnite Championship Series: Chapter 3 Season 2 - Grand Finals', 'EU', 50000.00),
        ('Setty', '2024-05-19', 3, 'Fortnite Championship Series: Major 2 2024 - Grand Finals', 'EU', 50000.00),
        ('Setty', '2022-07-31', 3, 'Gamers8 2022', 'Global (Third-Party Event)', 50000.00),
        ('Setty', '2021-09-05', 4, 'Fortnite Championship Series: Chapter 2 Season 7 - Grand Finals', 'EU', 40000.00),
        ('Setty', '2023-08-13', 4, 'Fortnite Championship Series: Major 3 2023 - Grand Finals', 'EU', 40000.00),
        ('Setty', '2021-03-14', 6, 'Fortnite Championship Series: Chapter 2 Season 5 - Grand Finals', 'EU', 30000.00),
        ('Setty', '2023-05-14', 5, 'Fortnite Championship Series: Major 2 2023 - Grand Finals', 'EU', 30000.00),
        ('Setty', '2022-06-19', 1, 'DreamHack Summer 2022', 'Global (Third-Party Event)', 12000.00),
        ('Th0masHD', '2024-09-08', 2, 'Fortnite Champion Series 2024 - Global Championship', 'Global', 150000.00),
        ('Th0masHD', '2021-11-21', 3, 'Fortnite Championship Series: Grand Royale 2021', 'EU', 90000.00),
        ('Th0masHD', '2022-03-06', 3, 'Fortnite Championship Series: Chapter 3 Season 1 - Grand Finals', 'EU', 75000.00),
        ('Th0masHD', '2022-05-29', 3, 'Fortnite Championship Series: Chapter 3 Season 2 - Grand Finals', 'EU', 75000.00),
        ('Th0masHD', '2021-03-14', 2, 'Fortnite Championship Series: Chapter 2 Season 5 - Grand Finals', 'EU', 70000.00),
        ('Th0masHD', '2020-05-24', 4, 'Fortnite Champion Series Invitational - Grand Finals', 'EU', 60000.00),
        ('Th0masHD', '2023-03-05', 2, 'Fortnite Championship Series: Major 1 2023 - Grand Finals', 'EU', 60000.00),
        ('Th0masHD', '2024-02-25', 2, 'Fortnite Championship Series: Major 1 2024 - Grand Finals', 'EU', 60000.00),
        ('Th0masHD', '2023-05-14', 3, 'Fortnite Championship Series: Major 2 2023 - Grand Finals', 'EU', 50000.00),
        ('Th0masHD', '2023-07-09', 5, 'Gamers8 2023', 'Global (Third-Party Event)', 50000.00),
        ('Th0masHD', '2022-11-13', 4, 'Fortnite Champions Series: Invitational 2022', 'Global', 45000.00),
        ('Th0masHD', '2021-05-30', 4, 'Fortnite Championship Series: Chapter 2 Season 6 - Grand Finals', 'EU', 40000.00),
        ('Th0masHD', '2022-08-14', 6, 'Fortnite Championship Series: Chapter 3 Season 3 - Grand Finals', 'EU', 40000.00),
        ('Th0masHD', '2020-11-01', 3, 'Fortnite Championship Series: Chapter 2 Season 4 - Grand Finals', 'EU', 25000.00),
        ('Th0masHD', '2023-06-04', 1, 'DreamHack Dallas 2023', 'Global (Third-Party Event)', 22500.00),
        ('Th0masHD', '2023-06-18', 1, 'DreamHack Summer 2023', 'Global (Third-Party Event)', 22500.00),
        ('Th0masHD', '2024-08-11', 3, 'Esports World Cup 2024', 'Global (Third-Party Event)', 20000.00),
        ('Th0masHD', '2024-05-19', 7, 'Fortnite Championship Series: Major 2 2024 - Grand Finals', 'EU', 20000.00),
        ('Th0masHD', '2022-07-31', 6, 'Gamers8 2022', 'Global (Third-Party Event)', 20000.00),
        ('Pollo', '2024-09-08', 1, 'Fortnite Champion Series 2024 - Global Championship', 'Global', 200000.00),
        ('Pollo', '2024-05-19', 1, 'Fortnite Championship Series: Major 2 2024 - Grand Finals', 'NA', 70000.00),
        ('Pollo', '2024-07-28', 1, 'Fortnite Championship Series: Major 3 2024 - Grand Finals', 'NA', 70000.00),
        ('Pollo', '2024-02-25', 2, 'Fortnite Championship Series: Major 1 2024 - Grand Finals', 'NA', 45000.00),
        ('Pollo', '2023-05-14', 3, 'Fortnite Championship Series: Major 2 2023 - Grand Finals', 'NA', 34000.00),
        ('Pollo', '2023-08-13', 5, 'Fortnite Championship Series: Major 3 2023 - Grand Finals', 'NA', 20000.00),
        ('Pollo', '2023-03-05', 2, 'Fortnite Championship Series: Major 1 2023 - Grand Finals', 'NAW', 12000.00),
        ('Veno', '2022-05-29', 1, 'Fortnite Championship Series: Chapter 3 Season 2 - Grand Finals', 'EU', 150000.00),
        ('Veno', '2021-06-26', 2, 'Fortnite Championship Series: All-Star Showdown 2021 - Solo Final', 'EU', 120000.00),
        ('Veno', '2023-05-14', 1, 'Fortnite Championship Series: Major 2 2023', 'EU', 100000.00),
        ('Veno', '2022-08-14', 3, 'Fortnite Championship Series: Chapter 3 Season 3 - Grand Finals', 'EU', 75000.00),
        ('Veno', '2022-11-13', 2, 'Fortnite Champions Series: Invitational 2022', 'Global', 70000.00),
        ('Veno', '2023-03-05', 4, 'Fortnite Championship Series: Major 1 2023 - Grand Finals', 'EU', 40000.00),
        ('Veno', '2021-09-05', 5, 'Fortnite Championship Series: Chapter 2 Season 7 - Grand Finals', 'EU', 35000.00),
        ('Veno', '2024-07-28', 4, 'Fortnite Championship Series: Major 3 2024 - Grand Finals', 'EU', 30000.00),
        ('EpikWhale', '2019-07-28', 3, 'Fortnite World Cup Finals 2019 - Solo', 'Global', 1200000.00),
        ('EpikWhale', '2022-07-31', 1, 'Gamers8 2022', 'Global (Third-Party Event)', 125000.00),
        ('EpikWhale', '2023-07-09', 6, 'Gamers8 2023', 'Global (Third-Party Event)', 40000.00),
        ('EpikWhale', '2021-11-21', 1, 'Fortnite Championship Series: Grand Royale 2021', 'NAW', 35000.00),
        ('EpikWhale', '2024-02-25', 4, 'Fortnite Championship Series: Major 1 2024 - Grand Finals', 'NA', 30000.00),
        ('EpikWhale', '2021-03-14', 1, 'Fortnite Championship Series: Chapter 2 Season 5 - Grand Finals', 'NAW', 25000.00),
        ('EpikWhale', '2021-05-30', 1, 'Fortnite Championship Series: Chapter 2 Season 6 - Grand Finals', 'NAW', 25000.00),
        ('EpikWhale', '2021-06-26', 4, 'Fortnite Championship Series: All-Star Showdown 2021 - Solo Final', 'NAW', 17500.00),
        ('EpikWhale', '2021-09-05', 1, 'Fortnite Championship Series: Chapter 2 Season 7 - Grand Finals', 'NAW', 16000.00),
        ('EpikWhale', '2020-11-01', 1, 'Fortnite Championship Series: Chapter 2 Season 4 - Grand Finals', 'NAW', 15000.00),
        ('EpikWhale', '2022-05-29', 1, 'Fortnite Championship Series: Chapter 3 Season 2 - Grand Finals', 'NAW', 14000.00),
        ('EpikWhale', '2021-10-31', 2, 'Fortnite Championship Series: Chapter 2 Season 8 - Grand Finals', 'NAW', 11500.00),
        ('EpikWhale', '2020-05-24', 6, 'Fortnite Championship Series Invitational - Grand Finals', 'NAW', 9000.00),
        ('EpikWhale', '2020-04-19', 1, 'Fortnite Championship Series: Chapter 2 Season 2 - Grand Finals', 'NAW', 8750.00),
        ('EpikWhale', '2019-12-08', 3, 'Fortnite Championship Series: Chapter 2 Season 1 - Grand Finals', 'NAW', 6000.00),
        ('EpikWhale', '2023-03-05', 6, 'Fortnite Championship Series: Major 1 2023 - Grand Finals', 'NAW', 5000.00),
        ('EpikWhale', '2019-09-22', 4, 'Fortnite Championship Series: Season X - Grand Finals', 'NAW', 44000.00),
        ('Malibuca', '2022-07-31', 1, 'Gamers8 2022', 'Global (Third-Party Event)', 125000.00),
        ('Malibuca', '2022-08-14', 2, 'Fortnite Championship Series: Chapter 3 Season 3 - Grand Finals', 'EU', 100000.00),
        ('Malibuca', '2024-02-25', 1, 'Fortnite Championship Series: Major 1 2024 - Grand Finals', 'EU', 85000.00),
        ('Malibuca', '2022-05-29', 4, 'Fortnite Championship Series: Chapter 3 Season 2 - Grand Finals', 'EU', 60000.00),
        ('Malibuca', '2023-03-05', 2, 'Fortnite Championship Series: Major 1 2023 - Grand Finals', 'EU', 60000.00),
        ('Malibuca', '2023-05-14', 3, 'Fortnite Championship Series: Major 2 2023 - Grand Finals', 'EU', 50000.00),
        ('Malibuca', '2023-07-09', 5, 'Gamers8 2023', 'Global (Third-Party Event)', 50000.00),
        ('Malibuca', '2024-07-28', 4, 'Fortnite Championship Series: Major 3 2024 - Grand Finals', 'EU', 40000.00),
        ('Malibuca', '2021-10-31', 7, 'Fortnite Championship Series: Chapter 2 Season 8 - Grand Finals', 'EU', 25000.00),
        ('Malibuca', '2024-05-19', 6, 'Fortnite Championship Series: Major 2 2024 - Grand Finals', 'EU', 25000.00),
        ('Malibuca', '2023-06-04', 1, 'DreamHack Dallas 2023', 'Global (Third-Party Event)', 22500.00),
        ('Malibuca', '2023-06-18', 1, 'DreamHack Summer 2023', 'Global (Third-Party Event)', 22500.00),
        ('Malibuca', '2024-08-11', 4, 'Esports World Cup 2024', 'Global (Third-Party Event)', 20000.00),
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
        y_2024 = calculate_by_year(placements, "2024")
        y_2023 = calculate_by_year(placements, "2023")
        y_2022 = calculate_by_year(placements, "2022")
        y_2021 = calculate_by_year(placements, "2021")
        y_2020 = calculate_by_year(placements, "2020")
        y_2019 = calculate_by_year(placements, "2019")
        cursor.execute('''
            UPDATE players
            SET all_time = ?,
                y_2024 = ?,
                y_2023 = ?,
                y_2022 = ?,
                y_2021 = ?,      
                y_2020 = ?,      
                y_2019 = ?       
            WHERE username = ?
        ''', (all_time, y_2024, y_2023, y_2022, y_2021, y_2020, y_2019, username))
        


    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_database()