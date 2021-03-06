import unittest
from Model import Question
from models.player import Player
from models.room import Room
from TriviaController import TriviaController
from TriviaView import TriviaView
import tkinter as tk



class TriviaControllerTest(unittest.TestCase):

     def test_init(self):
         view = TriviaView(tk.Tk(), "640x640", "TriviaMaze", 64)
         triviaController=TriviaController(view)
         assert triviaController.get_width() == 4
         assert triviaController.get_height() == 4

     def test_generate_map(self):
         view = TriviaView(tk.Tk(), "640x640", "TriviaMaze", 64)
         triviaController = TriviaController(view)
         triviaController.generate_map()
         map = triviaController.get_map()
         assert len(map) == 4
         assert len(map[0]) == 4
         assert isinstance(map[0][0], Room)
         assert isinstance(map[3][3], Room)

     def test_generate_player(self):
         view = TriviaView(tk.Tk(), "640x640", "TriviaMaze", 64)
         triviaController = TriviaController(view)
         triviaController.generate_map()
         triviaController.generate_player()
         triviaController.__player.generate_player()
         triviaController.__player.generate_player()
         player_x = triviaController.__player.get_x()
         player_y = triviaController.__player.get_y()
         assert player_x == 1
         assert player_y == 1
         assert triviaController.room_value(player_y, player_x) == 10
         player = Player()
         player.generate_player()
         assert player.get_x() == 1
         assert player.get_y() == 1

     def test_movement_available(self):
         view = TriviaView(tk.Tk(), "640x640", "TriviaMaze", 64)
         triviaController = TriviaController(view)
         triviaController.generate_map()
         assert triviaController.movement_available(-1, -1) is False
         assert triviaController.movement_available(1, 1) is True
         assert triviaController.movement_available(4, -1) is False
         assert triviaController.movement_available(3, 3) is True

     def test_block_room(self):
         view = TriviaView(tk.Tk(), "640x640", "TriviaMaze", 64)
         triviaController = TriviaController(view)
         triviaController.generate_map()
         assert triviaController.room_value(1, 1) == 0
         assert triviaController.room_status(1, 1) is False
         triviaController.block_room(1, 1)
         assert triviaController.room_value(1, 1) == 4
         assert triviaController.room_status(1, 1) is True

     def test_reach_exit(self):
         view = TriviaView(tk.Tk(), "640x640", "TriviaMaze", 64)
         triviaController = TriviaController(view)
         triviaController.generate_map()
         triviaController.generate_player()
         assert triviaController.has_reached_exit() is False

     def test_game_over(self):
         view = TriviaView(tk.Tk(), "640x640", "TriviaMaze", 64)
         triviaController = TriviaController(view)
         triviaController.generate_map()
         triviaController.generate_player()
         triviaController.block_room(triviaController.player_y() + 1, triviaController.player_x())
         triviaController.block_room(triviaController.player_y(), triviaController.player_x() + 1)
         assert triviaController.game_over() is True

     def test_get_question_from_db(self):
         question = db.getQuestion()
         self.assertEqual(question, 'Is this the question?')

     def test_move_character(self):
         isMoved = character.moved()
         self.assertEqual(isMoved, True)
         self.assertNotEqual(isMoved, False)

     def test_answer_question(self):
       isAnswered = Question.answerQuestion()
       self.assertEqual(isAnswered, True)
       self.assertNotEqual(isAnswered, False)

     def test_enter_west(self):
         isEnteredWest = character.enterWest()
         self.assertEqual(isEnteredWest, True)
         self.assertNoEqual(isEnteredWest, False)

     def test_enter_east(self):
         isEnteredEast = character.enterEast()
         self.assertEqual(isEnteredEast, True)
         self.assertNotEqual(isEnteredEast, False)

     def test_enter_north(self):
         isEnteredNorth = character.enterNorth()
         self.assertEqual(isEnteredNorth, True)
         self.assertNotEqual(isEnteredNorth, False)

     def test_enter_south(self):
          player = Player()
          player.move_south(2, 0)
          self.assertEqual(player.get_x(), 2)
          self.assertNotEqual(enter_south.get_y(),0)
          
class Map_Test(unittest.TestCase):
    
               
    def test_block_room(self):
        new_map = [[Room(y, x) for x in range(6)] for y in range(6)]
        map = Map(new_map)
        map.block_room(2, 3)
        map2=map.get_map()
        room = map2[2][3]
        self.assertEqual(room.get_value(), 4)
        self.assertEqual(room.visited_status(), True)
        
    
    def test_has_reach_exit(self):
        new_map = [[Room(y, x) for x in range(6)] for y in range(6)]
        map = Map(new_map)
        self.assertEqual(map.has_reach_exit(4, 4), True)
          

class TestPlayer(unittest.TestCase):

    def test_get_name(self):
         player = Player()
         player.set_name("Manny")
         self.assertEqual (player.get_name(), "Manny")

    def test_init(self):
        player = Player(5, 6)
        self.assertEqual(player.get_y(), 5)
        self.assertEqual(player.get_x(), 6)

    def test_set_score(self):
        player = Player()
        player.set_score(5)
        self.assertEqual(player.get_score(), 5)

    def test_get_score(self):
        player = Player()
        player.set_score(5)
        self.assertEqual(player.get_score(), 5)

    def test_set_name(self):
        player = Player()
        player.set_name("Manny")
        self.assertEqual(player.get_name(), "Manny")

    def test_move(self):
        player = Player()
        player.move(7, 25)
        self.assertEqual(player.get_y(), 7)
        self.assertEqual(player.get_x(), 25)

    def test_generate_player(self):
        player = Player(40, 20)
        player.generate_player("Manny")
        self.assertEqual(player.get_y(), 1)
        self.assertEqual(player.get_x(), 1)

    def test_get_x(self):
        player = Player()
        player.set_x(0)
        self.assertEqual(player.get_x(), 0)

    def test_get_y(self):
        player = Player()
        player.set_y(0)
        self.assertEqual(player.get_y(),0)

    def test_set_y(self):
         player = Player()
         player.set_y(3)
         self.assertEqual(player.get_y(),3)
