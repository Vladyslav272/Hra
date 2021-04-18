import pygame
import sys

pygame.init()

sirka_okna = 800
vyska_okna = 600
FPS = 60

sirka_ctverce = 50
vyska_ctverce = 50
pozice_ctverce_x = (sirka_okna - sirka_ctverce) / 2
pozice_ctverce_y = 550
rychlost = 8

cerna = (0, 0, 0)
bila = (255, 255, 255)

#okno
okno = pygame.display.set_mode((sirka_okna, vyska_okna))
pygame.display.set_caption(("hra"))

while True:
    stisknuto = pygame.key.get_pressed()
    udalosti = pygame.event.get()
    
    for udalost in udalosti:
        if udalost.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    if stisknuto[pygame.K_ESCAPE]:
        pygame.quit()
        sys.exit()
        
    if stisknuto[pygame.K_RIGHT]:
        pozice_ctverce_x += rychlost
    if stisknuto[pygame.K_LEFT]:
        pozice_ctverce_x -= rychlost
    
    okno.fill(cerna)
    
    ctverec = pygame.draw.rect(okno, bila, ((pozice_ctverce_x, pozice_ctverce_y), (sirka_ctverce, vyska_ctverce)))
    pygame.display.update()