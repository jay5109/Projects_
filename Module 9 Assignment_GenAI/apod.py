from api import API
import requests

class APOD(API):
    #step 7 a.i and a.ii
    def __init__(self, API_KEY): 
        url='https://api.nasa.gov/planetary/apod'
        super().__init__(API_KEY, NASA_URL= url) #Inherit the api key and nasa url from the constructor in the parent-class "class API:".
        
    # step 7.b
    def fetch_apod(self, date: str):
        params = {"date": date}
        return self.get_response(params) 
    
#Step 7.c: create method download_image()
    def download_image(self, url, filename): #step 7.i takes URL and filename as arguments
        response = requests.get(url)    #step 7.ii uses request.get with the img URL to download the image.
        
        # step 7.c.iii: checks if status code response returned is 200.
        if response.status_code== 200:
            with open(filename, "wb") as f:
                f.write(response.content)
            print(f"Image successfully saved as {filename}")
        
        #step 8.iv Otherwise prints to terminal the following statement.
        else:
            print("Failed to download image. Status code: " + response.status_code)
        
        