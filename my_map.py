import folium
from folium.plugins import MarkerCluster
import tempfile
import webbrowser
import pandas as pd

temp_user_loc = [32.064, 34.786]
csv_file_path = 'shelters.csv'

df = pd.read_csv(csv_file_path)

mapObj = folium.Map(temp_user_loc, zoom_start=17)
mCluster = MarkerCluster(name="Markers Demo").add_to(mapObj)

def add_shelters(mapObj, mCluster):
    for index, row in df.iterrows():
        location = row['Location'][1:-1].split(', ')  # Extract latitude and longitude
        folium.Marker(
            location=[float(location[0]), float(location[1])],
            tooltip=row['Name'],
            popup=f"We now have {row['Current Occupancy']}/{row['Capacity']}",
            icon=folium.Icon(icon="cloud"),
        ).add_to(mCluster)

    folium.LayerControl().add_to(mapObj)


def open_map_in_web(mapObj):
    with tempfile.NamedTemporaryFile(delete=False, suffix='.html') as temp_file:
        mapObj.save(temp_file.name)
        webbrowser.open('file://' + temp_file.name)

# Clean up the CSV file if necessary
# os.remove(csv_file_path)  # Uncomment if you want to delete the CSV file after use
