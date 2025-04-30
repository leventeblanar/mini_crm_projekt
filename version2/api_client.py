import requests

BASE_URL = "http://127.0.0.1:8000"

class APIclient:
    
    def _handle_response(self, response):
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": response.status_code, "message": response.text}
    
    def get_users(self):
        response = requests.get(f"{BASE_URL}/users")
        return self._handle_response(response)

    
    def get_user_by_id(self, user_id):
        response = requests.get(f"{BASE_URL}/users/{user_id}")
        return self._handle_response(response)
    
    def create_user(self, user_data):
        response = requests.post(f"{BASE_URL}/users", json=user_data)
        return self._handle_response(response)

    def update_user(self, user_id, updated_data):
        response = requests.put(f"{BASE_URL}/users/{user_id}", json=updated_data)
        return self._handle_response(response)

    def delete_user(self, user_id):
        response = requests.delete(f"{BASE_URL}/users/{user_id}")
        return self._handle_response(response)