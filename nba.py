import requests
from bs4 import BeautifulSoup

# Send a GET request to the NBA.com player statistics page
response = requests.get("https://www.nba.com/stats/players")

# Parse the HTML content
soup = BeautifulSoup(response.content, "html.parser")

# Extract the player information
player_stats = []
for player_row in soup.select("table.stats-table tbody tr"):
    player_info = {
        "name": player_row.select_one("td.player-name").text.strip(),
        "points": player_row.select_one("td.points").text.strip(),
        "rebounds": player_row.select_one("td.rebounds").text.strip(),
        "assists": player_row.select_one("td.assists").text.strip(),
    }
    player_stats.append(player_info)

# Process and store the scraped data
for player in player_stats:
    print(player)
