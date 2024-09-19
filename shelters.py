import pandas as pd

def read_shelters_from_csv(file_path):
    df = pd.read_csv(file_path)
    shelters = []

    for _, row in df.iterrows():
        shelter = {
            "shelter_number": row['shelter_number'],
            "address": row['address'],
            "capacity": row['capacity'],
            "current_population": row.get('current_population', 0),  # Initialize as 0 or appropriate default
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
            elif key == 'current_population':
                shelter['current_population'] = value
            elif key == 'residents':
                if isinstance(value, list) and all(isinstance(res, tuple) and len(res) == 2 for res in value):
                    shelter['residents'] = value
                else:
                    print("Error: Residents value must be a list of tuples.")
            elif key == 'utilities':
                if isinstance(value, dict):
                    shelter['utilities'].update(value)
                else:
                    print("Error: Utilities value must be a dictionary.")
            else:
                print("Error: Invalid key. Use 'capacity', 'current_population', 'residents', or 'utilities'.")
            break
    else:
        print("Error: Shelter not found.")

def get_population_amount(shelters, shelter_number):
    for shelter in shelters:
        if shelter['shelter_number'] == shelter_number:
            current_population = shelter['current_population']
            capacity = shelter['capacity']
            return current_population, capacity
    print("Error: Shelter not found.")
    return None, None

def save_shelters_to_csv(shelters, file_path):
    flattened_data = []
    for shelter in shelters:
        flat_shelter = {
            "shelter_number": shelter['shelter_number'],
            "address": shelter['address'],
            "capacity": shelter['capacity'],
            "current_population": shelter['current_population'],
            "longitude": shelter['longitude'],
            "latitude": shelter['latitude'],
        }
        flat_shelter.update(shelter['utilities'])

        flattened_data.append(flat_shelter)

    df = pd.DataFrame(flattened_data)
    df.to_csv(file_path, index=False)

# Example usage
file_path = 'shelters_data.csv'
shelters_data = read_shelters_from_csv(file_path)
print(shelters_data)

# Updating shelter example
update_shelter(shelters_data, 1, 'capacity', 160)
update_shelter(shelters_data, 2, 'utilities', {'Canned beans': 220})

# Update CSV
save_shelters_to_csv(shelters_data, file_path)


shelter_number = 1
current_population, capacity = get_population_amount(shelters_data, shelter_number)

if current_population is not None and capacity is not None:
    print(f"Shelter {shelter_number} currently has {current_population} people out of a capacity of {capacity}.")
