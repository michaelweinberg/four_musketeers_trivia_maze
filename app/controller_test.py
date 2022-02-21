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
    # def test_get_question_from_db(self):
    #     pass
    #
    # def test_move_character(self):
    #     pass
    #
    # def test_answer_question(self):
    #     pass
    #
    # def test_enter_west(self):
    #     pass
    #
    # def test_enter_east(self):
    #     pass
    #
    # def test_enter_north(self):
    #     pass
    #
    # def test_enter_south(self):
    #     pass