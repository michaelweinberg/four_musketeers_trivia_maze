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

    # def test_generate_player(self):
    #     pass
    #
    # def test_movement_available(self, y, x):
    #     pass
    #
    # def test_block_room(self, y, x):
    #     pass
    #
    # def test_reach_exit(self):
    #     pass
    #
    # def test_game_over(self):
    #     pass
    #
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
