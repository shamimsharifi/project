from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import User, Category, Expense

# Create a database engine
engine = create_engine("sqlite:///mydb.db", echo=False)
Session = sessionmaker(bind=engine)
session = Session()

# Create and add users
u1 = User(username="shamim", password="kkk")
u2 = User(username="sham", password="hhh")
u3 = User(username="shamo", password="pppp")
u4 = User(username="shami", password="nnn")
session.add_all([u1, u2, u3, u4])
session.commit()

# Create and add categories
c1 = Category(name="food")
c2 = Category(name="transport")
c3 = Category(name="entertainment")
session.add_all([c1, c2, c3])
session.commit()

# Create and add expenses
e1 = Expense(amount=34.0, description="Burger", date="2023-08-01", category=c1, user=u1)
e2 = Expense(
    amount=20.0, description="Bus fare", date="2023-08-02", category=c2, user=u2
)
e3 = Expense(
    amount=15.0, description="Movie ticket", date="2023-08-03", category=c3, user=u3
)
e4 = Expense(amount=10.0, description="Snacks", date="2023-08-04", category=c1, user=u4)
session.add_all([e1, e2, e3, e4])
session.commit()
