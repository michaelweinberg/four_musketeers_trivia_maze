import unittest
from models.room import Room
from TriviaController import TriviaController

class TriviaControllerTest(unittest.TestCase):
    def test_init(self):
        triviaController=TriviaController()
        assert triviaController.get_width() == 4
        assert triviaController.get_height() == 4

    def test_generate_map(self):
        triviaController = TriviaController()
        triviaController.generate_map()
        map = triviaController.get_map()
        assert len(map) == 4
        assert len(map[0]) == 4
        assert isinstance(map[0][0], Room)
        assert isinstance(map[3][3], Room)

    def test_generate_player(self):
        triviaController = TriviaController()
        triviaController.generate_map()
        triviaController.generate_player()
        player_x = triviaController.player_x()
        player_y = triviaController.player_y()
        assert player_x == 0
        assert player_y == 0
        assert triviaController.room_value(player_y, player_x) == 10

    def test_movement_available(self):
        triviaController = TriviaController()
        triviaController.generate_map()
        assert triviaController.movement_available(-1, -1) is False
        assert triviaController.movement_available(1, 1) is True
        assert triviaController.movement_available(4, -1) is False
        assert triviaController.movement_available(3, 3) is True

    def test_block_room(self):
        triviaController = TriviaController()
        triviaController.generate_map()
        assert triviaController.room_value(1, 1) == 0
        assert triviaController.room_status(1, 1) is False
        triviaController.block_room(1, 1)
        assert triviaController.room_value(1, 1) == 4
        assert triviaController.room_status(1, 1) is True

    def test_reach_exit(self):
        triviaController = TriviaController()
        triviaController.generate_map()
        triviaController.generate_player()
        assert triviaController.reach_exit() is False

    def test_game_over(self):
        triviaController = TriviaController()
        triviaController.generate_map()
        triviaController.generate_player()
        triviaController.block_room(triviaController.player_y() + 1, triviaController.player_x())
        triviaController.block_room(triviaController.player_y(), triviaController.player_x() + 1)
        assert triviaController.game_over() is True

    # Manny's test
    def test_get_question_from_db(self):
        question = db.getQuestion()
        self.assertEqual(question, 'Is this the question?')

    def test_move_character(self):
        isMoved = character.moved()
        self.assertEqual(isMoved, True)
         self.assertNotEqual(isMoved, False)

    def test_answer_question(self):
        isAnswered = user.answerQuestion()
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
        isEnteredSouth = character.enterSouth()
        self.assertEqual(isEnteredSouth, True)
        self.assertNotEqual(isEnteredSouth, False)
