class Model:

    def __init__(self, username):
        self.username = username

    def get_username(self):
        return self.username


class Question:
    def get_question(self):
        summary = self._dbselect()
        result = []
        for row in summary:
            result.append(row[0])
            result.append(row[1])
        return result

    def _dbselect(self):
        connection = sqlite3.connect("mydb.db")
        cursorObj = connection.cursor()
        id = random.Random(0, 60)
        result = cursorObj.execute("select * from question where id=%id " %id)
        results = result.fetchall()
        connection.close()
        cursorObj.close()
        return results