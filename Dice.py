from random import *
import pygame
import sys

from pygame import rect

"""SETTINGS"""

roll = 1

clock = pygame.time.Clock()
fps = 60

WHITE = (255, 255, 255)
GREY = (200, 200, 200)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

WIDTH = 520
HEIGHT = 500

bg = (255, 255, 255)

"""functions"""


def dice():
    global roll
    roll = randint(1, 6)
    print("You rolled a ", roll)


"""init"""

pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dice")

"""dice image"""

image = pygame.image.load("diceImage.gif").convert()
image2 = image.get_rect()
imageUsed = pygame.transform.scale(image, (WIDTH, HEIGHT))

"""text object"""
surf = pygame.Surface((WIDTH, 60))
font = pygame.font.SysFont("comicsansms", 37)
text = font.render("Click the dice to roll a number", True, (30, 128, 190))

surf2 = pygame.Surface((240, 90))

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            dice()
            mouse_pos = event.pos
            if image2.collidepoint(mouse_pos):
                print('button was pressed at {0}'.format(mouse_pos))

    text2 = font.render(("You rolled a " + str(roll)), True, (30, 128, 200))

    screen.fill(bg)
    screen.blit(imageUsed, (0, 0))
    screen.blit(surf, (0, 0))
    screen.blit(surf2, (130, 450))
    screen.blit(text, (0, 0))
    screen.blit(text2, (135, 450))
    pygame.display.update()
    clock.tick(fps)
