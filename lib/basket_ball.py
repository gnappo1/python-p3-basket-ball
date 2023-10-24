def game_dict():
    return {
        "home": {
            "team_name": "Cleveland Cavaliers",
            "colors": ["Wine", "Gold"],
            "players": [
                {
                    "name": "Jarrett Allen",
                    "number": 31,
                    "position": "Center",
                    "points_per_game": 16.1,
                    "rebounds_per_game": 10.8,
                    "assists_per_game": 1.6,
                    "steals_per_game": 0.8,
                    "blocks_per_game": 1.3,
                    "career_points": 3945,
                    "age": 24,
                    "height_inches": 82,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Darius Garland",
                    "number": 10,
                    "position": "Point Guard",
                    "points_per_game": 21.7,
                    "rebounds_per_game": 3.3,
                    "assists_per_game": 8.6,
                    "steals_per_game": 1.3,
                    "blocks_per_game": 0.1,
                    "career_points": 3142,
                    "age": 22,
                    "height_inches": 73,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Evan Mobley",
                    "number": 4,
                    "position": "Center",
                    "points_per_game": 15.0,
                    "rebounds_per_game": 8.3,
                    "assists_per_game": 2.5,
                    "steals_per_game": 0.8,
                    "blocks_per_game": 1.7,
                    "career_points": 1034,
                    "age": 21,
                    "height_inches": 83,
                    "shoe_brand": "Adidas",
                },
                {
                    "name": "Kevin Love",
                    "number": 0,
                    "position": "Power Forward",
                    "points_per_game": 13.6,
                    "rebounds_per_game": 7.2,
                    "assists_per_game": 2.2,
                    "steals_per_game": 0.4,
                    "blocks_per_game": 0.2,
                    "career_points": 14305,
                    "age": 34,
                    "height_inches": 80,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Isaac Okoro",
                    "number": 35,
                    "position": "Small Forward",
                    "points_per_game": 8.8,
                    "rebounds_per_game": 3.0,
                    "assists_per_game": 1.8,
                    "steals_per_game": 0.8,
                    "blocks_per_game": 0.3,
                    "career_points": 1234,
                    "age": 21,
                    "height_inches": 77,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Ricky Rubio",
                    "number": 99,
                    "position": "Point Guard",
                    "points_per_game": 13.1,
                    "rebounds_per_game": 4.1,
                    "assists_per_game": 6.6,
                    "steals_per_game": 1.4,
                    "blocks_per_game": 0.2,
                    "career_points": 7399,
                    "age": 31,
                    "height_inches": 74,
                    "shoe_brand": "Adidas",
                },
            ],
        },
            
        "away": {
            "team_name": "Washington Wizards",
            "colors": ["Red", "White", "Navy Blue"],
            "players": [   
                {
                    "name": "Bradley Beal",
                    "number": 3,
                    "position": "Shooting Guard",
                    "points_per_game": 23.2,
                    "rebounds_per_game": 4.7,
                    "assists_per_game": 6.6,
                    "steals_per_game": 0.9,
                    "blocks_per_game": 0.4,
                    "career_points": 14231,
                    "age": 29,
                    "height_inches": 76,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Kyle Kuzma",
                    "number": 33,
                    "position": "Power Forward",
                    "points_per_game": 17.1,
                    "rebounds_per_game": 8.5,
                    "assists_per_game": 3.5,
                    "steals_per_game": 0.6,
                    "blocks_per_game": 0.9,
                    "career_points": 5336,
                    "age": 27,
                    "height_inches": 81,
                    "shoe_brand": "Puma",
                },
                {
                    "name": "Kentavious Caldwell-Pope",
                    "number": 1,
                    "position": "Shooting Guard",
                    "points_per_game": 13.2,
                    "rebounds_per_game": 3.4,
                    "assists_per_game": 1.9,
                    "steals_per_game": 1.1,
                    "blocks_per_game": 0.3,
                    "career_points": 7911,
                    "age": 29,
                    "height_inches": 77,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Davis Bertans",
                    "number": 42,
                    "position": "Power Forward",
                    "points_per_game": 5.6,
                    "rebounds_per_game": 2.1,
                    "assists_per_game": 0.6,
                    "steals_per_game": 0.3,
                    "blocks_per_game": 0.3,
                    "career_points": 3165,
                    "age": 29,
                    "height_inches": 82,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Kristaps Porzingis",
                    "number": 6,
                    "position": "Power Forward",
                    "points_per_game": 22.1,
                    "rebounds_per_game": 8.8,
                    "assists_per_game": 2.9,
                    "steals_per_game": 0.7,
                    "blocks_per_game": 1.5,
                    "career_points": 6371,
                    "age": 27,
                    "height_inches": 87,
                    "shoe_brand": "Adidas",
                },
                {
                    "name": "Rui Hachimura",
                    "number": 8,
                    "position": "Power Forward",
                    "points_per_game": 11.3,
                    "rebounds_per_game": 3.8,
                    "assists_per_game": 1.1,
                    "steals_per_game": 0.5,
                    "blocks_per_game": 0.2,
                    "career_points": 1913,
                    "age": 24,
                    "height_inches": 80,
                    "shoe_brand": "Jordan",
                },
            ]
        }
    }

#! Helpers
def all_players():
    players_dict = {}
    for team in game_dict():
        for player in game_dict()[team]["players"]:
            player_copy = player.copy()
            player_copy.pop("name", None)
            players_dict[player["name"]] = player_copy
    return players_dict

# print(all_players())
#! Deliverables
def num_points_per_game(player_name):
    # if player_name in all_players():
    #     return all_players()[player_name]["points_per_game"]
    # else:
    #     return "The player is not among the roster"
    try:
        return all_players().get(player_name).get("points_per_game", "Did not score a thing!")
    except Exception as e:
        return "The player is not among the roster"

# print(num_points_per_game("Jarrett AllenZ"))
def player_age(player_name):
    try:
        return all_players().get(player_name, "The player is not among the roster").get("age", "No one told us about their age yet!")
    except Exception as e:
        return "The player's age is undisclosed or player not in roster"

# print(player_age("Jarrett Allen"))

def team_colors(team_name):
    # for team in game_dict(): # "home", "away"
    #     # import ipdb; ipdb.set_trace()
    #     if game_dict()[team]["team_name"] == team_name:
    #         return game_dict()[team]["colors"]
    # return "Breaking code now muahahahaha!"
    obj = game_dict()
    return next(
        (
            obj[team]["colors"]
            for team in obj
            if obj[team]["team_name"] == team_name
        ),
        "Breaking code now muahahahaha!",
    )
# print(team_colors("Washington Wizards"))

def team_names():
    return [team.get("team_name") for team in game_dict().values()]
# print(team_names())

def player_numbers(team_name):
    # numbers_list = []
    obj = game_dict()
    # for team in obj:
    #     if obj[team]["team_name"] == team_name:
    #         # for player in obj[team]["players"]:
    #         #     numbers_list.append(player["number"])
    #         return [player["number"] for player in obj[team]["players"]]
    # return "The team does not exist!"
    return next(
        (
            [player["number"] for player in obj[team]["players"]]
            for team in obj
            if obj[team]["team_name"] == team_name
        ),
        "The team does not exist!",
    )

# print(player_numbers("Washington WizardsS"))

def player_stats(player_name):
    player = all_players().get(player_name, "The player is not in any of our rosters")
    if type(player) is not str:
        player["name"] = player_name 
    return player

def create_shoe_brand_rebounds_list(brand):
    rebounds_list = []
    for team_stats in game_dict().values():
        for player in team_stats["players"]:
            if (player["shoe_brand"].lower() == brand.lower()):
                rebounds_list.append(player["rebounds_per_game"])
    return rebounds_list
# print(player_stats("Jarrett Allen"))

def average_rebounds_by_shoe_brand():
    # possible_brands = []
    # for player, stats in all_players().items():
    #     if stats["shoe_brand"] not in possible_brands:
    #         possible_brands.append(stats["shoe_brand"])
    # all_brands = {}
    # for brand in possible_brands:
    #     all_brands[brand] = create_shoe_brand_rebounds_list(brand)
    # for brand, rebound_list in all_brands.items():
    #     avg_rebounds = round(sum(rebound_list) / len(rebound_list), 2)
    #     print(f"{brand}: {avg_rebounds:.2f}")
    shoes_stats = {}
    for _, stats in all_players().items():
        brand = stats["shoe_brand"]
        rebounds = stats["rebounds_per_game"]
        if brand in shoes_stats:
            shoes_stats[brand].append(rebounds)
        else:
            shoes_stats[brand] = [rebounds]
    for brand in shoes_stats:
        #! Alternative: use reduce from functools or mean from statistics
        avg = sum(shoes_stats[brand]) / len(shoes_stats[brand])
        print(f"{brand}:", "{0:.2f}".format(avg))
    
    # print(all_brands)
average_rebounds_by_shoe_brand()