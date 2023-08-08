from db.models import User, Expense, Category, session


def register_user(username, password):
    existing_user = session.query(User).filter_by(username=username).first()
    if existing_user:
        return None

    new_user = User(username=username, password=password)
    session.add(new_user)
    session.commit()
    return new_user


def authenticate_user(username, password):
    user = session.query(User).filter_by(username=username, password=password).first()
    return user


def login_user():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    user = authenticate_user(username, password)
    if user:
        print("Login successful!")
        loged_in_user(user)
    else:
        print("Invalid username or password.")


def loged_in_user(user):
    print(f"Welcome, {user.username}!")
    while True:
        print("Main menu ")
        print("1: Add an expense ")
        print("2: View your expenses ")
        print("3: update your expenses ")
        print("4: Delete an expense ")
        print("5: Log out ")

        choice = input("Please select an option :")

        if choice == "1":
            add_expense(user)
        elif choice == "2":
            pass
        elif choice == "3":
            pass
        elif choice == "4":
            pass
        elif choice == "5":
            print("You have been logged out.")
            break
        else:
            print("Please choose one of the 5 options.")


def add_expense(user):
    print("Adding an expense: ")
    amount = float(input("Enter the amount: "))
    description = input("Enter a description: ")
    date = input("Enter the date (MM/DD): ")

    categories = session.query(Category).all()
    print("Available Categories: ")
    for category in categories:
        print(f"{category.id} : {category.name}")

    print("0 : Add a new category")
    category_id = int(input("Select a Categoty ID: '"))

    if category_id == 0:
        new_category_name = input("Enter the name of the new category: ")
        new_category = Category(name=new_category_name)
        session.add(new_category)
        session.commit()
        selected_category = new_category
    else:
        selected_category = session.query(Category).get(category_id)

        if not selected_category:
            print("Invalid category ID, expense not added.")

    new_expense = Expense(
        amount=amount,
        description=description,
        date=date,
        category=selected_category,
        user=user,
    )

    session.add(new_expense)
    session.commit()
    print("Expense added.")
