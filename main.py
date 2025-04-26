from api_client import APIclient

def main():
    client = APIclient()
    
    try:
        users_data = client.get_users()
        print("A felhasználók listája:")
        for user in users_data["data"]:
            print(f"{user['id']}: {user['first_name']} {user['last_name']} - {user['email']}")
    except Exception as e:
        print(str(e))
    

if __name__ == '__main__':
    main()
