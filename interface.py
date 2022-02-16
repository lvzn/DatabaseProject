import sqlite3

def query(cur):
    pass

def insert(cur):
    pass

def update(cur):
    pass


def menu():
    db = sqlite3.connect("database.db")
    cur = db.cursor()
    while True:
        print("\nGameDB interface\n"+
        "What would you like to do?\n"+
        "1) Search\n"+
        "2) Add a user\n"+
        "3) Update values\n"+
        "0) Quit")
        userChoice = int(input("Your choice: "))
        if (userChoice == 0):
            exit(0)
        elif userChoice == 1:
            query(cur)
        elif userChoice == 2:
            insert(cur)
        elif userChoice == 3:
            update(cur)
        else:
            print("Incorrect input. Try again.")
            

menu()