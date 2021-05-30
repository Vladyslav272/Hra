import pygame
import sys

clock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption('Hra')

 
font = pygame.font.SysFont(None, 120)
 
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
    
#barvy
zelena = (0, 112, 0)

#obrazky pozadi
pozadi = pygame.image.load("Cartoon_Forest_BG_01.png")
pozadi_hra = pygame.image.load("Cartoon_Forest_BG_04.png")

#obrazky na animaci
golem1 = pygame.image.load("Golem1.png")
golem2 = pygame.image.load("Golem2.png")

g1 = pygame.image.load("Golem_1.png")
g2 = pygame.image.load("Golem_2.png")
g3 = pygame.image.load("Golem_3.png")
g4 = pygame.image.load("Golem_4.png")
g5 = pygame.image.load("Golem_5.png")
g6 = pygame.image.load("Golem_6.png")
g7 = pygame.image.load("Golem_7.png")
g8 = pygame.image.load("Golem_8.png")
g9 = pygame.image.load("Golem_9.png")
g10 = pygame.image.load("Golem_10.png")
g11 = pygame.image.load("Golem_11.png")
g12 = pygame.image.load("Golem_12.png")
g13 = pygame.image.load("Golem_13.png")
g14 = pygame.image.load("Golem_14.png")
g15 = pygame.image.load("Golem_15.png")
g16 = pygame.image.load("Golem_16.png")
g17 = pygame.image.load("Golem_17.png")
g18 = pygame.image.load("Golem_18.png")

j1 = pygame.image.load("image_1.png")
j2 = pygame.image.load("image_2.png")
j3 = pygame.image.load("image_3.png")
j4 = pygame.image.load("image_4.png")
j5 = pygame.image.load("image_5.png")
j6 = pygame.image.load("image_6.png")
j7 = pygame.image.load("image_7.png")
j8 = pygame.image.load("image_8.png")
j9 = pygame.image.load("image_9.png")
j10 = pygame.image.load("image_10.png")
j11 = pygame.image.load("image_11.png")
j12 = pygame.image.load("image_12.png")
j13 = pygame.image.load("image_13.png")
j14 = pygame.image.load("image_14.png")
j15 = pygame.image.load("image_15.png")
j16 = pygame.image.load("image_16.png")
j17 = pygame.image.load("image_17.png")
j18 = pygame.image.load("image_18.png")


#zvuky
hudba_pozadi = pygame.mixer.music.load("bensound-november.mp3")
hlasitost = pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play(1)

#uzivatelske parametry
sirka_okna = 1920
vyska_okna = 1080
sirka_tlacitka = 300
vyska_tlacitka = 100
pozice_x = (sirka_okna - sirka_tlacitka) /2
pozice_y = 200
pozice_y2 = pozice_y + 200

okno = pygame.display.set_mode((sirka_okna, vyska_okna))

click = False

#menu
def main_menu():
    
    while True:
        
        okno.blit(pozadi, (0, 0))
        
        mx, my = pygame.mouse.get_pos()
 
        button_1 = pygame.Rect(pozice_x, pozice_y, sirka_tlacitka, vyska_tlacitka)
        button_2 = pygame.Rect(pozice_x, pozice_y2, sirka_tlacitka, vyska_tlacitka)
        if button_1.collidepoint((mx, my)):
            if click:
                hra()
        if button_2.collidepoint((mx, my)):
            if click:
                vypnout()
        pygame.draw.rect(okno, (zelena), button_1)
        pygame.draw.rect(okno, (zelena), button_2)
        
        draw_text("Play", font, (255, 255, 255), okno, (pozice_x + 55), (pozice_y + 10))
        draw_text("Exit", font, (255, 255, 255), okno, (pozice_x + 55), (pozice_y2 + 10))
        
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        
        pygame.display.update()
        clock.tick(60) 

#hra
def hra():
    Golem = golem1
    pozice_golema_x = 50
    pozice_golema_y = 910
    sirka_golema = 200
    vyska_golema = 133
    rychlost = 3
    skok = False
    skok2 = 10
    animCount = 5
    
    walkRight = [g1, g2, g3, g4, g5, g6, g7, g8, g9, g10, g11, g12, g13, g14, g15, g16, g17, g18]
    walkLeft = [j1, j2, j3, j4, j5, j6, j7, j8, j9, j10, j11, j12, j13, j14, j15, j16, j17, j18]
    
    running = True
    while running: 
        okno.blit(pozadi_hra,(0, 0))
        
        stisknuto = pygame.key.get_pressed()
        udalosti = pygame.event.get()
        
        for udalost in udalosti:
            if udalost.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        if stisknuto[pygame.K_ESCAPE]:
            running = False
        
        #ovladani a animace
        if stisknuto[pygame.K_RIGHT]:
            pozice_golema_x += rychlost
            left = False
            right = True
            
        elif stisknuto[pygame.K_LEFT]:
            pozice_golema_x -= rychlost
            left = True
            right = False
            
        else:
            left = False
            right = False
            animCount = 0
            
        
        if not(skok):       
            if stisknuto[pygame.K_UP]:
                skok = True
                
        else:    
            if skok2 >= -10:
                if skok2 < 0:
                    pozice_golema_y += (skok2 ** 2) / 2    
                else:
                    pozice_golema_y -= (skok2 ** 2) /2
                skok2 -= 1              
            else:
                skok = False
                skok2 = 10
 
 
        if animCount + 1 >= 90:
            animCount = 0            
        if left:
            okno.blit(walkLeft[animCount // 5], (pozice_golema_x, pozice_golema_y))
            animCount += 1
        elif right:
            okno.blit(walkRight[animCount // 5], (pozice_golema_x, pozice_golema_y))
            animCount += 1
        else:
            okno.blit(Golem, (pozice_golema_x, pozice_golema_y))
        
        #omezeni pohybu
        if pozice_golema_x < 0:
            pozice_golema_x = 0
        elif pozice_golema_x + sirka_golema > sirka_okna:
            pozice_golema_x = sirka_okna - sirka_golema
        if pozice_golema_y < 0:
            pozice_golema_y = 0
        elif pozice_golema_y + vyska_golema > vyska_okna:
            pozice_golema_y = vyska_okna - vyska_golema
        
        pygame.display.update()
        clock.tick(60)
        
#vypinani 
def vypnout():
    running = True
    while running:
        pygame.quit()
        sys.exit()
 
main_menu()