
if __name__ == "__main__":

# Take players and divide into two separate dict(). One dict() will have experienced: YES, and the other will have experienced: NO
def parse_players(players):
    experienced_players = []
    inexperienced_players = []
    for player in players:
        if player['experienced'] == "YES":
            experienced_players.append(player)
        else:
            inexperienced_players.append(player)
    return {"experienced_players": experienced_players, "inexperienced_players": inexperienced_players}


# take in a dict() 
#   ( ex. {"name": "fred", "experienced": True, ""parents": "Ed and Wilma"} ) 
# and divide in 3 different teams, then return teams 
#   (ex. {"team": "Rangers", [{"name": "fred", "experienced": True, ""parents": "Ed and Wilma"}], })
def create_teams(players, teams):
    pass