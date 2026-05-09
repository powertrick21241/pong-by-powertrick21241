import pygame
import random
import math
import numpy as np

pygame.init()
WIDTH = 800
HEIGHT = 600


hamster = 200
screen = pygame.display.set_mode((WIDTH, HEIGHT))
player = pygame.Rect(0, 200, 10, hamster)
playert = pygame.Rect(790, 200, 10, hamster)
playeron = "PLAYER"
playerton = "BOT"
pwhy = pygame.font.SysFont("courier", 20, bold=True)
ptwhy = pygame.font.SysFont("courier", 20, bold=True)
buttomm= pygame.Rect(200,165,100,70)
buttoll= pygame.Rect(500,165,100,70)
buttopp= pygame.Rect(350,365,100,70)
L_P_G_C_C_C= pygame.Rect(400, 300, 10, 10)
speed = 1
offset = (L_P_G_C_C_C.centery - player.centery) / (player.height / 2)
score = 0
scoret = 0
scorev = pygame.font.SysFont("courier", 32, bold=True)  # font di default, dimensione 50
scoretv = pygame.font.SysFont("courier", 32, bold=True)  # font di default, dimensione 50
vy = offset * speed
vx = 1
R = 255
G = 255
B = 255
mod = "banana"
run = True

while run:
    key = pygame.key.get_pressed()
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    screen.fill((0, 195, 0))

    if mod == "banana":
        pygame.draw.rect(screen, (255,255,255), buttomm)
        pygame.draw.rect(screen, (255,255,255), buttoll)
        pygame.draw.rect(screen, (255,255,255), buttopp)
        if buttomm.collidepoint(mouse) and click[0] and not prev_click:
            if playeron == "PLAYER":
                playeron = "BOT"
            elif playeron == "BOT":
                playeron = "PLAYER"
        if buttoll.collidepoint(mouse) and click[0] and not prev_click:
            if playerton == "PLAYER":
                playerton = "BOT"
            elif playerton == "BOT":
                playerton = "PLAYER"
        plo=pwhy.render(str(playeron), False, (0,0,0))
        ptlo=ptwhy.render(str(playerton), False, (0,0,0))
        screen.blit(plo, (200,165))
        screen.blit(ptlo, (500,165))
        if buttopp.collidepoint(mouse) and click[0] and not prev_click:
            mod = "game"
    prev_click= click[0]
    if mod == "game":
        if playeron == "PLAYER":
            if key[pygame.K_w] and player.y > 0:
                player.move_ip(0, -1)
            if key[pygame.K_s] and player.y < HEIGHT - player.height:
                player.move_ip(0, 1)
        
        if playerton == "PLAYER":
            if key[pygame.K_UP] and playert.y > 0:
                playert.move_ip(0, -1)
            if key[pygame.K_DOWN] and playert.y < HEIGHT - playert.height:
                playert.move_ip(0, 1)

        if L_P_G_C_C_C.colliderect(player):
            offset = (L_P_G_C_C_C.centery - player.centery) / (player.height / 2)
            vy = offset * speed
            vx = -vx * 1.05
            #if 
            R = random.randint(50,255)
            G = random.randint(50,255)
            B = random.randint(50,255)
        elif L_P_G_C_C_C.colliderect(playert):
            offset = (L_P_G_C_C_C.centery - playert.centery) / (playert.height / 2)
            vy = offset * speed
            vx = -vx * 1.05
            R = random.randint(50,255)
            G = random.randint(50,255)
            B = random.randint(50,255)
        if L_P_G_C_C_C.top <= 0 or L_P_G_C_C_C.bottom >= HEIGHT:
            vy = -vy
        if L_P_G_C_C_C.right >= WIDTH:
            score += 1
            L_P_G_C_C_C.center = (WIDTH // 2 - 200, HEIGHT // 2)
            vx = -1
            vy = 0

        if L_P_G_C_C_C.left <= 0:
            scoret += 1
            L_P_G_C_C_C.center = (WIDTH // 2 + 200, HEIGHT // 2)
            vx = 1
            vy = 0

        pygame.draw.rect(screen, (255,0,0), player)
        pygame.draw.rect(screen, (0,0,255), playert)
        pygame.draw.rect(screen, (R,G,B), L_P_G_C_C_C)
        score_text = scorev.render(str(score), False, (255, 255, 255))
        scoret_text = scoretv.render(str(scoret), False, (255, 255, 255))
        screen.blit(score_text, (250, 20))   # sinistra
        screen.blit(scoret_text, (500, 20))  # destra
        if hamster  >= 20:
            hamster -= 0.002
        player.height = hamster
        playert.height = hamster
        L_P_G_C_C_C.x -= vx
        L_P_G_C_C_C.y += vy


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.update()

pygame.quit()
#py -3.12 main.py