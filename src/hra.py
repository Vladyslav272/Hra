import pygame
import sys

sirka_okna = 800
vyska_okna = 600
FPS = 60

sirka_ctverce = 50
vyska_ctverce = 50
rychlost = 8

cerna = (0, 0, 0)
bila = (255, 255, 255)

#okno
okno = pygame.display.set_mode((sirka_okna, vyska_okna))
pygame.display.set_caption(("hra"))