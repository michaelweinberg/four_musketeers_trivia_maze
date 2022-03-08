by Manny

import pygame
from pygame import mixer
from pathlib import Path


class SoundEffect:
    """
    Constructor/instance included so that a tracker can be used for sound options.
    
    """
    def __init__(self):
        """
        is_running keeps track of whether music & sound is on to 
        allow sound option to turn off or on. 
        Set initial background music and sounds to medium level.
        """
        self.__is_running = True
        pygame.init()
        mixer.music.set_volume(0.4)
        mixer.Channel(0).set_volume(0.75)

    @property
    def is_running(self):
        """
        Getter for is_running status of all sounds
        :return: status of whether sounds are on
        :rtype: bool
        """
        return self.__is_running

    @is_running.setter
    def is_running(self, change):
        """
        Setter for is_running status of all sounds
        :param change: switching off or on of all sounds
        :type change: bool
        :raises: if param is not a boolean
        """
        if isinstance(change, bool):
            self.__is_running = change
        else:
            raise TypeError("Only boolean param accepted")

    def turn_off(self):
        """
        Turn off all sounds
        """
        self.__is_running = False
        mixer.quit()

    def turn_on(self, in_game=False):
        """
        Turn on all sounds, play intro music or in-game music depending
        on when this is called
        :param in_game: whether this is accessed at intro or in-game
        :type in_game: bool
        :raises: if param is not a boolean type
        """
        if isinstance(in_game, bool):
            self.__is_running = True
            mixer.init()
            mixer.music.set_volume(0.4)
            if in_game:
                self.in_game()
            else:
                self.intro()
        else:
            raise TypeError("Only boolean param accepted")

    def low_volume(self):
        """
        Set to low volume
        """
        if self.__is_running:
            mixer.music.set_volume(0.1)
            mixer.Channel(0).set_volume(0.25)  

    def normal_volume(self):
        """
        Set to normal/default volume
        """
        if self.__is_running:
            mixer.music.set_volume(0.4)
            mixer.Channel(0).set_volume(0.75)  

    def high_volume(self):
        """
        Set to high volume
        """
        if self.__is_running:
            mixer.music.set_volume(0.7)
            mixer.Channel(0).set_volume(1)  

    def intro(self):
        """
        Play intro music.
        """
        if self.__is_running:
            mixer.music.load(Path('title and filename,file.mp3'))
            mixer.music.play(-1)

    def in_game(self):
        """
        Play in-game music. Music for the game
        """
        if self.__is_running:
            mixer.music.load(Path('(title - file.mp3'))
            mixer.music.play(-1)

    def pause_menu(self, resume=False):
        """
        Pause music while in pause menu
        :param resume: allow resuming game music
        :type resume: bool
        """
        if resume:
            mixer.music.unpause()
        else:
            mixer.music.pause()

    def lose(self):
        """
        Music with player loses, obtained by Manny
        """
        if self.__is_running:
            mixer.music.load(Path('sound/file.mp3'))
            mixer.music.play(-1)

    def win(self):
        """
        Music with player wins,
        """
        if self.__is_running:
            mixer.music.load(Path('sound/file.mp3'))
            mixer.music.play(-1)

    def enter_room(self):
        """
        Sound for entering each room
        
        """
        if self.__is_running:
            # play a sound on channel 0 with a max time of 600 milliseconds
            mixer.Channel(0).play(pygame.mixer.Sound(Path('sound', 'file.mp3')), maxtime=600)

    def sound_winner(self):
        """
        Sound for collecting pillar key, by manny
        """
        if self.__is_running:
            mixer.Channel(1).play(pygame.mixer.Sound(Path('sound', 'file.mp3')))
    
    def sound_door_locked(self):
        """
        Sound for falling into pit, obtained by Manny
        """
        if self.__is_running:
            mixer.Channel(1).play(pygame.mixer.Sound(Path('sound', 'file.mp3')))
