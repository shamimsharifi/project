from db.models import session
from helpers import register_user, login_user, loged_in_user
import logging


def main_menu():
    logging.getLogger("sqlalchemy").setLevel(logging.ERROR)
    while True:
        print("\033[48;5;236m\033[38;5;123m1. \033[38;5;208mRegister\033[0;0m")
        print("\033[48;5;236m\033[38;5;123m2. \033[38;5;208mLogin\033[0;0m")
        print("\033[48;5;236m\033[38;5;123m3. \033[38;5;208mExit\033[0;0m")
        choice = input("\033[48;5;236m\033[38;5;123mSelect an option: \033[0;0m")

        if choice == "1":
            username = input("\033[48;5;236m\033[38;5;123mEnter a username: \033[0;0m")
            password = input("\033[48;5;236m\033[38;5;123mEnter a password: \033[0;0m")
            user = register_user(username, password)
            if user:
                print("\033[48;5;236m\033[38;5;123mRegistration successful!\033[0;0m")
            else:
                print("\033[48;5;236m\033[38;5;123mUsername already taken.\033[0;0m")
                break

        elif choice == "2":
            login_user()
            break

        elif choice == "3":
            break

        else:
            print(
                "\033[48;5;236m\033[38;5;123mInvalid choice. Please select a valid option.\033[0;0m"
            )


if __name__ == "__main__":
    main_menu()
