import pygame
import random
import time

pygame.mixer.init()
pygame.font.init()
pygame.init()
myfontp = pygame.font.Font("fonts/Pokemon Hollow.ttf", 100)
myfont_ = pygame.font.Font("fonts/Pokemon Solid.ttf", 130)
myfont = pygame.font.SysFont('Arial Black', 30)
crédits = pygame.font.SysFont("Source Sans Pro Black", 35)
youlo = pygame.font.Font("fonts/ZOMBIES REBORN.ttf", 310)
sky = pygame.font.Font("fonts/komicax.ttf", 130)
pygame.display.set_caption("Pythomon!")



gameDisplay = pygame.display.set_mode((900,800))
son = pygame.mixer.Sound("sound/bip.ogg")
yugi = pygame.mixer.Sound("sound/yugi.ogg")
binks = pygame.mixer.Sound("sound/fma.ogg")
binks2 = pygame.mixer.Sound("sound/fmab.ogg")
victory = pygame.mixer.Sound("sound/win.ogg")
#intro = True



bleu = (13,69,238) #les couleurs
vert = (4,247,83)
rose = (242,13,237)
rouge = (231,24,24)
cyan = (95,252,240)
vertf = (36,107,29)
bleuf = (7,1,135)
rougef = (101,35,66)
rougeg = (255, 43, 43)
noir = (0,0,0)
blanc = (255,255,255)
noir = (10,10,10)
jaune = (255, 255, 0)
jaunef = (255, 248, 5)


def menu ():
    intro = True
    img = pygame.image.load("art/end.png")
    gameDisplay.blit(img,(0,0))

    LoL = myfont_.render("PYTHOMON", False, noir) #création du titre
    gameDisplay.blit(LoL,(110,50))                      #affichage du titre

    LaL = myfontp.render("PLAY", False, noir) #création du titre
    gameDisplay.blit(LaL,(270,250))                  #affichage du titre

    LiL = myfontp.render("CREDITS", False, noir) #création du titre
    gameDisplay.blit(LiL,(250,450))                  #affichage du titre

    LeL = myfontp.render("EXIT", False, noir) #création du titre
    gameDisplay.blit(LeL,(270,650))                  #affichage du titre

    pygame.display.update()                             #refresh l'affichage


    while intro :
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            win()

def credit():

    babinks = True
    son.play()
    binks2.play()
    yugi.stop()
    gameDisplay.fill((0,0,0))
    pygame.draw.rect(gameDisplay, bleu,(0,0,900,220))
    pygame.draw.rect(gameDisplay, blanc,(18,758,133,30))
    LoL = myfont_.render("PYTHOMON", False, (12, 0, 205))
    gameDisplay.blit(LoL,(110,50))
    Dev = crédits.render("DEV     MIJOSE / TEDDY / YOUSSEF / MOHAMED", False, (255, 255, 255))
    gameDisplay.blit(Dev,(50,350))
    Stud = crédits.render("STUDIO     MTYM", False, (255, 255, 255))
    gameDisplay.blit(Stud,(50,400))
    Prix = crédits.render("PRIX     DISPONIBLE GRATUITEMENT", False, (255, 255, 255))
    gameDisplay.blit(Prix,(50,450))
    Chara = crédits.render("CHARACTER DESIGN     YOUSSEF / TEDDY ", False, (255, 255, 255))
    gameDisplay.blit(Chara,(50,500))
    Pyth2 = crédits.render("PYTHOMON 2 BIENTOT DISPONIBLE !", False, (255, 255, 255))
    gameDisplay.blit(Pyth2,(190,600))
    pygame.display.update()
    Ret = crédits.render("RETURN", False, noir)
    gameDisplay.blit(Ret,(20,750))
    pygame.display.update()




def win():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        Fin = True
        if Fin :
            co_y = 0
            binks2.stop()
            victory.play()
            gameDisplay.fill((0,0,0))
            pygame.draw.rect(gameDisplay, noir,(0,0,900,800))

            img = pygame.image.load("art/end.png")
            gameDisplay.blit(img,(50,co_y))

            pygame.display.update()
            time.sleep(3)
            while co_y > -2000 :
                gameDisplay.blit(img,(50,co_y))
                co_y -= 1
                pygame.display.update()
            Fin = False
        if not Fin:
            time.sleep(3)
            pygame.quit()
            quit()


win()