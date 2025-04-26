import requests

header = "x-api-key: reqres-free-v1"

class APIclient:
    BASE_URL = "https://reqres.in/api"
    API_KEY = "reqres-free-v1"
    
    def __init__(self):
        self.headers = {
            "x-api-key": self.API_KEY
        }
        
    def get_users(self, page=2):
        url = f"{self.BASE_URL}/users?page={page}"
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception (f"Hiba történt a userek lekérdezése során.")

