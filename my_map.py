import folium
from folium.plugins import MarkerCluster
import tempfile
import webbrowser
import pandas as pd
import shelters
import data_handling
from data_handling import add_long_lat

csv_file_path = 'shelters.csv'
df = add_long_lat


def create_map(user_loc):
    mapObj = folium.Map(user_loc, zoom_start=12)
    mCluster = MarkerCluster(name="Shelters").add_to(mapObj)
    add_shelters(mapObj, mCluster)
    return mapObj


def add_shelters(mapObj, mCluster):
    for address in df:
        for loc in address:
            location = [loc[0], loc[1]] # Extract latitude and longitude
            folium.Marker(
                location=[float(location[1]), float(location[0])],
                tooltip=address,
                popup=f"We now have {0}/{200}",
                icon=folium.Icon(icon="warning-sign"),
            ).add_to(mCluster)

        folium.LayerControl().add_to(mapObj)


def open_map_in_web(mapObj):
    with tempfile.NamedTemporaryFile(delete=False, suffix='.html') as temp_file:
        mapObj.save(temp_file.name)
        webbrowser.open('file://' + temp_file.name)
