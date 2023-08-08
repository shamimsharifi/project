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
    else:
        print("Invalid username or password.")


def add_expense(user, amount, description, date, category_name):
    category = session.query(Category).filter_by(name=category_name).first()
    if not category:
        category = Category(name=category_name)
        session.add(category)
        session.commit()

    expense = Expense(
        amount=amount, description=description, date=date, category=category, user=user
    )
    session.add(expense)
    session.commit()
    print("Expense added successfully!")


def list_expenses(user):
    expenses = session.query(Expense).filter_by(user=user).all()
    if not expenses:
        print("No expenses found.")
        return

    print("List of Expenses:")
    for expense in expenses:
        print(
            f"Amount: {expense.amount}, Description: {expense.description}, Date: {expense.date}, Category: {expense.category.name}"
        )
