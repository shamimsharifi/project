from db.models import session
from helpers import (
    register_user,
    authenticate_user,
    login_user,
    add_expense,
    list_expenses,
)


def main_menu():
    while True:
        print("1. Register")
        print("2. Login")
        print("3. Add Expense")
        print("4. List Expenses")
        print("5. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            username = input("Enter a username: ")
            password = input("Enter a password: ")
            user = register_user(username, password)
            if user:
                print("Registration successful!")
            else:
                print("Username already taken.")

        elif choice == "2":
            login_user()

        elif choice == "3":
            user = authenticate_user(...)  # Authenticate the user
            amount = float(input("Enter the expense amount: "))
            description = input("Enter the expense description: ")
            date = input("Enter the expense date (YYYY-MM-DD): ")
            category = input("Enter the expense category: ")
            add_expense(user, amount, description, date, category)

        elif choice == "4":
            user = authenticate_user(...)  # Authenticate the user
            list_expenses(user)

        elif choice == "5":
            break

        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main_menu()
