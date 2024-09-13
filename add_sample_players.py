import sqlite3

def add_sample_players():
    # Connect to the database
    conn = sqlite3.connect('fortnite_rankings.db')
    cursor = conn.cursor()

    # Define sample player data
    players = [
        ('PeterBot', 'Peter Kata', '2007-06-20', 'United States', 643724),
        ('Queasy', 'Aleksa Cvetkovic', '2002-04-17', 'Serbia', 1195358),
        ('Bugha', 'Kyle Giersdorf', '2002-12-30', 'United States', 3740425),
        ('Mero', 'Matthew Faitel', '2004-09-18', 'Canada', 1014450),
    ]

    # Insert sample data into the players table
    try:
        cursor.executemany('''
            INSERT INTO players (username, name, date_of_birth, country, total_earnings)
            VALUES (?, ?, ?, ?, ?)
        ''', players)

        # Commit changes
        conn.commit()
        print("Sample players added successfully!")

    except sqlite3.Error as e:
        print(f"An error occurred: {e}")

    finally:
        conn.close()

if __name__ == '__main__':
    add_sample_players()