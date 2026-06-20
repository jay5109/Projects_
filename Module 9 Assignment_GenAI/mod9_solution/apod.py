"""
APOD Class

Grabs image and metadata from NASA's APOD API using object-oriented structure.
"""

import requests
from api import API


class APOD(API):
    def __init__(self, api_key):
        super().__init__("https://api.nasa.gov/planetary/apod", api_key)

    def fetch_apod(self, date):
        params = {"api_key": self.api_key, "date": date}
        return self.get_response(params)

    def download_image(self, url, filename):
        response = requests.get(url)
        with open(filename, 'wb') as f:
            f.write(response.content)
        print(f"\nImage successfully saved as '{filename}'")
