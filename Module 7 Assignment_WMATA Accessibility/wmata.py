import json
import requests

from geojson import Point
from urllib.parse import urlencode, quote


# API endpoint URL's and access keys
WMATA_API_KEY = "c136ce66679341b88f616ec8f03317ad" # https://developer.wmata.com/demokey
MAPBOX_API_KEY = "pk.eyJ1IjoianBlcmV6NjQiLCJhIjoiY21tZmJ1ZnYwMDc5YzJzcTFtNzgwbHd6cCJ9.K15skUMzTo-LzerWoGfl1A"
INCIDENTS_URL = "https://api.wmata.com/Incidents.svc/json/ElevatorIncidents"
STATION_URL = "https://api.wmata.com/Rail.svc/json/jStationInfo"
MAPBOX_URL = "https://api.mapbox.com/styles/v1/mapbox/streets-v12/static"
headers = {"api_key": WMATA_API_KEY, 'Accept': '*/*'}

# MapBox URL parameters
CENTER_POINT = "-77.054,38.942"
ZOOM_LEVEL = "9"
DIMENSIONS = "500x500"
MAPBOX_URL_PARAMS = f"{CENTER_POINT},{ZOOM_LEVEL}/{DIMENSIONS}"

################################################################################
""" 
Part 1
"""
# query the WMATA 'ElevatorIncidents' API to get a list of outages 
def get_station_incidents():
  # use 'requests' to retrieve escalator/elevator incident information
  response = requests.get(INCIDENTS_URL, headers= headers)
  incidents = response.json() # returns json formated response
  
  # docs: https://developer.wmata.com/api-details#api=54763641281d83086473f232&operation=54763641281d830c946a3d75
  # parse the JSON response of all incidents and create a set containing the station codes  
  
  station_codes = []                            # creates an empty to list to store the station codes
    
  for i in incidents["ElevatorIncidents"]:      # Iterates through the dictionary ElevatorIncidents
    codes = i["StationCode"]                    # locates station codes from the dictionary
    station_codes = station_codes + [codes]     # adds the station codes to the empty list

  # return the set
  return  set(station_codes) # converts the list to a set once the loop is complete

################################################################################
""" 
Part 2
"""
# query the WMATA 'Stations' API to get location coordinates (lat/lon)
def get_station_info(station_codes: str):
  
  param= {'StationCode': station_codes} # passes specific parameter to the API
  
  # use 'requests' to retrive station information by station code
  response_2 = requests.get(STATION_URL, headers= headers, params= param) 

  # docs: https://developer.wmata.com/api-details#api=5476364f031f590f38092507&operation=5476364f031f5909e4fe330c
  # return the response as JSON
  return response_2.json()

################################ DO NOT TOUCH FUNCTION BELOW  ################################################

# # convert list lat/lon pairs (tuples) to URL-encoded GeoJSON object
def encode_geojson(incident_locations):
  feature_collection = {"type":"FeatureCollection","features":[]}

  # build out FeatureCollection to contain a list of "features"
  # each "feature" contains a GeoJSON object that will be plotted as a map marker
  for location in incident_locations:
    feature = {"type":"Feature","properties": 
                {"marker-color":"#462eff","marker-size":"small","marker-symbol":"caution"},
                "geometry": Point(location)}
    feature_collection["features"].append(feature)

  # return URL-encoded (quoted) GeoJSON object
  return quote(json.dumps(feature_collection))

################################################################################
""" 
Part 3  
"""
# retrieve static map image with GeoJSON multiple marker overlay
def get_static_map(encoded_geo_json):
  # MapBox static map URL for 500x500 image centered at (-77.054,38.942) lon/lat
  static_map_url = f"{MAPBOX_URL}/geojson({encoded_geo_json})/{MAPBOX_URL_PARAMS}?access_token={MAPBOX_API_KEY}"
  
#------------------------------- My code ------------------------------------------------------------------------------------
  # use 'requests' and the static_map_url to retrieve the map image
  response_3 =requests.get(static_map_url)
  
    # if the status code is 200, write the raw bytes (binary data) in the response to a new file called map.png
  if response_3.status_code == 200:
      with open("map.png", "wb") as file:
        file.write(response_3.content)

    # else print "Error returned from MapBox API"
  else:
    print ("Error returned from MapBox API")

################################################################################

def main():
  # get a set of unique station codes experiencing outages
  station_codes = get_station_incidents()
  
  # print the total number of stations with outages
  # format: X stations are currently experiencing accessibility outages.
  num_stations= len(station_codes)
  print(f"{num_stations} stations are currently experiencing accessibility outages.") # used f-strings to convert num_stations to strings

  # print the name of each station with an outage
  # build a list of lon/lat pairs (tuples) of the location of the first 20 stations with an outage
  # format: [(lon1, lat1), (lon2, lat2), ..., ()]
  station_coords = [] # an empty list to hold the (lon, lat) coordinates
  
  for code in station_codes:    
    station_data = get_station_info(code)
    station_name = station_data["Name"]   # Accessed the dictionary station_data for Name value
    print(station_name)
        
    if len(station_coords) < 20:
      lon = station_data["Lon"]
      lat = station_data["Lat"]
      station_coords.append((lon,lat))  # Used the append function to add the pair of lon and lat as a tuple to the list, station_coords

  # convert the list of lon/lat pairs to a URL-encoded GeoJSON blob using the provided 'encode_geojson' function
  # hint: just pass the result of the previous step (the list of lon/lat tuples) to the 'encode_geojson' function
  encoded_data = encode_geojson(station_coords)
    
  # use the provided 'get_static_map' function to retrieve and download the static map image
  # hint: pass the return value from the previous step to the 'get_static_map' function
  get_static_map(encoded_data)
  
################################################################################

if __name__ == "__main__":
  main()
