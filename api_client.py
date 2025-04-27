import requests
import sys

sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')


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
            raise Exception (f"Error while requesting user data.")

    def create_user(self, first_name, last_name, email, avatar):
        url = f"{self.BASE_URL}/users"
        new_user_data = {
            'first_name': first_name,
            'last_name':last_name,
            'email': email,
            'avatar': avatar
            }
        response = requests.post(url, headers=self.headers, json=new_user_data)
        if response.status_code == 200 or 201:
            return response.json()
        else:
            raise Exception ("Error while uploading new user.")