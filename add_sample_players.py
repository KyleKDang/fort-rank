import sqlite3

def add_sample_players():
    # Connect to the database
    conn = sqlite3.connect('fortnite_rankings.db')
    cursor = conn.cursor()

    # Define sample player data
    players = [
        ('PeterBot', 'Peter Kata', '2007-06-20', 'USA', 643724, 'https://yt3.googleusercontent.com/PRIImuXVV9d-RHTDMebJZwxJMi41_6TLckYBsRTmeNvrD8_oo1zVgDPkAq1wxeNI1Fh7unHDqJE=s900-c-k-c0x00ffffff-no-rj'),
        ('Queasy', 'Aleksa Cvetkovic', '2002-04-17', 'Serbia', 1195358, 'https://example.com/image2.jpg'),
        ('Bugha', 'Kyle Giersdor', '', 'UK', 3000, 'https://example.com/image3.jpg'),
        ('player4', 'Bob Brown', '2002-11-30', 'Australia', 6000, 'https://example.com/image4.jpg'),
    ]

    # Insert sample data into the players table
    try:
        cursor.executemany('''
            INSERT INTO players (username, name, date_of_birth, country, total_earnings, image_url)
            VALUES (?, ?, ?, ?, ?, ?)
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