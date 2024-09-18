import folium
from folium.plugins import MarkerCluster
import tempfile
import webbrowser
import pandas as pd
import os

# Temporary user location and shelter data
temp_user_loc = [32.064, 34.786]
temp_shelter_ds = [
    ["shelter1", [32.06418523361497, 34.78680114451362], 250, 20],
    ["shelter2", [32.071777, 34.775263], 300, 15],
    ["shelter3", [32.065444, 34.767834], 150, 10],
    ["shelter4", [32.073160, 34.794247], 200, 25],
    ["shelter5", [32.072073, 34.758155], 180, 12]
]

# Save shelter data to a CSV file
csv_file_path = 'shelters.csv'
df = pd.DataFrame(temp_shelter_ds, columns=["Name", "Location", "Capacity", "Current Occupancy"])
df.to_csv(csv_file_path, index=False)

# Read shelter data from the CSV file
df = pd.read_csv(csv_file_path)

# Create a map object
mapObj = folium.Map(temp_user_loc, zoom_start=17)
mCluster = MarkerCluster(name="Markers Demo").add_to(mapObj)

# Add markers for each shelter
for index, row in df.iterrows():
    location = row['Location'][1:-1].split(', ')  # Extract latitude and longitude
    folium.Marker(
        location=[float(location[0]), float(location[1])],
        tooltip=row['Name'],
        popup=f"We now have {row['Current Occupancy']}/{row['Capacity']}",
        icon=folium.Icon(icon="cloud"),
    ).add_to(mCluster)

folium.LayerControl().add_to(mapObj)

# Add a circle marker for the user's location
radius = 50
folium.CircleMarker(
    location=temp_user_loc,
    radius=radius,
    stroke=False,
    fill=False,
    fill_opacity=0.6,
    opacity=1,
    popup="{} pixels".format(radius),
).add_to(mapObj)

# Save the map to a temporary HTML file and open it
with tempfile.NamedTemporaryFile(delete=False, suffix='.html') as temp_file:
    mapObj.save(temp_file.name)
    webbrowser.open('file://' + temp_file.name)

# Clean up the CSV file if necessary
# os.remove(csv_file_path)  # Uncomment if you want to delete the CSV file after use
