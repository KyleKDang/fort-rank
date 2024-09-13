import requests
import sqlite3
from bs4 import BeautifulSoup
import time

def main():
    recreate_tables()

    base_url = "https://www.esportsearnings.com"
    players_list_url = f"{base_url}/games/534-fortnite/top-players"

    print(f"Fetching player list from: {players_list_url}")
    player_rows = fetch_data(players_list_url)

    if player_rows:
        for player_row in player_rows:
            player_link = player_row.find('a')
            if player_link:
                username = player_link.text.strip()
                player_url = base_url + player_link['href'].strip() + "/results-by-prize"

                print(f"Processing player: {username} with URL: {player_url}")

                player_details = scrape_player_details(player_url)
                if player_details:
                    player_id = insert_player_details(player_details, username)
                    print(f"Inserted player with ID: {player_id}")

                    scrape_placements(player_url, player_id)
                time.sleep(1)
    else:
        print("Failed to retrieve the player list.")

def fetch_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup.find_all('tr')
    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return None

def scrape_player_details(player_url):
    print(f"Fetching player details from: {player_url}")
    response = requests.get(player_url)

    if response.status_code == 200:
        print("Successfully retrieved player details.")
        soup = BeautifulSoup(response.text, 'html.parser')

        name_tag = soup.find(string="Name:")
        name = name_tag.find_next().text.strip() if name_tag else "Unknown"

        age_tag = soup.find(string="Age:")
        age = age_tag.find_next().text if age_tag else None

        country_tag = soup.find(class_="info_country")
        country = country_tag.find('img')['alt'] if country_tag else "Unknown"

        total_earnings_tag = soup.find(string="Total Prize Money Earned:")
        if total_earnings_tag:
            earnings_element = total_earnings_tag.find_next()
            if earnings_element:
                total_earnings = earnings_element.find(class_="info_prize_highlight").text
                total_earnings = int(float(total_earnings.replace('$', '').replace(',', '')))
            else:
                total_earnings = 0
        else:
            total_earnings = 0

        print(f"Scraped details - Name: {name}, Age: {age}, Country: {country}, Total Earnings: {total_earnings}")
        player_details = (name, age, country, total_earnings, player_url)
        return player_details
    else:
        print("Failed to retrieve player details.")
        return None

def insert_player_details(player_details, username):
    with sqlite3.connect('fortnite_rankings.db') as conn:
        cursor = conn.cursor()
        full_player_details = (username,) + player_details
        cursor.execute('''
            INSERT INTO players (username, name, age, country, total_earnings, player_url)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', full_player_details)
        conn.commit()
        player_id = cursor.lastrowid
        print(f"Player inserted with ID: {player_id}")
        return player_id

def scrape_placements(player_url, player_id):
    print(f"Fetching placements for player ID: {player_id} from: {player_url}")
    response = requests.get(player_url)

    if response.status_code == 200:
        print("Successfully retrieved placements.")
        soup = BeautifulSoup(response.text, 'html.parser')

        tables = soup.find_all('table')
        if not tables:
            print("No tables found on the page.")
            return
        
        placements_table = tables[0]

        placements = []

        for row in placements_table.find_all('tr'):
            if 'detail_list_header' in row.get('class', []):
                continue

            columns = row.find_all('td')

            print(f"Row: {row}")
            print(f"Columns: {columns}")

            if len(columns) < 6:
                print("Not enough columns found. Skipping row.")
                continue

            try:
                date = columns[1].text.strip()
                place = int(columns[2].text.strip().replace('th', '').replace('rd', '').replace('nd', '').replace('st', ''))
                tournament = columns[3].text.strip()
                earnings_text = columns[5].text.strip()
                earnings = 0
                if earnings_text and earnings_text != '-':
                    earnings = int(float(earnings_text.replace('$', '').replace(',', '')))

                placements.append((player_id, date, place, tournament, earnings))

            except (IndexError, ValueError) as e:
                print(f"Error processing row: {e}")
                print(f"Row content: {columns}")
                continue

        print(f"Scraped {len(placements)} placements.")
        insert_placements(placements)
    else:
        print("Failed to retrieve placements.")

def insert_placements(placements):
    with sqlite3.connect('fortnite_rankings.db') as conn:
        cursor = conn.cursor()
        cursor.executemany('''
            INSERT INTO placements (player_id, date, place, tournament, earnings)
            VALUES (?, ?, ?, ?, ?)
        ''', placements)
        conn.commit()
        print("Placements inserted successfully.")

def recreate_tables():
    with sqlite3.connect('fortnite_rankings.db') as conn:
        cursor = conn.cursor()
        cursor.execute('DROP TABLE IF EXISTS players')
        cursor.execute('DROP TABLE IF EXISTS placements')

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

if __name__ == "__main__":
    main()

