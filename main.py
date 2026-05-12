from tkinter import font

import pygame
import random
import numpy as np

pygame.init()
WIDTH = 800
HEIGHT = 600

prev_click = False
hamster = 200 
screen = pygame.display.set_mode((WIDTH, HEIGHT))
player = pygame.Rect(0, 200, 10, hamster)
padella = pygame.image.load("racchettae.png")
manico = pygame.image.load("manico.png")
playert = pygame.Rect(790, 200, 10, hamster)
padellat = pygame.image.load("racchettate.png")
maniaco = pygame.image.load("maniaco.png")
playeron = "PLAYER"
playerton = "BOT"
pwhy = pygame.font.SysFont("courier", 20, bold=True)
ptwhy = pygame.font.SysFont("courier", 20, bold=True)
poi = pygame.font.SysFont("courier", 20, bold=True)
buttomm= pygame.Rect(200,165,65,65)
racchettomm= pygame.image.load("racchetta.png")
buttoll= pygame.Rect(500,165,65,65)
racchettoll = pygame.image.load("racchettat.png")
buttopp= pygame.Rect(350,365,65,65)
pallopp= pygame.image.load("palla.png")
ostazioni= pygame.Rect(0,0,85,85)
imp=pygame.image.load("impostazioni.png")
L_P_G_C_C_C= pygame.Rect(400, 300, 10, 10)
speed = 1
offset = (L_P_G_C_C_C.centery - player.centery) / (player.height / 2)
score = 0
scoret = 0
scorev = pygame.font.SysFont("courier", 32, bold=True)
scoretv = pygame.font.SysFont("courier", 32, bold=True)
C_C_C = pygame.font.SysFont("courier", 20, bold=True)
P_C_C_C = pygame.Rect(0,30,65,65)
resume = pygame.font.SysFont("courier", 20, bold=True)
riso = pygame.Rect(0,HEIGHT//2-30,65,65)
leave = pygame.font.SysFont("courier", 20, bold=True)
pulsante = pygame.Rect(0,HEIGHT-30-65,65,65)
vy = offset * speed
vx = 1
R = 255
G = 255
B = 255
P_E_C_C_C = "off"
event = pygame.event.poll()
mod = "banana" 
WIDTH, HEIGHT = screen.get_size()
fullscreen = False
run = True
while run:
    key = pygame.key.get_pressed()
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    screen.fill((0, 195, 0))

    if mod == "banana":
        pygame.draw.rect(screen, (0,195,0), buttomm)
        pygame.draw.rect(screen, (0,195,0), buttoll)
        pygame.draw.rect(screen, (0, 195, 0), buttopp)
        screen.blit(racchettomm, (157,145))
        screen.blit(racchettoll, (467,145))
        screen.blit(pallopp, (305,325))
        racchettomm = pygame.transform.scale(racchettomm, (145, 145))
        racchettoll = pygame.transform.scale(racchettoll, (145, 145))
        pallopp = pygame.transform.scale(pallopp, (145, 145))
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
        cipenso=poi.render("START", False, (0,0,0))
        screen.blit(plo, ((200 if playeron == "PLAYER" else 215),185))
        screen.blit(ptlo, ((500 if playerton == "PLAYER" else 515),185))
        screen.blit(cipenso, (350,385))
        if buttopp.collidepoint(mouse) and click[0] and not prev_click:
            prev_mod=mod
            mod = "game"
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
            if P_E_C_C_C == "on":
                R = random.randint(50,255)
                G = random.randint(50,255)
                B = random.randint(50,255)
        elif L_P_G_C_C_C.colliderect(playert):
            offset = (L_P_G_C_C_C.centery - playert.centery) / (playert.height / 2)
            vy = offset * speed
            vx = -vx * 1.05
            if P_E_C_C_C == "on":
                R = random.randint(50,255)
                G = random.randint(0,50)
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
        screen.blit(padella, (player.x, player.y))
        padella = pygame.transform.scale(padella,(10, hamster))
        coy = player.y + player.height
        screen.blit(manico, (player.x-10, coy))
        screen.blit(padellat, (playert.x, playert.y))
        padellat = pygame.transform.scale(padellat,(10, hamster))
        coyt = playert.y + playert.height
        screen.blit(maniaco, (playert.x, coyt))
        pygame.draw.rect(screen, (((R,G,B) if P_E_C_C_C == "on" else (255,255,0))), L_P_G_C_C_C)
        score_text = scorev.render(str(score), False, (255, 255, 255))
        scoret_text = scoretv.render(str(scoret), False, (255, 255, 255))
        screen.blit(score_text, (250, 20))
        screen.blit(scoret_text, (500, 20))
        if hamster  >= 30:
            hamster -= 0.002
        player.height = hamster
        playert.height = hamster
        L_P_G_C_C_C.x -= vx
        L_P_G_C_C_C.y += vy
    screen.blit(imp, (0,0))
    if ostazioni.collidepoint(mouse) and click[0] and not prev_click and mod != "impostazioni":
        prev_mod = mod
        mod = "impostazioni"
        prev_click = True
        continue
    if mod == "impostazioni":
        screen.fill((100,100,100))
        if P_C_C_C.collidepoint(mouse) and click[0] and not prev_click:
            P_E_C_C_C = ("on" if P_E_C_C_C == "off" else "off")
        if pulsante.collidepoint(mouse) and click[0] and not prev_click:
            mod = "banana"
            hamster = 200
            player.height = hamster
            playert.height = hamster
            player.y = 200
            playert.y = 200
            L_P_G_C_C_C.center = (WIDTH // 2, HEIGHT // 2)
            score = 0
            scoret = 0
        if riso.collidepoint(mouse) and click[0] and not prev_click:
            mod = prev_mod
        P_E_C_C_C = P_E_C_C_C
        pygame.draw.rect(screen, ((random.randint(50,255), random.randint(50,255), random.randint(50,255)) if P_E_C_C_C == "on" else (255,255,0)), P_C_C_C)
        pygame.draw.rect(screen, (34, 197, 94), riso)
        pygame.draw.rect(screen, (255,0,0), pulsante)
        L_P_G_C_C_C_text = resume.render("la pallina cambia colore", False, (0,0,0))
        resume_text = leave.render("riprendi", False, (0,0,0))
        leave_text = leave.render("abbandona partita", False, (0,0,0))
        screen.blit(L_P_G_C_C_C_text, ((P_C_C_C.x+P_C_C_C.width), P_C_C_C.y))
        screen.blit(resume_text, ((riso.x+riso.width), riso.y))
        screen.blit(leave_text, ((pulsante.x+pulsante.width), pulsante.y))
    prev_click= click[0]
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_F11:
            fullscreen = not fullscreen
            if fullscreen:
                screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
            else:
                screen = pygame.display.set_mode((800,600))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.update()

pygame.quit() #io sono un commento ma non un commento normale, sono un commento speciale che serve a far capire che il programma è finito, e che non c'è più niente da eseguire, quindi se tu sei un essere umano e stai leggendo questo commento, vuol dire che hai finito di leggere tutto il codice, e che adesso puoi chiudere questo programma, oppure puoi eseguirlo se vuoi, ma se lo esegui, ricordati di chiuderlo quando hai finito, altrimenti potrebbe causare problemi al tuo computer, quindi chiudi questo programma quando hai finito di usarlo, e ricorda di non eseguirlo se non sai cosa fa, perché potrebbe essere pericoloso per il tuo computer, quindi fai attenzione quando esegui questo programma, e ricorda di chiuderlo quando hai finito.
#py -3.12 main.py