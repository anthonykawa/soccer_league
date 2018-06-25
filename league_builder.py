
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

def create_teams_file(teams):
    with open('teams.txt', 'w') as file:
        for team in teams:
            file.write('-'*30 + "\n")
            file.write(" "*10 + team['team_name'] + "\n")
            file.write('-'*30 + "\n")
            for player in team['players']:
                file.write(player['Name'] + ", " + player['Soccer Experience'] + ", " + player['Guardian Name(s)'] + "\n")
            file.write("\n")
            file.write("\n")

def create_welcome_letters(teams):
    for team in teams:
        team_name = team['team_name']
        for player in team['players']:
            names = player['Name'].split()
            with open(names[0].lower() + "_" + names[1].lower() + ".txt", "w"):
                pass            

# Update the average height within the teams dictionary 
def update_avg_height(teams):
    for team in teams:
        total_height = 0
        for player in team['players']:
            total_height += int(player['Height (inches)'])
        team.update({'avg_height': total_height/len(team['players'])})

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
    create_teams(inexp_players, teams)
    update_avg_height(teams)
    create_teams_file(teams)
    create_welcome_letters(teams)


if __name__ == "__main__":
    run()