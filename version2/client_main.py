from api_client import APIclient

def main():
    client = APIclient()

    while True:
        print("-" * 50)
        print("\n ***** Mini CRM App *****")
        print("\n Please select a function:")
        print("1. Review all existing users")
        print("2. Review user by UserId")
        print("3. Create new user")
        print("4. Modify existing user")
        print("5. Delete user")
        print("6. Exit")
        print(("-" * 50))
        
        
        choice = input("Selected function: ")
        
        if choice == "1":
            users = client.get_users()
            for i, user in enumerate(users):
                print(f"\n[{i}] {user['first_name']} {user['last_name']} - {user['email']}")
        
        elif choice == "2":
            print("\n-- Review user by UserId --")
            user_id = input("UserId: ")
            result = client.get_user_by_id(user_id)
            print(result)
            
        elif choice == "3":
            print("\n-- Create new user --")
            first_name = input("First name: ").capitalize()
            last_name = input("Last name: ").capitalize()

            email_valid = False

            while not email_valid:
                email = input("Email: ")
                if "@" not in email or "." not in email:
                    print("Please provide a valid email address.")
                else:
                    email_valid = True
            
            phone = input("Phone: ")
            
            new_user = {
                "first_name": first_name,
                "last_name": last_name,
                "email": email,
                "phone": phone
            }
            
            result = client.create_user(new_user)
            print("Létrehozva: ", result)
            
        elif choice == "4":
            print("\n-- Modify existing user --")
            user_id = input("UserId: ")
            print("Please provide the new user data: ")
            
            first_name = input("First name: ").capitalize()
            last_name = input("Last name: ").capitalize()
            email = input("Email: ")
            phone = input("Phone: ")

            updated_user = {
                "first_name": first_name,
                "last_name": last_name,
                "email": email,
                "phone": phone
            }
            
            result = client.update_user(user_id, updated_user)
            print("Updated: ", result)
            
        elif choice == "5":
            print("\n-- Delete user --")
            user_id = input("UserId: ")
            result = client.delete_user(user_id)

            print("User deleted:: ", result)
        
        elif choice == "6":
            print("Exit...")
            break
        
        else:
            print("Invalid answer. Please try again.")

if __name__ == '__main__':
    main()