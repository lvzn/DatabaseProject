from os import devnull
import sqlite3
from bokeh.plotting import figure, output_file, show

def query(conn, id):
    while True:
        print("Choose 1\n"+
        "1) Search for games by developer\n"+
        "2) Search for games by publisher (note: please search by developer if game is self-published)\n"+
        "3) Search for games by composer\n"+
        "4) Show all your games\n"+
        "5) Calculate total played hours\n"+
        "6) Generate a chart\n"+
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

            script = """
            SELECT DISTINCT Game.game_name FROM ((Game
            inner join User_games ON User_games.FK_game_id=Game.game_id)
            inner join User ON User_games.FK_user_id=?);
            """

            cur.execute(script, (id,))
            games = cur.fetchall()
            print()
            for game in games:
                print(game['game_name'])
            print()
        elif userChoice == 5:
            cur = conn.cursor()

            script = """
            SELECT DISTINCT User_games.hours_played FROM ((User_games
            inner join Game ON User_games.FK_game_id=Game.game_id)
            inner join User ON User_games.FK_user_id=?);
            """

            cur.execute(script, (id,))
            games = cur.fetchall()
            print()
            hoursPlayed = 0
            for game in games:
                hoursPlayed += game['hours_played']
            print("Hours you've played in total: " + str(hoursPlayed) + "\n")
        elif userChoice == 6:
            output_file("chart.html")
            cur = conn.cursor()
            script = """
            SELECT DISTINCT Game.game_name, User_games.hours_played FROM ((Game
            inner join User_games ON User_games.FK_game_id=Game.game_id)
            inner join User ON User_games.FK_user_id=?);
            """
            cur.execute(script, (id,))
            games = []
            hours = []
            for game in cur.fetchall():
                games.append(game["game_name"])
                hours.append(game["hours_played"])
            p = figure(x_range=games)
            p.vbar(x=games, top=hours, width=0.8)
            show(p)




def insert(conn):
    print("Registration")
    login = input("Enter your email: ")
    passwd = input("Enter your password: ")
    cur = conn.cursor()
    cur.execute("INSERT INTO LoginT (login_name, login_password) values (?,?)", (login, passwd))
    username = input("Choose username: ")
    cur.execute("INSERT INTO User (username) values (?)", (username,))
    conn.commit()


def update(conn, id):
    print("Change your username")
    newUsername = input("Enter new username: ")
    cur = conn.cursor()
    cur.execute("UPDATE USER SET username = ? WHERE id=?", (newUsername, id))
    conn.commit()

def login(conn):
    print("Login")
    cur = conn.cursor()
    while True:
        username = input("Username: ")
        cur.execute("SELECT * FROM LoginT where login_name=?", (username,))
        user = cur.fetchone()
        if user == None:
            print("User doesn't exist. Try again:")
            continue
        passwd = input("Password: ")
        if user["login_password"] == passwd:
            print("Login succesful!")
            return user["id"]

def menu():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    user_id = login(conn)
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
            query(conn, user_id)
        elif userChoice == 2:
            insert(conn)
        elif userChoice == 3:
            update(conn, user_id)
        else:
            print("Incorrect input. Try again.")
            
menu()