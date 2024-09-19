import folium
from folium.plugins import MarkerCluster
import tempfile
import webbrowser
import pandas as pd

csv_file_path = 'shelters.csv'
df = pd.read_csv(csv_file_path)


def create_map(user_loc):
    mapObj = folium.Map(user_loc, zoom_start=12)
    mCluster = MarkerCluster(name="Shelters").add_to(mapObj)
    add_shelters(mapObj, mCluster)
    return mapObj


def add_shelters(mapObj, mCluster):
    for index, row in df.iterrows():
        location = row['Location'][1:-1].split(', ')  # Extract latitude and longitude
        folium.Marker(
            location=[float(location[0]), float(location[1])],
            tooltip=row['Name'],
            popup=f"We now have {row['Current Occupancy']}/{row['Capacity']}",
            icon=folium.Icon(icon="warning-sign"),
        ).add_to(mCluster)

    folium.LayerControl().add_to(mapObj)


def open_map_in_web(mapObj):
    with tempfile.NamedTemporaryFile(delete=False, suffix='.html') as temp_file:
        mapObj.save(temp_file.name)
        webbrowser.open('file://' + temp_file.name)
