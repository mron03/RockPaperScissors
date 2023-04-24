import pygame
from menu import startMenu
from game import startGame

pygame.init()
WIDTH = 1500
HEIGHT = 1000
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("ROCK PAPER SCISSORS")

winner = ''

while True:
    
    if winner:
        VALUES = startMenu(winner)
    else:    
        VALUES = startMenu('')
    
    
    winner = startGame(VALUES)

    


