"""
API Parent Class
"""

import requests

class API:
    def __init__(self, base_url, api_key=None):
        self.base_url = base_url
        self.api_key = api_key

    def get_response(self, params):
        response = requests.get(self.base_url, params=params)
        return response.json()