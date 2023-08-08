from db.models import session
from helpers import register_user, login_user, loged_in_user


def main_menu():
    while True:
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            username = input("Enter a username: ")
            password = input("Enter a password: ")
            user = register_user(username, password)
            if user:
                print("Registration successful!")
            else:
                print("Username already taken.")
                break

        elif choice == "2":
            login_user()
            break

        elif choice == "3":
            break

        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main_menu()
