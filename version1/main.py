from api_client import APIclient

def main():
    client = APIclient()
    
    try:
        # GET user data
        users_data = client.get_users()
        print("List of already existing users:")
        for user in users_data["data"]:
            print(f"UserID: {user['id']}")
            print(f"First name: {user['first_name']}")
            print(f"Last name: {user['last_name']}")
            print(f"email: {user['email']}")
            print(f"-"*40)
            
        # POST new user
        print("Create new user...")

        first_name = str(input("First name: ").capitalize())
        last_name = str(input("Last name: ").capitalize())
        
        email_valid = False

        while not email_valid:
            email = str(input("Email: "))
            if "@" not in email or "." not in email:
                print("Please provide a valid email address.")
            else:
                email_valid = True
            
        avatar_valid = False
            
        while not avatar_valid:
            avatar = str(input("Avatar link: "))
            if "https://" not in avatar:
                print("Please provide a valid link for the avatar.")
            else:
                avatar_valid = True
                
        new_user = client.create_user(first_name, last_name, email, avatar)
        print("New user creation is successfull.")
        print(new_user)
            
            
    except Exception as e:
        print(str(e))
    
    

if __name__ == '__main__':
    main()
