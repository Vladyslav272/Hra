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

zelena = (0, 112, 0)


golem1 = pygame.image.load("Golem.png")
golem2 = pygame.image.load("Golem2.png")
pozadi = pygame.image.load("Cartoon_Forest_BG_01.png")
pozadi_hra = pygame.image.load("Cartoon_Forest_BG_04.png")


sirka_okna = 1920
vyska_okna = 1080
sirka_tlacitka = 300
vyska_tlacitka = 100

pozice_x = (sirka_okna - sirka_tlacitka) /2
pozice_y = 200
pozice_y2 = pozice_y + 200



okno = pygame.display.set_mode((sirka_okna, vyska_okna))

click = False
 
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
 
def hra():
    
    Golem = golem1
    pozice_golema_x = 50
    pozice_golema_y = 900
    sirka_golema = 200
    vyska_golema = 133
    rychlost = 10
    skok = False
    skok2 = 10
    
    
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
        
        #postava
        if stisknuto[pygame.K_LEFT]:
            Golem = golem2
        if stisknuto[pygame.K_RIGHT]:
            Golem = golem1
        
        #ovladani
        if stisknuto[pygame.K_RIGHT]:
            pozice_golema_x += rychlost
            
        if stisknuto[pygame.K_LEFT]:
            pozice_golema_x -= rychlost
        
        if not(skok):       
            if stisknuto[pygame.K_UP]:
                skok = True
                
        else:    
            if skok2 >= -20:
                if skok2 < 0:
                    pozice_golema_y += (skok2 ** 2) / 2
                    
                else:
                    pozice_golema_y -= (skok2 ** 2) /2
                
                skok2 -= 1
                
            else:
                skok = False
                skok2 = 10
            
        #omezeni pohybu
        if pozice_golema_x < 0:
            pozice_golema_x = 0
        elif pozice_golema_x + sirka_golema > sirka_okna:
            pozice_golema_x = sirka_okna - sirka_golema
        if pozice_golema_y < 0:
            pozice_golema_y = 0
        elif pozice_golema_y + vyska_golema > vyska_okna:
            pozice_golema_y = vyska_okna - vyska_golema
        
        okno.blit(pozadi_hra,(0, 0))
        okno.blit(Golem, (pozice_golema_x, pozice_golema_y))
        
        pygame.display.update()
        clock.tick(60)
 
def vypnout():
    running = True
    while running:
        pygame.quit()
        sys.exit()
 
main_menu()