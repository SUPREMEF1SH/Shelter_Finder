



def get_city_coordinates(city_name):

  return cities_coordinates.get(city_name, None)  # Returns None if city is not found
# Example usage:
city_coordinates = get_city_coordinates("Tel Aviv")
print(city_coordinates)  # Output: (32.0788, 34.7749)