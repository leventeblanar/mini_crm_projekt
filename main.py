from api_client import APIclient

def main():
    client = APIclient()
    
    try:
        users_data = client.get_users()
        print("A felhasználók listája:")
        for user in users_data["data"]:
            print(f"UserID: {user['id']}")
            print(f"First name: {user['first_name']}")
            print(f"Last name: {user['last_name']}")
            print(f"email: {user['email']}")
            print(f"-"*40)
    except Exception as e:
        print(str(e))
    

if __name__ == '__main__':
    main()
