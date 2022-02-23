import sqlite3
import csv
# todo: script to seed database before initializing app
def seed():
    con = sqlite3.connect("data.db")
    cObj = con.cursor()

    # cObj.execute("DROP TABLE IS EXISTS questions")
    # # Category, Question, Answer
    # cObj.execute(
    #     "CREATE TABLE IF NOT EXISTS questions(ID INTEGER, "
    #     "Category TEXT, Question TEXT, Answer TEXT)")
    # con.commit()


    a_file = open("./TriviaQuestions.csv")

    build_db_sql = open("./resources/build_db.sql")
    build_db_sql_string = build_db_sql.read()
    cObj.executescript(build_db_sql_string)

    rows = csv.reader(a_file)

    cObj.executemany("INSERT INTO questions (ID, Category, Question, Answer) VALUES (?, ?, ?, ?)", rows)

    cObj.execute("SELECT * FROM questions")

    print(cObj.fetchall())


class DBSeeder:
    pass
