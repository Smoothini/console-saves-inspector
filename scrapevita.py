import requests
from bs4 import BeautifulSoup
import json, re

# URL of the webpage
url = "https://renascene.com/psv/?target=list&sort=name&page=1"  # Replace with the actual URL

# Send a request to fetch the HTML content of the page
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# Prepare the data structure to hold the games
games_data = []

# Find the table with id "tabloid"
table = soup.find("table", {"id": "tabloid"})
rows = table.find_all("tr", class_="defRows")

for row in rows:
    cells = row.find_all("td")



    # Only process rows with enough cells (avoid rows with missing data)
    if len(cells) >= 6:
        # Extract the relevant data from each row
        game = {}

        game["psn_id"] = cells[1].get_text(strip=True)  # Extract PSN ID from 1st cell

        # Extract title from 3rd cell (<a href=...>)
        title = cells[2].get_text(strip=True)
        game["title"] = title

        # Extract region from 4th cell (img src)
        pattern = r"flags/([a-zA-Z]{2})\.gif"
        region_img = cells[3].find("img")
        #region = region_img["src"].split("/")[2].split(".")[0] if region_img else ""
        region = re.search(pattern, str(region_img)).group(1) if region_img else ""
        game["region"] = region

        # Extract PSN ID (5th cell)
        title_id = cells[4].get_text(strip=True)
        game["title_id"] = title_id

        box_id = cells[5].get_text(strip=True)  # Extract Box ID from 5th cell
        game["box_id"] = box_id

        # Extract category from 7th cell
        category = cells[6].get_text(strip=True)
        game["category"] = category

        # Extract release date from 8th cell
        release_date = cells[7].get_text(strip=True)
        game["release_date"] = release_date

        # Add the game data to the list
        games_data.append(game)

# Save the data to a JSON file
with open("datafiles/psv.json", "w", encoding="utf-8") as json_file:
    json.dump(games_data, json_file, ensure_ascii=False, indent=4)

print("Data has been saved to datafiles/psv.json")
