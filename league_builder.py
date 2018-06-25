
import csv

TEAMS = ["Raptors", "Dragons", "Sharks"]
CSV_FILE = 'soccer_players.csv'

# Will take in a csv file and return a dict of the player details in a list format
def csv_to_players(file):
    results = []
    with open(file) as file:
        for row in csv.DictReader(file):
            results.append(row)
    return results

# Take players and divide into two separate dict(). One dict() will have experienced: YES, and the other will have experienced: NO
def create_player(team_name):
    return {"team_name": team_name, "avg_height": 0, "players": []}


def create_teams(players, teams):
    while players:
        for team in teams:
            team['players'].append(players.pop(0))

# take in players and write to file the teams and their respective players
def players_to_file(players):
    pass

def run():

    teams = []
    for team in TEAMS:
        teams.append(create_player(team))

    # get players from CSV file and assign them to players
    players = csv_to_players(CSV_FILE)
    # Separate the experienced players from the inexperienced players
    exp_players = []
    inexp_players = []
    for player in players:
        if player["Soccer Experience"] == "YES":
            exp_players.append(player)
        else:
            inexp_players.append(player)
    create_teams(exp_players, teams)
    create_teams(inexp_players, teams)\


if __name__ == "__main__":
    run()