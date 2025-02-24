from bs4 import BeautifulSoup
import pandas as pd
import requests
import time

all_teams = []  # List to store all teams

html = requests.get('https://www.baseball-reference.com/').text  # Getting the HTML from the website
soup = BeautifulSoup(html, 'lxml')
table = soup.find_all('table', class_='stats_table')[0] # 0 for AL, 1 for NL

#links = table[0].find_all('a')  # Finding all links in the table
links = table.find_all('a') 
links = [l.get("href") for l in links]  # Parsing through links
links = [l for l in links if '/teams/' in l]  # Filtering through links to only get  teams

team_urls = [f"https://baseball-reference.com{l}" for l in links]  # Formatting back to links
#https://www.baseball-reference.com/teams/NYY/2024.shtml
for team_url in team_urls:
    team_name = team_url.split("/")[-2]  # Isolating the names of the teams
    data = requests.get(team_url).text
    soup = BeautifulSoup(data, 'lxml')
    stats = soup.find_all('table', class_="stats_table")[0]  # Only want the first table

    if stats and stats.columns:
        stats.columns = stats.columns.droplevel()  # Formatting the stats

    team_data = pd.read_html(str(stats))[0]
    team_data["Team"] = team_name
    all_teams.append(team_data)  # Appending the data
    time.sleep(5)  # Making sure we don't get blocked from scraping by delaying each loop by 5 seconds

stat_df = pd.concat(all_teams)  # Concatenating all of the stats
stat_df.to_csv("stats.csv")  # Exporting to CSV
