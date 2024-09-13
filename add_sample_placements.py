import sqlite3

def add_sample_players():
    # Connect to the database
    conn = sqlite3.connect('fortnite_rankings.db')
    cursor = conn.cursor()

    # Define sample player data
    players = [
        ('player1', 'John Doe', '2000-01-01', 'USA', 5000, 'https://example.com/image1.jpg'),
        ('player2', 'Jane Smith', '1999-05-15', 'Canada', 7500, 'https://example.com/image2.jpg'),
        ('player3', 'Alice Johnson', '2001-08-23', 'UK', 3000, 'https://example.com/image3.jpg'),
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