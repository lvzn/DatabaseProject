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
            devName = f"%{devName}%"
            cur = conn.cursor()
            cur.execute("SELECT * FROM Game WHERE game_dev LIKE (?)", (devName,))
            games = cur.fetchall()
            print("\nList of games found:")
            for game in games:
                print(game["game_name"])
            print()
        elif userChoice == 2:
            pubName = input("Name of the publisher: ")
            pubName = f"%{pubName}%"
            cur = conn.cursor()
            cur.execute("SELECT * FROM Game WHERE game_pub LIKE (?)", (pubName,))
            games = cur.fetchall()
            print("\nList of games found:")
            for game in games:
                print(game["game_name"])
            print()
        elif userChoice == 3:
            compName = input("Name of the composer: ")
            compName = f"%{compName}%"
            cur = conn.cursor()
            cur.execute("SELECT * FROM Game WHERE game_comp LIKE (?)", (compName,))
            games = cur.fetchall()
            print("\nList of games found:")
            for game in games:
                print(game["game_name"])
            print()
        elif userChoice == 4:
            cur = conn.cursor()
            cur.execute("SELECT * FROM User")
            users = cur.fetchall()
            print("Whose games would you like to view?")
            for user in users:
                print(f"{user['id']}) {user['username']}")
            userID = int(input("User: "))
            cur = conn.cursor()

            script = """
            SELECT DISTINCT Game.game_name FROM ((Game
            inner join User_games ON User_games.FK_game_id=Game.game_id)
            inner join User ON User_games.FK_user_id=?);
            """

            cur.execute(script, (userID,))
            games = cur.fetchall()
            print()
            for game in games:
                print(game['game_name'])
            print()



def insert(conn):
    print("Registration")
    login = input("Enter your email: ")
    passwd = input("Enter your password: ")
    cur = conn.cursor()
    cur.execute("INSERT INTO LoginT (login_name, login_password) values (?,?)", (login, passwd))
    username = input("Choose username: ")
    cur.execute("INSERT INTO User (username) values (?)", (username,))
    conn.commit()
    pass

def update(conn):
    pass


def menu():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
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