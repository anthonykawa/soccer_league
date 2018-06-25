
import csv

# Read csv file and return a dict of the player dictionaries in a list
def csv_to_players(file):
    results = []
    with open(file) as file:
        for row in csv.DictReader(file):
            results.append(row)
    return results

# Take players and divide into two separate dict(). One dict() will have experienced: YES, and the other will have experienced: NO
def create_player(team_name):
    return {"team_name": team_name, "avg_height": 0, "players": []}

# assemble the players into a Dict unfrt players, and team name under team_name, and return that Dict
def create_teams(players, teams):
    while players:
        for team in teams:
            team['players'].append(players.pop(0))

# Create teams.txt file with the teams listed in format below
#   Rangers
#   Fred Durst, YES, Susan and Doyle
#   Susan Carlyle, NO, Dorothy
def create_teams_file(teams):
    with open('teams.txt', 'w') as file:
        for team in teams:
            file.write('-'*30 + "\n")
            file.write(" "*10 + team['team_name'] + "\n")
            file.write('-'*30 + "\n")
            for player in team['players']:
                file.write(player['Name'] + ", " + player['Soccer Experience'] + ", " + player['Guardian Name(s)'] + "\n")
            file.write("\n\n")

# Create welcome letter files where filename is first and lastname of the student in lowercase (ex fred_durst.txt) 
# and the contents include Dear {Guardian Name} and also include team name, name of the player and the date and time
# they will start practice within the body of the message
def create_welcome_letters(teams):
    for team in teams:
        team_name = team['team_name']
        for player in team['players']:
            names = player['Name'].split()
            with open(names[0].lower() + "_" + names[1].lower() + ".txt", "w") as File:
                File.write("Dear " + player['Guardian Name(s)'] + ",\n\n")
                File.write("First, I would like to welcome " + names[0] + " " + names[1] + " to the " + team_name + ".")
                File.write(" The first practice will be starting on July 1st\nat 6:30 PM, so please make sure you arrive on time, ")
                File.write("and have all the necessary paperwork filled out before\nthen.")
                File.write("\n\n")
                File.write("Thank you,\n")
                File.write("Coach Carter")         

# Update the average height within the teams dictionary 
def update_avg_height(teams):
    for team in teams:
        total_height = 0
        for player in team['players']:
            total_height += int(player['Height (inches)'])
        team.update({'avg_height': total_height/len(team['players'])})


def run():
    TEAMS = ["Raptors", "Dragons", "Sharks"]
    CSV_FILE = 'soccer_players.csv'
    teams = []

    for team in TEAMS:
        teams.append(create_player(team))

    # get players from CSV file and assign them to players variable
    players = csv_to_players(CSV_FILE)

    # Separate the experienced players from the inexperienced players
    exp_players = []
    inexp_players = []
    for player in players:
        if player["Soccer Experience"] == "YES":
            exp_players.append(player)
        else:
            inexp_players.append(player)
    # create the teams, and add the players to the teams so there are an equal number of players on the teams
    # Also distribute the experienced and inexperienced players evenly
    create_teams(exp_players, teams)
    create_teams(inexp_players, teams)

    update_avg_height(teams)

    create_teams_file(teams)

    create_welcome_letters(teams)


if __name__ == "__main__":
    run()