import random
import sqlite3


class Model:

    def __init__(self, username):
        self.username = username

    def get_username(self):
        return self.username
    
     def save_game():
        ''' creates the information to be saved'''
        saved = {"user.name", "current_score","current_location\n"}
        '''save the game'''
        pickle.dump(saved, with open("saved.data", "wb"))

    def load_game():
    """Load game state from a predefined savegame location and return the
    game state contained in that savegame.
    """
    with open(SAVEGAME_FILENAME, 'r') as savegame:
        state = jsonpickle.decode(savegame.read())
    return state


def save_game():
    """Save the current game state to a savegame in a predefined location.
    """
    global game_state
    with open(SAVEGAME_FILENAME, 'w') as savegame:
        savegame.write(jsonpickle.encode(game_state))


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

    def get_game_info(self, name):
        pass

    def get_score_list(self):
        pass
