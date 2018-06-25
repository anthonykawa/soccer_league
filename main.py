import league_builder

PLAYERS = [
    {"name": "Frederick Gonzalez", "experienced": "YES", "guardians": "Fred and Wilma"},
    {"name": "Dederick Gallahan", "experienced": "NO", "guardians": "Your mom"}
]

print(league_builder.parse_players(PLAYERS))