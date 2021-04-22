import pygame
import sys
import pygame_menu

clock = pygame.time.Clock()
pygame.init()

sirka_okna = 1200
vyska_okna = 800
okno = pygame.display.set_mode((sirka_okna, vyska_okna))
pygame.display.set_caption(("hra"))

def start_the_game():
    while start_the_game:
        
        #uzivatelske parametry
        sirka_okna = 1200
        vyska_okna = 800
        FPS = 60
        sirka_ctverce = 20
        vyska_ctverce = 20
        pozice_ctverce_x = 800
        pozice_ctverce_y = 500
        rychlost = 8
        cerna = (0, 0, 0)
        bila = (255, 255, 255)
        
        okno = pygame.display.set_mode((sirka_okna, vyska_okna))

        stisknuto = pygame.key.get_pressed()
        udalosti = pygame.event.get()
        
        for udalost in udalosti:
            if udalost.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        if stisknuto[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()
        
        #ovladani
        if stisknuto[pygame.K_RIGHT]:
            pozice_ctverce_x += rychlost
        if stisknuto[pygame.K_LEFT]:
            pozice_ctverce_x -= rychlost
        if stisknuto[pygame.K_UP]:
            pozice_ctverce_y -= rychlost
        if stisknuto[pygame.K_DOWN]:
            pozice_ctverce_y += rychlost
        
        #omezeni pohybu
        if pozice_ctverce_x < 0:
            pozice_ctverce_x = 0
        if pozice_ctverce_x + sirka_ctverce > sirka_okna:
            pozice_ctverce_x = sirka_okna - sirka_ctverce
        if pozice_ctverce_y < 0:
            pozice_ctverce_y = 0
        if pozice_ctverce_y + vyska_ctverce > vyska_okna:
            pozice_ctverce_y = vyska_okna - vyska_ctverce
                
        okno.fill(cerna)
    
        #objekty
        ctverec = pygame.draw.rect(okno, bila, ((pozice_ctverce_x, pozice_ctverce_y), (sirka_ctverce, vyska_ctverce)))
        
        clock.tick(FPS)
        pygame.display.update()
    pass    
menu = pygame_menu.Menu("Welcome", 300, 400, theme=pygame_menu.themes.THEME_BLUE)

menu.add.button('Play', start_the_game)
menu.add.button('Quit', pygame_menu.events.EXIT)

menu.mainloop(okno)