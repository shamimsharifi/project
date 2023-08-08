# Phase 3 CLI Project Template

## Learning Goals

- Discuss the basic directory structure of a CLI.
- Outline the first steps in building a CLI.

---

## Introduction

You now have a basic idea of what constitutes a CLI, but you (understandably!)
likely don't have the best idea of where to start. Fork and clone this lesson
for a template for your CLI. Take a look at the directory structure before we
begin:

```console
.
├── Pipfile
├── Pipfile.lock
├── README.md
└── lib
    ├── cli.py
    ├── db
    │   ├── models.py
    │   └── seed.py
    ├── debug.py
    └── helpers.py
```

This application will help you track your expences view them and update them.

-To make this application the first step is to make the database and the tables. We will have three tables: users, categories and expenses.
The relatinship between tables are many one to many in more specific way, a user can have may expences but an expense can only have one user, in the same way a a category can have many expences but an expence can only have one category so category has a one to many relationship with expenses.
-I have my modules and my tables in mmodels.py where I imported required classes, tools and datatypes that are going to be used while builting the database.
-The seed for the base are in the module seeds.py.
-The first thing that I want to do in the CLI in a login user where users can log in or register for the app. THe functions for login is in helpers.py.
When user enters the app, should see three option

- Register
- Login
- Exit

Register: should ask for a username and a password, username must be unique then it should add the user data to database and then it should print("Registered successfully) and if the username already exits it should print("please chose a different username).

Login: Should ask for the username and password and when loged in should give 3 options:

- Add an expence
- view your expenses
- update or delete your expenses
- log out
  ADD AN EXPENSE: will give the user the inputs for the expence like amount, decription, date, category id (shoudl give customer options for a category like food, transportation ,enetertainment and give an other option add new category
  )
  and then add the expence to the database and print("Expense added.)

  VIEW YOUR EXPENSES: will give the user all the expenses
