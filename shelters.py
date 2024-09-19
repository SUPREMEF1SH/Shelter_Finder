import pandas as pd
import random

shelters_data = [
    {
        "shelter_number": 1,
        "address": "Hatikva Neighborhood Shelter, Tel Aviv",
        "capacity": 160,
        "current_population": [],
        "longitude": 34.7736,
        "latitude": 32.0505,
        "utilities": {
            "Canned beans": 160,            # 1 * 160
            "Canned vegetables": 160,       # 1 * 160
            "Rice": 80,                     # 0.5 * 160
            "Pasta": 80,                    # 0.5 * 160
            "Canned fruit": 80,             # 0.5 * 160
            "soap": 32,                     # 0.2 * 160
            "Instant oatmeal": 80,          # 0.5 * 160
            "tooth paste": 16,              # 0.1 * 160
            "toilet paper": 80,             # 0.5 * 160
            "Shelf-stable milk": 160,       # 1 * 160
        }
    },
    {
        "shelter_number": 2,
        "address": "Shelter 4, Tel Aviv",
        "capacity": 200,
        "current_population": [],
        "longitude": 34.7760,
        "latitude": 32.0590,
        "utilities": {
            "Canned beans": 200,            # 1 * 200
            "Canned vegetables": 200,       # 1 * 200
            "Rice": 100,                    # 0.5 * 200
            "Pasta": 100,                   # 0.5 * 200
            "Canned fruit": 100,            # 0.5 * 200
            "soap": 40,                     # 0.2 * 200
            "Instant oatmeal": 100,         # 0.5 * 200
            "tooth paste": 20,              # 0.1 * 200
            "toilet paper": 100,            # 0.5 * 200
            "Shelf-stable milk": 200,       # 1 * 200
        }
    },
    {
        "shelter_number": 3,
        "address": "Shelter 3, Tel Aviv",
        "capacity": 120,
        "current_population": [],
        "longitude": 34.7701,
        "latitude": 32.0726,
        "utilities": {
            "Canned beans": 120,            # 1 * 120
            "Canned vegetables": 120,       # 1 * 120
            "Rice": 60,                     # 0.5 * 120
            "Pasta": 60,                    # 0.5 * 120
            "Canned fruit": 60,             # 0.5 * 120
            "soap": 24,                     # 0.2 * 120
            "Instant oatmeal": 60,          # 0.5 * 120
            "tooth paste": 12,              # 0.1 * 120
            "toilet paper": 60,             # 0.5 * 120
            "Shelf-stable milk": 120,       # 1 * 120
        }
    },
    {
        "shelter_number": 4,
        "address": "Neve Sha'anan Shelter, Tel Aviv",
        "capacity": 180,
        "current_population": [],
        "longitude": 34.7721,
        "latitude": 32.0416,
        "utilities": {
            "Canned beans": 180,            # 1 * 180
            "Canned vegetables": 180,       # 1 * 180
            "Rice": 90,                     # 0.5 * 180
            "Pasta": 90,                    # 0.5 * 180
            "Canned fruit": 90,             # 0.5 * 180
            "soap": 36,                     # 0.2 * 180
            "Instant oatmeal": 90,          # 0.5 * 180
            "tooth paste": 18,              # 0.1 * 180
            "toilet paper": 90,             # 0.5 * 180
            "Shelf-stable milk": 180,       # 1 * 180
        }
    },
    {
        "shelter_number": 5,
        "address": "Shelter 5, Tel Aviv",
        "capacity": 100,
        "current_population": [],
        "longitude": 34.7620,
        "latitude": 32.0548,
        "utilities": {
            "Canned beans": 100,            # 1 * 100
            "Canned vegetables": 100,       # 1 * 100
            "Rice": 50,                     # 0.5 * 100
            "Pasta": 50,                    # 0.5 * 100
            "Canned fruit": 50,             # 0.5 * 100
            "soap": 20,                     # 0.2 * 100
            "Instant oatmeal": 50,          # 0.5 * 100
            "tooth paste": 10,              # 0.1 * 100
            "toilet paper": 50,             # 0.5 * 100
            "Shelf-stable milk": 100,       # 1 * 100
        }
    }
]


def update_shelter(shelters, shelter_number, key, value):
    for shelter in shelters:
        if shelter['shelter_number'] == shelter_number:
            if key == 'capacity':
                shelter['capacity'] = value
            elif key == 'current_population':
                shelter['current_population'].append(value)

            elif key == 'utilities':
                if isinstance(value, dict):
                    shelter['utilities'].update(value)
            break
    else:
        print("Error: Shelter not found.")


def update_population(shelter_num, id_num, full_name):
    info = (full_name, id_num)
    update_shelter(shelters_data, shelter_num, "current_population", info)


# Updating shelter example
update_shelter(shelters_data, 1, 'capacity', 160)
update_shelter(shelters_data, 2, 'utilities', {'Canned beans': 220})
update_population(1, 123456789, "shalom tubul")
update_population(1, 215395559, "ofir raz")
update_population(1,123456789,"Oded Yalo")

for shelter in shelters_data:
    print(shelter)
