import pandas
from geopy.geocoders import Nominatim


jerusalem_shelters = pandas.read_csv("EN_Shelters.csv", encoding="ISO-8859-1")
jerusalem_shelters = jerusalem_shelters.dropna()
jerusalem_shelters = jerusalem_shelters.drop(
    jerusalem_shelters[jerusalem_shelters["Shelter Number"].str.contains("Temporarily Inactive")].index)
jerusalem_shelters.reset_index(drop=True, inplace=True)
print(jerusalem_shelters)
j_shelters = jerusalem_shelters.copy()


# calling the Nominatim tool and create Nominatim class
loc = Nominatim(user_agent="Geopy Library")

addresses = jerusalem_shelters[["Address"]]
add_long_lat = {}
for address in range(len(addresses)):
    real_address = jerusalem_shelters['Address'].loc[jerusalem_shelters.index[address]]

    if real_address[0].isdigit():
        add = real_address.split(" ")
        add.append(add[0])
        add.pop(0)
        real_address = " ".join(add)
        # print(real_address)

    # # entering the location name
    getLoc = loc.geocode("Jerusalem " + real_address,timeout=100)
    if getLoc == None:
        index = jerusalem_shelters[(jerusalem_shelters.Address == real_address)].index
        jerusalem_shelters.drop(index)
        continue
    # jerusalem_shelters.insert()



    # #latitude and longitude dictionary!!!
    add_long_lat[real_address] = [getLoc.longitude,getLoc.latitude]



shelters_data = [
    {"shelter_number": 1, "address": "Hatikva Neighborhood Shelter, Tel Aviv", "capacity": 150, "longitude": 34.7736, "latitude": 32.0505},
    {"shelter_number": 2, "address": "Shelter 4, Tel Aviv", "capacity": 200, "longitude": 34.7760, "latitude": 32.0590},
    {"shelter_number": 3, "address": "Shelter 3, Tel Aviv", "capacity": 120, "longitude": 34.7701, "latitude": 32.0726},
    {"shelter_number": 4, "address": "Neve Sha'anan Shelter, Tel Aviv", "capacity": 180, "longitude": 34.7721, "latitude": 32.0416},
    {"shelter_number": 5, "address": "Shelter 5, Tel Aviv", "capacity": 100, "longitude": 34.7620, "latitude": 32.0548},
    {"shelter_number": 6, "address": "Shelter 6, Tel Aviv", "capacity": 250, "longitude": 34.7900, "latitude": 32.0830},
    {"shelter_number": 7, "address": "Yad Sarah Shelter, Tel Aviv", "capacity": 160, "longitude": 34.7808, "latitude": 32.0886},
    {"shelter_number": 8, "address": "Shelter 8, Tel Aviv", "capacity": 220, "longitude": 34.7723, "latitude": 32.0784},
    {"shelter_number": 9, "address": "Rothschild Shelter, Tel Aviv", "capacity": 130, "longitude": 34.7707, "latitude": 32.0670},
    {"shelter_number": 10, "address": "Hadar Yosef Shelter, Tel Aviv", "capacity": 140, "longitude": 34.7982, "latitude": 32.0781},
]
