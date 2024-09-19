import pandas as pd


def read_shelters_from_csv(file_path):
    df = pd.read_csv(file_path)
    shelters = []

    for _, row in df.iterrows():
        shelter = {
            "shelter_number": row['shelter_number'],
            "address": row['address'],
            "capacity": row['capacity'],
            "longitude": row['longitude'],
            "latitude": row['latitude'],
            "utilities": {
                "Canned beans": row.get('Canned beans', 0),
                "Canned vegetables": row.get('Canned vegetables', 0),
                "Rice": row.get('Rice', 0),
                "Pasta": row.get('Pasta', 0),
                "Canned fruit": row.get('Canned fruit', 0),
                "soap": row.get('soap', 0),
                "Instant oatmeal": row.get('Instant oatmeal', 0),
                "tooth paste": row.get('tooth paste', 0),
                "toilet paper": row.get('toilet paper', 0),
                "Shelf-stable milk": row.get('Shelf-stable milk', 0),
            },
        }
        shelters.append(shelter)

    return shelters


def update_shelter(shelters, shelter_number, key, value):
    for shelter in shelters:
        if shelter['shelter_number'] == shelter_number:
            if key == 'capacity':
                shelter['capacity'] = value
            elif key == 'utilities':
                # Check if the value is a dict and update utilities
                if isinstance(value, dict):
                    shelter['utilities'].update(value)
                else:
                    print("Error: Utilities value must be a dictionary.")
            else:
                print("Error: Invalid key. Use 'capacity' or 'utilities'.")
            break
    else:
        print("Error: Shelter not found.")


def save_shelters_to_csv(shelters, file_path):
    flattened_data = []
    for shelter in shelters:
        flat_shelter = {
            "shelter_number": shelter['shelter_number'],
            "address": shelter['address'],
            "capacity": shelter['capacity'],
            "longitude": shelter['longitude'],
            "latitude": shelter['latitude'],
        }
        flat_shelter.update(shelter['utilities'])
        flattened_data.append(flat_shelter)

    df = pd.DataFrame(flattened_data)
    df.to_csv(file_path, index=False)


file_path = 'shelters_data.csv'
shelters_data = read_shelters_from_csv(file_path)
print(shelters_data)

# example
update_shelter(shelters_data, 1, 'capacity', 160)
update_shelter(shelters_data, 2, 'utilities', {'Canned beans': 220})

# update csv
save_shelters_to_csv(shelters_data, file_path)
