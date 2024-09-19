import pandas
from geopy.geocoders import Nominatim


jerusalem_shelters = pandas.read_csv("EN_Shelters.csv", encoding="ISO-8859-1")
jerusalem_shelters = jerusalem_shelters.dropna()
jerusalem_shelters = jerusalem_shelters.drop(
    jerusalem_shelters[jerusalem_shelters["Shelter Number"].str.contains("Temporarily Inactive")].index)
jerusalem_shelters.reset_index(drop=True, inplace=True)
print(jerusalem_shelters)



# calling the Nominatim tool and create Nominatim class
loc = Nominatim(user_agent="Geopy Library")

addresses = jerusalem_shelters[["Address"]]
count = 0
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
        continue

    # # printing address
    # print(getLoc.address)
    count += 1

    # #latitude and longitude
    add_long_lat[real_address] = [getLoc.longitude,getLoc.latitude]
    # print("Latitude = ", getLoc.latitude, "\n")
    # print("Longitude = ", getLoc.longitude)




