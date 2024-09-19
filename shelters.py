import pandas as pd
import random

shelters_data = [
    {
        "shelter_number": 1,
        "address": "Hatikva Neighborhood Shelter, Tel Aviv",
        "capacity": 160,
        "current_population": [
            ("shalom tubul", 123456789),
            ("ofir raz", 215395559)
        ],
        "longitude": 34.7736,
        "latitude": 32.0505,
        "utilities": {
            "Canned beans": 0,
            "Canned vegetables": 0,
            "Rice": 0,
            "Pasta": 0,
            "Canned fruit": 0,
            "soap": 0,
            "Instant oatmeal": 0,
            "tooth paste": 0,
            "toilet paper": 0,
            "Shelf-stable milk": 0,
        }
    },
    {
        "shelter_number": 2,
        "address": "Shelter 4, Tel Aviv",
        "capacity": 200,
        "current_population": [
            ("Jane Smith", 475888626)
        ],
        "longitude": 34.7760,
        "latitude": 32.0590,
        "utilities": {
            "Canned beans": 220,
            "Canned vegetables": 0,
            "Rice": 0,
            "Pasta": 0,
            "Canned fruit": 0,
            "soap": 0,
            "Instant oatmeal": 0,
            "tooth paste": 0,
            "toilet paper": 0,
            "Shelf-stable milk": 0,
        }
    },
    {
        "shelter_number": 3,
        "address": "Shelter 3, Tel Aviv",
        "capacity": 120,
        "current_population": [
            ("Jane Smith", 475888626)
        ],
        "longitude": 34.7701,
        "latitude": 32.0726,
        "utilities": {
            "Canned beans": 0,
            "Canned vegetables": 0,
            "Rice": 0,
            "Pasta": 0,
            "Canned fruit": 0,
            "soap": 0,
            "Instant oatmeal": 0,
            "tooth paste": 0,
            "toilet paper": 0,
            "Shelf-stable milk": 0,
        }
    },
    {
        "shelter_number": 4,
        "address": "Neve Sha'anan Shelter, Tel Aviv",
        "capacity": 180,
        "current_population": [
            ("Jane Smith", 475888626)
        ],
        "longitude": 34.7721,
        "latitude": 32.0416,
        "utilities": {
            "Canned beans": 0,
            "Canned vegetables": 0,
            "Rice": 0,
            "Pasta": 0,
            "Canned fruit": 0,
            "soap": 0,
            "Instant oatmeal": 0,
            "tooth paste": 0,
            "toilet paper": 0,
            "Shelf-stable milk": 0,
        }
    },
    {
        "shelter_number": 5,
        "address": "Shelter 5, Tel Aviv",
        "capacity": 100,
        "current_population": [
            ("Jane Smith", 475888626)
        ],
        "longitude": 34.7620,
        "latitude": 32.0548,
        "utilities": {
            "Canned beans": 0,
            "Canned vegetables": 0,
            "Rice": 0,
            "Pasta": 0,
            "Canned fruit": 0,
            "soap": 0,
            "Instant oatmeal": 0,
            "tooth paste": 0,
            "toilet paper": 0,
            "Shelf-stable milk": 0,
        }
    }
]


def update_shelter(shelters, shelter_number, key, value):
    for shelter in shelters:
        if shelter['shelter_number'] == shelter_number:
            if key == 'capacity':
                shelter['capacity'] = value
            elif key == 'current_population':
                if type(shelter['current_population']) == str:
                    print(shelter['current_population'])
                    shelter['current_population'] = [shelter['current_population']]
                    shelter['current_population'].append(value)
                else:
                    shelter['current_population'].append(value)

            elif key == 'utilities':
                if isinstance(value, dict):
                    shelter['utilities'].update(value)
            break
    else:
        print("Error: Shelter not found.")


def update_population(shelter_num, id_num, full_name):
        info = (full_name, id_num)
        update_shelter(shelters_data, shelter_num,"current_population", info)

# Updating shelter example
update_shelter(shelters_data, 1, 'capacity', 160)
update_shelter(shelters_data, 2, 'utilities', {'Canned beans': 220})
update_population(1, 123456789, "shalom tubul")
update_population(1, 215395559, "ofir raz")

print(shelters_data)


