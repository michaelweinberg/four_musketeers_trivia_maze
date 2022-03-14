import pygame
from pygame import mixer
''' The Winning Sports cortesy of www.https://videvo.com
    and my coding skills
'''


def olympic_sound():

    pygame.init()
    mixer.music.load('Ultimate-Victory.wav')
    mixer.music.play(-1)

    try:
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
        pygame.quit()
    except SystemExit:
        pygame.quit()


olympic_sound()
