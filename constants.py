# Constants module

# Screen dimensions
SCREEN_WIDTH, SCREEN_HEIGHT = 600, 400

# Color definitions
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
BLUE = (0, 0, 255)

CITIES_COORDINATES = {
    "Tel Aviv": (32.0788, 34.7749),
    "Jerusalem": (31.7725, 35.2183),
    "Haifa": (32.8052, 34.9857),
    "Beer Sheva": (31.2462, 34.7857),
    "Eilat": (29.5528, 34.9480),
}

def get_city_coordinates(city_name):
    """Returns the coordinates of the given city name or None if not found."""
    return CITIES_COORDINATES.get(city_name, None)
