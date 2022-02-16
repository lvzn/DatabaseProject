from os import devnull
import sqlite3

def query(conn):
    while True:
        print("Choose 1\n"+
        "1) Search for games by developer\n"+
        "2) Search for games by publisher (note: please search by developer if game is self-published)\n"+
        "3) Search for games by composer\n"+
        "4) Show all games a specific user owns\n"+
        "5) \n"+
        "0) fuck go back")
        userChoice = int(input("Your choice: "))
        if userChoice == 0:
            break
        elif userChoice == 1:
            devName = input("Name of the developer: ")
            cur = conn.cursor()
            cur.execute("SELECT * FROM Game WHERE game_dev LIKE (?)", (devName,))
            games = cur.fetchall()
            for game in games:
                print(game) #todo print only game name
        elif userChoice == 2:
            pubName = input("Name of the publisher: ")
            cur = conn.cursor()
            cur.execute("SELECT * FROM Game WHERE game_pub LIKE (?)", (pubName,))
            games = cur.fetchall()
            for game in games:
                print(game)
        elif userChoice == 3:
            compName = input("Name of the developer: ")
            cur = conn.cursor()
            cur.execute("SELECT * FROM Game WHERE game_comp LIKE (?)", (devName,))
            games = cur.fetchall()
            for game in games:
                print(game)


def insert(conn):
    pass

def update(conn):
    pass


def menu():
    conn = sqlite3.connect("database.db")
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
            query(conn)
        elif userChoice == 2:
            insert(conn)
        elif userChoice == 3:
            update(conn)
        else:
            print("Incorrect input. Try again.")
            

menu()