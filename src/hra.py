import pygame
import sys

clock = pygame.time.Clock()
pygame.init()

sirka_okna = 1200
vyska_okna = 800
FPS = 60

sirka_ctverce = 20
vyska_ctverce = 20
pozice_ctverce_x = sirka_okna * -1
pozice_ctverce_y = vyska_okna
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
    if stisknuto[pygame.K_UP]:
        pozice_ctverce_y -= rychlost
    if stisknuto[pygame.K_DOWN]:
        pozice_ctverce_y += rychlost
    
    if pozice_ctverce_x < 0:
        pozice_ctverce_x = 0
    if pozice_ctverce_x + sirka_ctverce > sirka_okna:
        pozice_ctverce_x = sirka_okna - sirka_ctverce
    if pozice_ctverce_y < 0:
        pozice_ctverce_y = 0
    if pozice_ctverce_y + vyska_ctverce > vyska_okna:
        pozice_ctverce_y = vyska_okna - vyska_ctverce
        
        
    okno.fill(cerna)
    
    ctverec = pygame.draw.rect(okno, bila, ((pozice_ctverce_x, pozice_ctverce_y), (sirka_ctverce, vyska_ctverce)))
    clock.tick(FPS)
    pygame.display.update()