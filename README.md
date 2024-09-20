# Fortnite Player Ranker
#### Video Demo:  https://youtu.be/XM6gIez1gbg
#### Description:

##### Overview
The Fortnite Player Ranker is a web application that allows users to track and rank Fortnite players based on their performances in competitive events. This tool provides insights into player rankings by factoring in multiple parameters such as placement, region, and event scope, and it calculates scores accordingly. It is designed to help players and fans get a deeper understanding of past and present competitive performance trends.

##### Functionality
The core functionality of the Fortnite Player Ranker lies in its ability to store and process placement data from various Fortnite competitive events. Users can view detailed player statistics, sort players based on multiple factors (like most earnings or best placements in a given year), and visualize their overall performance trends.

Players and placements can be inputted manually into the database, where key details are stored, such as:
- Player Name: The Fortnite player’s name.
- Player Image: The file name of the Fortnite player's headshot image.
- Event Date: The date of the competition.
- Tournament Name: The name of the competitive event.
- Placement: The player’s rank in the competition.
- Earnings: The prize money won by the player.
- Region: The region in which the event took place (North America, Europe, Global, etc.).

##### Project Structure
The project comprises several files, each responsible for different aspects of the application:

1. app.py: This file serves as the main application logic, utilizing Flask to handle requests and render web pages. It defines routes for viewing player data, adding new placements, and viewing detailed player profiles. It also handles communication with the database.
2. helpers.py: The helpers.py file contains utility functions, including the calculate_age() function, which computes a player’s age based on their birth date, and calculate_all_time() and calculate_by_year(), which calculate the player’s total score based on their placements and region multipliers.
3. create_db.py: This script is responsible for creating the database schema. It defines the structure of the database, including tables for storing player details and their placements.
4. layout.html: This HTML file defines the overall structure of the web pages, providing a consistent layout for all views. It includes the navigation menu and footer, and extends to other HTML files like index.html and player_details.html.
5. index.html: The home page of the application where users can see a list of all players and their rankings. It includes options for sorting players based on criteria such as user ranking, earnings, and yearly placements. The data is pulled from the database and presented in a tabular format.
6. player_details.html: This page displays the detailed information for a selected player, including their biographical information as well as past event placements. Users can explore how a player performs over time and sort placements by date.

##### Scoring System
The application uses a scoring system based on player placements and the region in which the event took place. Each region has a different multiplier, which affects the final score. The all-time multiplier and yearly multiplier for each region are presented as a pair (all-time / yearly):
- NA (North America): 1.0 / 1.0
- NAE (North America East): 1.0 / 1.0
- NAW (North America West): 0.5 / 0.5
- EU (Europe): 1.2 / 1.2
- Global: 2.0 / 3.0
- Global (Third-Party Event): 0.25 / 0.0

Players receive a base score depending on their placement in an event:
- 1st Place: 200 points (before multiplier)
- 2nd Place: 90 points (before multiplier)
- 3rd Place: 80 points (before multiplier)
- And so on, decreasing by 10 points for each subsequent place.
The player’s total score is calculated by summing up their scores from their best placements (7th/8th place or better), adjusted by the regional multiplier.

##### Sorting Features
The application provides robust sorting options to help users organize the data in meaningful ways:
- Players: Sort players by user ranking, most earnings, all-time placement score, and yearly placement scores (2020-2024)
- Placements: Sort placements by ranking, most earnings, most recent date, and oldest date.

##### Design Choices
A key design consideration was ensuring that the application remains flexible and easy to use. The use of Flask allows for a clear separation between the backend logic and frontend presentation. Each component of the application was built to handle specific tasks, promoting clean and maintainable code.

The database schema was structured to be both efficient and scalable, enabling the tracking of multiple players and hundreds of event placements. Additionally, the ability to calculate scores dynamically based on region and placement allows for adaptability, such as altering region multipliers without significant code changes.

##### Conclusion
The Fortnite Player Ranker is an effective tool for tracking the competitive performance of Fortnite players. With its combination of dynamic scoring, player and placement sorting, and detailed player profiles, it offers a valuable resource for fans, analysts, and players alike. The project demonstrates fundamental web development concepts such as database management, server-side scripting, and responsive design, all while applying these skills to a real-world gaming context.