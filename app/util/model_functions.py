import sqlite3

con = sqlite3.connect('mydb.db')
cObj = con.cursor()


def create_table():
    cObj.execute(
        "CREATE TABLE IF NOT EXISTS answers(id INTEGER PRIMARY KEY, question TEXT, answer TEXT)")
    con.commit()


def insert_value(id, name, country, age, medals):
    cObj.execute("INSERT INTO athletic VALUES(?, ?, ?, ?, ?)", (id, name, country, age, medals))
    con.commit()
    
def save_game(name, player, map):
    cObj.execute("INSERT INTO games VALUES(?, ?, ?)", (name, player, map))
    con.commit()

def load_game(name):
    cObj.execute("SELECT name, player, map from games where name=?", (name,))
    result = cObj.fetchall()
    return result

def data_fetch():
    cObj.execute("SELECT * FROM athletic")
    result = cObj.fetchall()
    print(result)


def delete_all():
    cObj.execute("DELETE FROM athletic Where id=?", (1,))
    #k = input("enter the key to delete:\n")
    con.commit()



