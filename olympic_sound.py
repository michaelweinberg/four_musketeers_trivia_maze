import pygame
import time
from pygame import mixer


def olympic_sound():

    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((200, 100))
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
