class Player:
    def __init__(self, data):
        self.name = data["name"]
        self.age = data["age"]
        self.position = data["position"]
        self.team = data["team"]

kevin = {
    "name": "Kevin Durant", 
    "age":34, 
    "position": "small forward", 
    "team": "Phoenix Suns" #hehe this must be a little old huh?
}
jayson = {
    "name": "Jayson Tatum", 
    "age":25, 
    "position": "small forward", 
    "team": "Boston Celtics" #no worries Jay, I'll spell your name right since Duke held that L
}
kyrie = {
    "name": "Kyrie Irving", 
    "age":30, 
    "position": "Point Guard", 
    "team": "Dallas Mavericks" #I got you too Kyrie!
}

# Create your Player instances here!
player_kevin = Player(kevin)
player_jayson = Player(jayson)
player_kyrie = Player(kyrie)

# ... (class definition and large list of players here)
players = [
    {
        "name": "Kevin Durant", 
        "age":35, 
        "position": "small forward", 
        "team": "Phoenix Suns"
    },
    {
        "name": "Jayson Tatum", 
        "age":25, 
        "position": "small forward", 
        "team": "Boston Celtics"
    },
    {
        "name": "Kyrie Irving", 
        "age":30, 
        "position": "Point Guard", 
        "team": "Dallas Mavericks"
    },
    {
        "name": "Damian Lillard", 
        "age":32, 
        "position": "Point Guard", 
        "team": "Portland Trailblazers"
    },
    {
        "name": "Joel Embiid", 
        "age": 29,
        "position": "Power Foward", 
        "team": "Philadelphia 76ers"
    }
]
new_team = []
# Write your for loop here to populate the new_team variable with Player objects.
for roster in players:
    new_player = Player(roster)
    new_team.append(new_player)

print(new_team)


