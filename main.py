from my_map import create_map, open_map_in_web
from gui import run_gui
from constants import CITIES_COORDINATES

def main():
    selected_city = run_gui()
    if selected_city:
        user_loc = CITIES_COORDINATES[selected_city]
        mapObj = create_map(user_loc)
        open_map_in_web(mapObj)


main()

