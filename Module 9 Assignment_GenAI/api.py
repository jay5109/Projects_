import requests

class API:
    def __init__(self, API_KEY, NASA_URL):
        # Instance variabes
        self.API_KEY = API_KEY             
        self.NASA_URL = NASA_URL
        API_KEY = None
    
# Sends get request and returns json object
    def get_response(self, params):
        params["api_key"] = 'ELAgLGPJaS2081IZDz6oNGPo3VdAyeCg11pSGbrG'
        response = requests.get(self.NASA_URL, params=params)
        return response.json()


        
