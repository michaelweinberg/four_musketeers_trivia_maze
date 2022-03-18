import unittest
from Model import Question
from models.player import Player
from models.room import Room
from models.map import Map
from TriviaController import TriviaController
from TriviaView import TriviaView
import tkinter as tk

    
class Room_Test(unittest.TestCase):
    
    def test_set_empty(self):  # room
        room = Room(0, 0)
        room.set_empty()
        self.assertEqual(room.get_name(), "empty room")
        self.assertEqual(room.get_value(), 0)
        
    def test_str__(self):
        room = Room(1, 1)
        string = str(room)
        self.assertEqual(string,"This is a x1y1value0")
            
      
    def test_set_value(self):
        room1 = Room(2 ,2)
        room1.set_value(1)
        self.assertEqual(room1.get_value(), 1)
        
        
            
    def test_set_block(self):
          room = Room(3, 3)
          room.set_block()
          self.assertEqual(room.get_value(), 4)    
                 
    def test_get_x(self):
        room = Room(2, 2)
        self.assertEqual(room.get_x(), 2)
        
        
    def test_get_y(self):
        room = Room(1, 1)
        self.assertEqual(room.get_y(), 1)
        

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
    
        

class Player_Test(unittest.TestCase):
    
    def test_generate_player(self):  
        player = Player(40, 20)
        player.generate_player("Manny")
        self.assertEqual(player.get_y(), 1)
        self.assertEqual(player.get_x(), 1)
        self.assertEqual(player.get_name(), "Manny")


    def test_get_name(self):  
        player = Player()
        player.set_name("Manny")
        self.assertEqual(player.get_name(), "Manny")

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

    def test_get_x(self):  
        player = Player()
        player.set_x(0)
        self.assertEqual(player.get_x(), 0)

    def test_get_y(self):  
        player = Player()
        player.set_y(0)
        self.assertEqual(player.get_y(), 0)

    def test_set_y(self):  
        player = Player()
        player.set_y(3)
        self.assertEqual(player.get_y(), 3)


if __name__ == '__main__':
    unittest.main()
    
    
    
    
    
