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
            view_expenses(user)
        elif choice == "3":
            update_expenses(user)
        elif choice == "4":
            delete_expense(user)
        elif choice == "5":
            print("You have been logged out.")
            break
        else:
            print("Please choose one of the 5 options.")


def add_expense(user):
    print("Adding an expense: ")
    print("0 : Add a new category")
    amount = float(input("Enter the amount: "))
    description = input("Enter a description: ")
    date = input("Enter the date (MM/DD): ")

    categories = session.query(Category).all()
    print("Available Categories: ")
    for category in categories:
        print(f"{category.id} : {category.name}")

    # print("0 : Add a new category")
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


def view_expenses(user):
    expenses = session.query(Expense).filter_by(user_id=user.id).all()
    if not expenses:
        print("No expenses found.")
    else:
        print("Your expenses: ")
        for expense in expenses:
            print(
                f"ID: {expense.id}, Amount: {expense.amount}, Description: {expense.description}, Date: {expense.date}"
            )


#  For updating an expense
# do the same thins ast view expenses so user can see what should be changed
# and then have the user to select the ID for that expense then create a query object that targets the expense after that make an if statment so if id is not in expense print something and if it is have nre variables for new-expense and after that assign those variables to expenses then commit it.


def update_expenses(user):
    expenses = session.query(Expense).filter_by(user_id=user.id).all()
    print("Select the ID of expence that you want to update")
    for expense in expenses:
        print(
            f"ID: {expense.id}, Amount: {expense.amount}, Description: {expense.description}, Date: {expense.date}"
        )

    expense_id = int(input("Enter the ID of the expense to update: "))
    expense = session.query(Expense).filter_by(id=expense_id, user_id=user.id).first()
    print(expense)

    if not expense:
        print("INvalid expense ID.")
        return

    new_amount = float(input("Enter the new amout"))
    new_description = input("Enter the new description")
    new_date = input("Enter the new date")

    expense.amount = new_amount
    expense.description = new_description
    expense.date = new_date

    session.commit()
    print("Expense updated")


def delete_expense(user):
    print("Deleting an expense:")

    expenses = session.query(Expense).filter_by(user_id=user.id).all()
    if not expenses:
        print("No expenses to delete.")
        return

    print("Select an expense to delete:")
    for expense in expenses:
        print(
            f"ID: {expense.id}, Amount: {expense.amount}, Description: {expense.description}"
        )

    expense_id = input("Enter the ID of the expense you want to delete: ")

    expense_to_delete = session.query(Expense).get(expense_id)
    if not expense_to_delete:
        print("Invalid expense ID.")
        return

    session.delete(expense_to_delete)
    session.commit()
    print("Expense deleted.")
