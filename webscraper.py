import requests
import sqlite3
from bs4 import BeautifulSoup
import time

def main():
    base_url = "https://www.esportsearnings.com"
    players_list_url = f"{base_url}/games/534-fortnite/top-players"

    print(f"Fetching player list from: {players_list_url}")
    response = requests.get(players_list_url)

    if response.status_code == 200:
        print("Successfully retrieved player list.")
        soup = BeautifulSoup(response.text, 'html.parser')

        player_rows = soup.find_all('tr')

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


def scrape_player_details(player_url):
    print(f"Fetching player details from: {player_url}")
    response = requests.get(player_url)

    if response.status_code == 200:
        print("Successfully retrieved player details.")
        soup = BeautifulSoup(response.text, 'html.parser')

        name = soup.find(text="Name:").find_next().text.strip() if soup.find(text="Name:") else "Unknown"
        age = soup.find(text="Age:").find_next().text if soup.find(text="Age:") else None
        country = soup.find(class_="info_country").find('img')['alt'] if soup.find(class_="info_country") else "Unknown"
        total_earnings = soup.find(text="Total Prize Money Earned:").find_next().find(class_="info_prize_highlight").text
        total_earnings = int(float(total_earnings.replace('$', '').replace(',', ''))) if total_earnings else 0

        print(f"Scraped details - Name: {name}, Age: {age}, Country: {country}, Total Earnings: {total_earnings}")
        player_details = (name, age, country, total_earnings, player_url)
        return player_details
    else:
        print("Failed to retrieve player details.")
        return None


def insert_player_details(player_details, username):
    conn = sqlite3.connect('fortnite_rankings.db')
    cursor = conn.cursor()

    print(f"Inserting player details for username: {username}")
    cursor.execute('''
        INSERT INTO players (username, name, age, country, total_earnings, player_url)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', player_details)

    conn.commit()
    player_id = cursor.lastrowid
    conn.close()

    print(f"Player inserted with ID: {player_id}")
    return player_id


def scrape_placements(player_url, player_id):
    print(f"Fetching placements for player ID: {player_id} from: {player_url}")
    response = requests.get(player_url)

    if response.status_code == 200:
        print("Successfully retrieved placements.")
        soup = BeautifulSoup(response.text, 'html.parser')

        placements_table = soup.find_all('table')[0]

        placements = []

        for row in placements_table.find_all('tr'):
            columns = row.find_all('td')

            date = columns[1].text.strip()
            place = int(columns[2].text.strip().replace('th', '').replace('rd', '').replace('nd', '').replace('st', ''))
            tournament = columns[3].text.strip()
            earnings = int(float(columns[5].text.strip().replace('$', '').replace(',', '')))

            placements.append((player_id, date, place, tournament, earnings))

        print(f"Scraped {len(placements)} placements.")
        insert_placements(placements)
    else:
        print("Failed to retrieve placements.")


def insert_placements(placements):
    conn = sqlite3.connect('fortnite_rankings.db')
    cursor = conn.cursor()

    print(f"Inserting {len(placements)} placements into database.")
    cursor.executemany('''
        INSERT INTO placements (player_id, date, place, tournament, earnings)
        VALUES (?, ?, ?, ?, ?)
    ''', placements)

    conn.commit()
    conn.close()
    print("Placements inserted successfully.")


if __name__ == "__main__":
    main()