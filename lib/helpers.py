from db.models import User, Expense, Category, session

# List to store monthly expenses
monthly_expenses = []

# Dictionary to map category names to their IDs
category_name_to_id = {}


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
    username = input("\033[48;5;236m\033[38;5;123mEnter your username: \033[0;0m")
    password = input("\033[48;5;236m\033[38;5;123mEnter your password: \033[0;0m")

    user = authenticate_user(username, password)
    if user:
        print("\033[48;5;236m\033[38;5;123mLogin successful!\033[0;0m")
        loged_in_user(user)
    else:
        print("\033[48;5;236m\033[38;5;123mInvalid username or password.\033[0;0m")


def loged_in_user(user):
    print(f"\033[48;5;236m\033[38;5;123mWelcome, {user.username}!\033[0;0m")
    while True:
        print("\033[48;5;236m\033[38;5;123mMain menu \033[0;0m")
        print("\033[48;5;236m\033[38;5;123m1: \033[38;5;208mAdd an expense \033[0;0m")
        print(
            "\033[48;5;236m\033[38;5;123m2: \033[38;5;208mView your expenses \033[0;0m"
        )
        print(
            "\033[48;5;236m\033[38;5;123m3: \033[38;5;208mUpdate your expenses \033[0;0m"
        )
        print(
            "\033[48;5;236m\033[38;5;123m4: \033[38;5;208mDelete an expense \033[0;0m"
        )
        print("\033[48;5;236m\033[38;5;123m5: \033[38;5;208mLog out \033[0;0m")

        choice = input("\033[48;5;236m\033[38;5;123mPlease select an option: \033[0;0m")

        if choice == "1":
            add_expense(user)
        elif choice == "2":
            view_expenses(user)
        elif choice == "3":
            update_expenses(user)
        elif choice == "4":
            delete_expense(user)
        elif choice == "5":
            print("\033[48;5;236m\033[38;5;123mYou have been logged out.\033[0;0m")
            break
        else:
            print(
                "\033[48;5;236m\033[38;5;123mPlease choose one of the 5 options.\033[0;0m"
            )


def add_expense(user):
    print("\033[48;5;236m\033[38;5;123mAdding an expense:\033[0;0m")
    amount = float(input("\033[48;5;236m\033[38;5;123mEnter the amount: \033[0;0m"))
    description = input("\033[48;5;236m\033[38;5;123mEnter a description: \033[0;0m")
    date = input("\033[48;5;236m\033[38;5;123mEnter the date (MM-DD-YYYY): \033[0;0m")

    categories = session.query(Category).all()
    print("\033[48;5;236m\033[38;5;123mAvailable Categories:\033[0;0m")
    for category in categories:
        print(f"\033[48;5;236m\033[38;5;123m{category.id} : {category.name}\033[0;0m")
        category_name_to_id[category.name] = category.id

    category_id_or_new = input(
        "\033[48;5;236m\033[38;5;123mSelect a Category ID or enter 'new' to add a new category: \033[0;0m"
    )

    if category_id_or_new.lower() == "new":
        new_category_name = input(
            "\033[48;5;236m\033[38;5;123mEnter the name of the new category: \033[0;0m"
        )
        new_category = Category(name=new_category_name)
        session.add(new_category)
        session.commit()  # Commit the session to generate the ID
        selected_category_id = new_category.id
    else:
        selected_category_id = category_name_to_id.get(category_id_or_new)

    if not selected_category_id:
        print(
            "\033[48;5;236m\033[38;5;123mInvalid category ID or name, expense not added.\033[0;0m"
        )
        return

    new_expense = Expense(
        amount=amount,
        description=description,
        date=date,
        category_id=selected_category_id,
        user_id=user.id,
    )

    session.add(new_expense)
    session.commit()
    print("\033[48;5;236m\033[38;5;123mExpense added.\033[0;0m")


def view_expenses(user):
    expenses = session.query(Expense).filter_by(user_id=user.id).all()
    if not expenses:
        print("\033[48;5;236m\033[38;5;123mNo expenses found.\033[0;0m")
    else:
        print("\033[48;5;236m\033[38;5;123mYour expenses: \033[0;0m")
        for expense in expenses:
            print(
                f"\033[48;5;236m\033[38;5;123mID: {expense.id}, Amount: {expense.amount}, Description: {expense.description}, Date: {expense.date}\033[0;0m"
            )


#  For updating an expense
# do the same thins ast view expenses so user can see what should be changed
# and then have the user to select the ID for that expense then create a query object that targets the expense after that make an if statment so if id is not in expense print something and if it is have nre variables for new-expense and after that assign those variables to expenses then commit it.


def update_expenses(user):
    expenses = session.query(Expense).filter_by(user_id=user.id).all()
    print(
        "\033[48;5;236m\033[38;5;123mSelect the ID of expence that you want to update.\033[0;0m"
    )
    for expense in expenses:
        print(
            f"\033[48;5;236m\033[38;5;123mID: {expense.id}, Amount: {expense.amount}, Description: {expense.description}, Date: {expense.date}\033[0;0m"
        )

    expense_id = int(
        input(
            "\033[48;5;236m\033[38;5;123mEnter the ID of the expense to update: \033[0;0m"
        )
    )
    expense = session.query(Expense).filter_by(id=expense_id, user_id=user.id).first()
    print(expense)

    if not expense:
        print("\033[48;5;236m\033[38;5;123mINvalid expense ID.\033[0;0m")
        return

    new_amount = float(
        input("\033[48;5;236m\033[38;5;123mEnter the new amout: \033[0;0m")
    )
    new_description = input(
        "\033[48;5;236m\033[38;5;123mEnter the new description: \033[0;0m"
    )
    new_date = input("\033[48;5;236m\033[38;5;123mEnter the new date: \033[0;0m")

    expense.amount = new_amount
    expense.description = new_description
    expense.date = new_date

    session.commit()
    print("\033[48;5;236m\033[38;5;123mExpense updated.\033[0;0m")


def delete_expense(user):
    print("\033[48;5;236m\033[38;5;123mDeleting an expense: \033[0;0m")

    expenses = session.query(Expense).filter_by(user_id=user.id).all()
    if not expenses:
        print("\033[48;5;236m\033[38;5;123mNo expenses to delete.\033[0;0m")
        return

    print("\033[48;5;236m\033[38;5;123mSelect an expense to delete: \033[0;0m")
    for expense in expenses:
        print(
            f"\033[48;5;236m\033[38;5;123mID: {expense.id}, Amount: {expense.amount}, Description: {expense.description}\033[0;0m"
        )

    expense_id = input(
        "\033[48;5;236m\033[38;5;123mEnter the ID of the expense you want to delete: \033[0;0m"
    )

    expense_to_delete = session.query(Expense).get(expense_id)
    if not expense_to_delete:
        print("\033[48;5;236m\033[38;5;123mInvalid expense ID. \033[0;0m")
        return

    session.delete(expense_to_delete)
    session.commit()
    print("\033[48;5;236m\033[38;5;123mExpense deleted.\033[0;0m")
