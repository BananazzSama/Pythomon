import pygame
import random
import time

pygame.mixer.init()
pygame.font.init()
#pygame.init()
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
    """
    Fonction qui permet d'afficher le menu principal du jeu contenant
    un bouton "PLAY" , "CREDITS" et "QUIT"

    La boucle "Tant que" ( while ) sert à créer les zones de cliquage

    """
    yugi.play(2)
    intro = True

    img = pygame.image.load("art/fond.jpg")
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
            lose()

def credit():
    """
    Fonction qui permet d'afficher les credits du jeu contenant
    un bouton "RETURN"

    La boucle "Tant que" ( while ) sert à créer les zones de cliquage

    """
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
    Lose = crédits.render("TEST LOSE", False, blanc)
    gameDisplay.blit(Lose,(330,750))
    Win = crédits.render("TEST WIN", False, blanc)
    gameDisplay.blit(Win,(720,750))
    pygame.display.update()                                     #fin écran crédits

def lose():
     mama = True
     binks2.stop()
     binks.play()
     gameDisplay.fill((0,0,0))
     pygame.draw.rect(gameDisplay, rougeg,(0,0,900,220))
     pygame.draw.rect(gameDisplay, rouge,(18,758,83,35))
     pygame.draw.rect(gameDisplay, rouge,(328,758,185,35))
     pygame.draw.rect(gameDisplay, rouge,(718,758,138,35))
     LoL = myfont_.render("PYTHOMON", False, (219, 23, 2))
     gameDisplay.blit(LoL,(110,50))

     Yol =  youlo.render("YOU LOSE !", False, (219, 23, 2))
     gameDisplay.blit(Yol,(120,310))

     Ret = crédits.render("QUIT", False, noir)
     gameDisplay.blit(Ret,(20,750))

     Play = crédits.render("PLAY AGAIN", False, noir)
     gameDisplay.blit(Play,(330,750))

     Cred = crédits.render("CREDITS", False, noir)
     gameDisplay.blit(Cred,(720,750))

     pygame.display.update()

     while mama:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if pygame.mouse.get_pressed() == (1,0,0):
                mouse = pygame.mouse.get_pos()
                if 0 < mouse[0] < 150 and 700 <  mouse[1] < 800 :
                    intro = False
                    son.play()
                    pygame.quit()
                if 325 < mouse[0] < 530 and 740 <  mouse[1] < 800 :
                    binks.stop()
                    son.play()
                    menu()
                if 715 < mouse[0] < 800 and 740 <  mouse[1] < 800 :
                    binks.stop()
                    son.play()
                    credit()

def win():
     mama = True
     binks2.stop()
     victory.play()
     gameDisplay.fill((0,0,0))
     pygame.draw.rect(gameDisplay, jaunef,(0,0,900,220))
     pygame.draw.rect(gameDisplay, blanc,(18,758,83,35))
     pygame.draw.rect(gameDisplay, blanc,(328,758,185,35))
     pygame.draw.rect(gameDisplay, blanc,(718,758,138,35))
     LoL = myfont_.render("PYTHOMON", False, blanc)
     gameDisplay.blit(LoL,(110,50))

     Yol =  sky.render("YOU WIN !", False, jaune )
     gameDisplay.blit(Yol,(120,310))

     Ret = crédits.render("QUIT", False,noir)
     gameDisplay.blit(Ret,(20,750))

     Play = crédits.render("PLAY AGAIN", False, noir)
     gameDisplay.blit(Play,(330,750))

     Cred = crédits.render("CREDITS", False, noir)
     gameDisplay.blit(Cred,(720,750))

     pygame.display.update()

     while mama:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if pygame.mouse.get_pressed() == (1,0,0):
                mouse = pygame.mouse.get_pos()
                if 0 < mouse[0] < 150 and 700 <  mouse[1] < 800 :
                    intro = False
                    son.play()
                    pygame.quit()
                if 325 < mouse[0] < 530 and 740 <  mouse[1] < 800 :
                    victory.stop()
                    son.play()
                    menu()
                if 715 < mouse[0] < 800 and 740 <  mouse[1] < 800 :
                    victory.stop()
                    son.play()
                    credit()



menu()