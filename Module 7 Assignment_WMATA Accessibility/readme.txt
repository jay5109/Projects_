Name: Jeremy Perez (jperez64)
Module Info: Module 7 Assignment - WMATA Accessibility
	     Due 03/08/2026 at 11: 59 PM EST

Approach

wmata.py:

Installed the request and point libraries. Created the required API keys and stored them into the variables "WMATA_API_KEY" and "MAPBOX_API_KEY".

- The function get_station_incidents():
Created variable "response", to use the requests library to get information from the url in the "incident_url" variable. Returned the information as in json format in the variable "incidents". To parse the json response, created an empty list called "station_codes" to store station codes.The for-loop iterates through the dictionary ElevatorIncidents from the json file. Stored the "StationCodes" in the variable "codes", added to the empty list and returned this list as a set with set(station_codes).

-The function get_station_info(station_codes: str):
Passed a specific parameter to the API for get the station codes in the variable param. Stored the requested information from the url in STATION_URL variable with parameters "Station Code" in the variable response_2. Returned the station info in json format.

-The function encode_geojson(incidents):
Stored the requested the static map url in the variable response_3. Using If and Else conditional statements, created a written file "map.png" for the static map using "with open" so the file closes automatically once executed. Only if the response is true based on the 	response value equal to '200', otherwise will print "Error returned from MapBox API" in the console.  

-The function main():
Called the function get_station_incidents() and stored the return value in "station_codes". Stored the amounts of station outages in the variable, "num_stations" and printed the total number of stations currently experiencing accessibility outages. Used f-strings to convert the datatype of num_stations into strings.

Created an empty list called "station_coords" to hold the longitude and latitude values of each station. Used a for-loop to iterate through the list station_codes for each station code. Called the function get_station_info() with argument "code" and stored results in "station_data". Accessed the dictionary value for ['Name'] from station_data and stored results into "station_name" and printed every station's name. Used an if statement to check for the first 20 stations with an outage. Using the count of elements in the list station_coords, accessed the dictionary values for both ["Lon"] and ["Lat"] from station_data and stored into "lon" and "lat" variables. Then Used the function .append() to add the pair of (lon, lat) as a tuples to the empty list, station_coords. Passed the function encode_geojson() with the list of tuples in "station_coords" and stored results in "encoded_data". Lastly to retrieve and download the static map image, passed the return value from "encoded_data" to the function "get_static_map".

incidents.yaml:

Using swagger editor, passed the pet store api example and modified it based on the given criteria.The OpenAPI is 3.0.3, titled "WMATA Accessibility API", description "JHU Intro Python Module 7 Assignment - WMATA Accessibility" and the version 1.0.0. The API included a GET endpoint /incidents that accepts the path parameter called {machine_type}. The API returns a 200 response with JSON data containing an array of machine incident objects. 
Each object in the Machine component has the properties:
- StationCode; (type string , example "A11)
- StationName; (type string example "Grosvenor-Strathmore")
- UnitName; (type string, example "A11X01")
- UnitType; (type string, example "ELEVATOR")

Known Bugs: 
N/a
