import pygame
import time
import random
import os
import auto_py_to_exe

pygame.init()
pygame.display.set_caption("Pythomon Combat Alpha")

pythomon_fighting = True
ostariointro = True
clicked = False
currentTurn = 0
bleu = (13,69,238)
blanc = (255,255,255)
noir = (0,0,0)
myfont = pygame.font.SysFont("calibri", 15)
comp = pygame.font.SysFont("calibri", 13)
#myfont = pygame.font.Font("dogicapixel.ttf", 15)
#comp = pygame.font.Font("dogicapixel.ttf", 13)

gameDisplay = pygame.display.set_mode((900,800))
img = pygame.image.load("prototype_interface3.png")
gameDisplay.blit(img,(0,0))

atkimg = pygame.image.load("combat/atk.png")

pygame.draw.rect(gameDisplay, noir,(301,630,600,200))
pygame.draw.rect(gameDisplay, bleu,(0,630,300,200))

boss_name = myfont.render("Ostario, Maître des devoreurs", False, (0, 0, 0))
text_rect = boss_name.get_rect(center=(900/2, 20))
gameDisplay.blit(boss_name, text_rect)

atk1 = myfont.render("Hagra", False, (0, 0, 0))
atk2 = myfont.render("Flash Tatane", False, (0, 0, 0))
atk3 = myfont.render("3", False, (0, 0, 0))
atk4 = myfont.render("4", False, (0, 0, 0))
atk5 = myfont.render("Châtiment", False, (0, 0, 0))
atk5_1 = myfont.render("Obscur", False, (0,0,0))
atk6 = myfont.render("Pulsar", False, (0, 0, 0))
atk6_1 = myfont.render("Sombre", False, (0, 0, 0))
atk7 = myfont.render("3", False, (0, 0, 0))
atk8 = myfont.render("4", False, (0, 0, 0))
atk9 = myfont.render("Empal'Flamme", False, (0, 0, 0))
atk10 = myfont.render("Empal'Flamme", False, (0, 0, 0))
atk11 = myfont.render("Empal'Flamme", False, (0, 0, 0))
atk12 = myfont.render("Empal'Flamme", False, (0, 0, 0))

blaze1 = ""
blaze2 = ""
blaze3 = ""

f = open("equipe.txt", "r")
blaze1 = (f.readline())
blaze2 = (f.readline())
blaze3 = (f.readline())

blaze1 = blaze1[6:][:-2]
blaze2 = blaze2[6:][:-2]
blaze3 = blaze3[6:][:-1]

theme = pygame.mixer.Sound("sound/fight.ogg")
theme.play(2)


#GESTION DES PYTHOMONS (VIE, ATTAQUE, ENERGIE)#
class personnage():
    def __init__(self, nbredeVie, nbredeVieMax, nomduPerso,): #on initialise de la class personnage.
        self.vie=nbredeVie
        self.vieMax=nbredeVieMax
        self.nom=nomduPerso
    def infos(self):
        print(str(self.nom) + " => " + "PV restants: " + str(self.vie))

#BOSS#
class Ostario(personnage):  #Ici on définit notre 1er boss, Ostario, le poisson-chat
    def __init__(self, nbredeVie, nbredeVieMax, nomduPerso):
        personnage.__init__(self, nbredeVie, nbredeVieMax, nomduPerso)

    def BulletDeCanon(self, cible1, cible2):
        nbreDegat = 13
        print('Ostario souffle des bulles explosives, cela inflige ' +str(nbreDegat))
        cible1.vie -= nbreDegat
        cible2.vie -= nbreDegat
        print("Ca sent le savon...")

class Hagura(personnage):  #on crée la class de notre premier personnage.
    def __init__(self, nbredeVie, nbredeVieMax, nomduPerso, nbrePE):
        personnage.__init__(self, nbredeVie, nbredeVieMax, nomduPerso)
        self.PE=nbrePE

    def affichePE(self):
        print(self.PE)

    def Hagra(self, cible): #Attaque 1
        nbreDegat = 30
        if self.PE >= 5:
            print('Hagura Hagar son opposant !, cela inflige ' +str(nbreDegat))
            cible.vie -= nbreDegat
            self.PE -= 5
            print("il reste "+str(self.PE) +"PE")
        else:
            print("Hagura n'a plus assez de colère")

    def FlashTatane(self, cible): #Attaque 2
        nbreDegat = 14
        chance = [1,2,3]
        coups = random.choice(chance)
        if self.PE >= 5 and coups == 1:
            print('Hagura tape 1 fois, cela inflige ' +str(nbreDegat))
            cible.vie -= nbreDegat
            self.PE -= 5
            print("il reste "+str(self.PE) +"PE")
        elif self.PE >= 5 and coups == 2:
            print('Hagura tape 2 fois, cela inflige ' +str(nbreDegat*1.5))
            cible.vie -= nbreDegat*1.5
            self.PE -= 5
            print("il reste "+str(self.PE) +"PE")
        elif self.PE >= 5 and coups == 3:
            print('Hagura fracasse son ennemi et tape 3 fois!, cela inflige ' +str(nbreDegat*2.2))
            cible.vie -= nbreDegat*2.2
            self.PE -= 5
            print("il reste "+str(self.PE) +"PE")
        else:
            print("Hagura n'a plus assez de colère")

class MajNwar(personnage):
    def __init__(self, nbredeVie, nbredeVieMax, nomduPerso, nbrePE):
        personnage.__init__(self, nbredeVie, nbredeVieMax, nomduPerso)
        self.PE=nbrePE

    def affichePE(self):
        print(self.PE)

    def ChatimentObscur(self, cible):
        nbreDegat = 45
        if self.PE >= 20:
            print('Maj Nwar châtie son opposant, cela inflige ' +str(nbreDegat))
            cible.vie -= nbreDegat
            self.PE -= 20
            print("il reste "+str(self.PE) +"PE")
        else:
            print("Arrête arrête, Maj Nwar n'a plus assez d'énergie sombre")

    def PulsarSombre(self, cible):
        nbreDegat = 30
        if self.PE >= 20:
            print('Maj Nwar déchaîne le Pulsar Sombre sur son ennemi, cela inflige ' +str(nbreDegat))
            cible.vie -= nbreDegat
            self.PE -= 20
            print("il reste "+str(self.PE) +"PE")
        else:
            print("Arrête arrête, Maj Nwar n'a plus assez d'énergie sombre")

class Demonio(personnage):
    def __init__(self, nbredeVie, nbredeVieMax, nomduPerso, nbrePE):
        personnage.__init__(self, nbredeVie, nbredeVieMax, nomduPerso)
        self.PE=nbrePE

    def affichePE(self):
        print(self.PE)

    def EmpalFlamme(self, cible):
        nbreDegat = 45
        if self.PE >= 20:
            print('Demonio empale violemment son ennemi , cela inflige ' +str(nbreDegat))
            cible.vie -= nbreDegat
            self.PE -= 20
            print("il reste "+str(self.PE) +"PE")
        else:
            print("Demonio n'a plus assez de PE")

    def Tartarus(self, cible):
        nbreDegat = 45
        if self.PE >= 20:
            print('Demonio emmène son ennemi au Tartarus, cela inflige ' +str(nbreDegat))
            cible.vie -= nbreDegat
            self.PE -= 20
            print("il reste "+str(self.PE) +"PE")
        else:
            print("Demonio n'a plus assez de PE")

    def SouffleEmbrase(self, cible):
        nbreDegat = 20

class Bonzai(personnage):
    def __init__(self, nbredeVie, nbredeVieMax, nomduPerso, nbrePE):
        personnage.__init__(self, nbredeVie, nbredeVieMax, nomduPerso)
        self.PE=nbrePE

    def affichePE(self):
        print(self.PE)

    def MauvaisePousse(self, cible):
        nbreDegat = 25
        if self.PE >= 20:
            print("Bonzai ordonne à sa plante d'attaquer, cela inflige " +str(nbreDegat))
            cible.vie -= nbreDegat
            self.PE -= 20
            print("il reste "+str(self.PE) +"PE")
        else:
            print("Bonzai n'a plus assez de PE")

    def df(self, cible):
        nbreDegat = 25
        if self.PE >= 20:
            print("Bonzai ordonne à sa plante d'attaquer, cela inflige " +str(nbreDegat))
            cible.vie -= nbreDegat
            self.PE -= 20
            print("il reste "+str(self.PE) +"PE")
        else:
            print("Bonzai n'a plus assez de PE")

class Spectreur(personnage):
    def __init__(self, nbredeVie, nbredeVieMax, nomduPerso, nbrePE):
        personnage.__init__(self, nbredeVie, nbredeVieMax, nomduPerso)
        self.PE=nbrePE

    def affichePE(self):
        print(self.PE)

    def FauxSpectrale(self, cible):
        nbreDegat = 35
        if self.PE >= 20:
            print("Spectreur tranche son ennemi par sa Faux Spectrale, cela inflige " +str(nbreDegat))
            cible.vie -= nbreDegat
            self.PE -= 20
            print("il reste "+str(self.PE) +"PE")
        else:
            print("Bonzai n'a plus assez de PE")

    def Backstab(self, cible):
        nbreDegat = 60
        chance = [0,0,0,0,0,0,0,0,0,1,1]
        coup = random.choice(chance)
        if self.PE >= 20 and coup == 0:
            print("Spectreur s'est fait repéré, il n'a infligé aucun dégat")
            self.PE -= 20
        elif self.PE >= 20 and coup == 1:
            print("Spectreur a planté son adversaire dans le dos, cela inflige " +str(nbreDegat))
            cible.vie -= nbreDegat
            self.PE -= 20
            print("il reste "+str(self.PE) +"PE")
        else:
            print("Spectreur n'a plus assez de PE")
    

#GESTION DES PYTHOMONS (VIE, ATTAQUE, ENERGIE)#


#INITIALISATION DES PYTHOMONS#
PLAYERHagura = Hagura(300, 300, "Hagura", 606060)
PLAYERMajNwar = MajNwar(250, 250, "Maj Nwar", 55)
PLAYERDemonio = Demonio(240, 240, "Demonio", 66)
PLAYERBonzai = Bonzai(350, 350, "Bonzai", 3000)
PLAYERSpectreur = Spectreur(200, 200, "Spectreur", 3000)
BOSSOstario = Ostario(1200, 1200, "Ostario, le Poisson-Chat")
#INITIALISATION DES PYTHOMONS#

def affiche1(blaze1,c,b):
    blaze1 = ("sprite/" + blaze1 + ".png")
    img1 = pygame.image.load(blaze1)
    gameDisplay.blit(img1,(c,b))

def affiche2(blaze2,c,b):
    blaze2 = ("sprite/" + blaze2 + ".png")
    img2 = pygame.image.load(blaze2)
    gameDisplay.blit(img2,(c,b))

def affiche3(blaze3,c,b):
    blaze3 = ("sprite/" + blaze3 + ".png")
    img3 = pygame.image.load(blaze3)
    gameDisplay.blit(img3,(c,b))

def tab_atk():
    gameDisplay.blit(atkimg,(0,634))
    gameDisplay.blit(atkimg,(152,634))
    gameDisplay.blit(atkimg,(0,718))
    gameDisplay.blit(atkimg,(152,718))

def boss_health_bar():
    bar_color = (153, 0, 204)
    bar_back_color = (60, 50, 61)

    bar_length = 500
    ratio = BOSSOstario.vieMax / bar_length

    pygame.draw.rect(gameDisplay, bar_back_color, (198, 38, BOSSOstario.vieMax / ratio + 4, 14))
    pygame.draw.rect(gameDisplay, bar_color, (200, 40, BOSSOstario.vie / ratio, 10))

def health_bar1():
    bar_color = (0, 230, 0)
    bar_back_color = (80, 91, 75)

    if PLAYERHagura.vie < 50:
        bar_color = (199, 23, 23)

    bar_length = 200

    if blaze1 == "Hagura":
        ratio = PLAYERHagura.vieMax / bar_length
        pygame.draw.rect(gameDisplay, bar_back_color, (48, 598, PLAYERHagura.vieMax / ratio + 4, 14))
        pygame.draw.rect(gameDisplay, bar_color, (50, 600, PLAYERHagura.vie / ratio, 10))
        mon_name = comp.render(str(PLAYERHagura.nom), False, (0, 0, 0))
        text_rect = mon_name.get_rect(center=(300/2, 585))
        gameDisplay.blit(mon_name, text_rect)
    elif blaze1 == "Maj Nwar":
        ratio = PLAYERMajNwar.vieMax / bar_length
        pygame.draw.rect(gameDisplay, bar_back_color, (48, 598, PLAYERMajNwar.vieMax / ratio + 4, 14))
        pygame.draw.rect(gameDisplay, bar_color, (50, 600, PLAYERMajNwar.vie / ratio, 10))
        mon_name = comp.render(str(PLAYERMajNwar.nom), False, (0, 0, 0))
        text_rect = mon_name.get_rect(center=(300/2, 585))
        gameDisplay.blit(mon_name, text_rect)
    elif blaze1 == "Demonio":
        ratio = PLAYERDemonio.vieMax / bar_length
        pygame.draw.rect(gameDisplay, bar_back_color, (48, 598, PLAYERDemonio.vieMax / ratio + 4, 14))
        pygame.draw.rect(gameDisplay, bar_color, (50, 600, PLAYERDemonio.vie / ratio, 10))
        mon_name = comp.render(str(PLAYERDemonio.nom), False, (0, 0, 0))
        text_rect = mon_name.get_rect(center=(300/2, 585))
        gameDisplay.blit(mon_name, text_rect)
    elif blaze1 == "Bonzai":
        ratio = PLAYERBonzai.vieMax / bar_length
        pygame.draw.rect(gameDisplay, bar_back_color, (48, 598, PLAYERBonzai.vieMax / ratio + 4, 14))
        pygame.draw.rect(gameDisplay, bar_color, (50, 600, PLAYERBonzai.vie / ratio, 10))
        mon_name = comp.render(str(PLAYERBonzai.nom), False, (0, 0, 0))
        text_rect = mon_name.get_rect(center=(300/2, 585))
        gameDisplay.blit(mon_name, text_rect)
    elif blaze1 == "Spectreur":
        ratio = PLAYERSpectreur.vieMax / bar_length
        pygame.draw.rect(gameDisplay, bar_back_color, (48, 598, PLAYERSpectreur.vieMax / ratio + 4, 14))
        pygame.draw.rect(gameDisplay, bar_color, (50, 600, PLAYERSpectreur.vie / ratio, 10))
        mon_name = comp.render(str(PLAYERSpectreur.nom), False, (0, 0, 0))
        text_rect = mon_name.get_rect(center=(300/2, 585))
        gameDisplay.blit(mon_name, text_rect)

def health_bar2():
    bar_color = (0, 230, 0)
    bar_back_color = (80, 91, 75)

    if PLAYERMajNwar.vie < 50:
        bar_color = (199, 23, 23)

    bar_length = 200

    if blaze2 == "Hagura":
        ratio = PLAYERHagura.vieMax / bar_length
        pygame.draw.rect(gameDisplay, bar_back_color, (348, 598, PLAYERHagura.vieMax / ratio + 4, 14))
        pygame.draw.rect(gameDisplay, bar_color, (350, 600, PLAYERHagura.vie / ratio, 10))
        mon_name = comp.render(str(PLAYERHagura.nom), False, (0, 0, 0))
        text_rect = mon_name.get_rect(center=(900/2, 585))
        gameDisplay.blit(mon_name, text_rect)
    elif blaze2 == "Maj Nwar":
        ratio = PLAYERMajNwar.vieMax / bar_length
        pygame.draw.rect(gameDisplay, bar_back_color, (348, 598, PLAYERMajNwar.vieMax / ratio + 4, 14))
        pygame.draw.rect(gameDisplay, bar_color, (350, 600, PLAYERMajNwar.vie / ratio, 10))
        mon_name = comp.render(str(PLAYERMajNwar.nom), False, (0, 0, 0))
        text_rect = mon_name.get_rect(center=(900/2, 585))
        gameDisplay.blit(mon_name, text_rect)
    elif blaze2 == "Demonio":
        ratio = PLAYERDemonio.vieMax / bar_length
        pygame.draw.rect(gameDisplay, bar_back_color, (348, 598, PLAYERDemonio.vieMax / ratio + 4, 14))
        pygame.draw.rect(gameDisplay, bar_color, (350, 600, PLAYERDemonio.vie / ratio, 10))
        mon_name = comp.render(str(PLAYERDemonio.nom), False, (0, 0, 0))
        text_rect = mon_name.get_rect(center=(900/2, 585))
        gameDisplay.blit(mon_name, text_rect)
    elif blaze2 == "Bonzai":
        ratio = PLAYERBonzai.vieMax / bar_length
        pygame.draw.rect(gameDisplay, bar_back_color, (348, 598, PLAYERBonzai.vieMax / ratio + 4, 14))
        pygame.draw.rect(gameDisplay, bar_color, (350, 600, PLAYERBonzai.vie / ratio, 10))
        mon_name = comp.render(str(PLAYERBonzai.nom), False, (0, 0, 0))
        text_rect = mon_name.get_rect(center=(900/2, 585))
        gameDisplay.blit(mon_name, text_rect)
    elif blaze2 == "Spectreur":
        ratio = PLAYERSpectreur.vieMax / bar_length
        pygame.draw.rect(gameDisplay, bar_back_color, (348, 598, PLAYERSpectreur.vieMax / ratio + 4, 14))
        pygame.draw.rect(gameDisplay, bar_color, (350, 600, PLAYERSpectreur.vie / ratio, 10))
        mon_name = comp.render(str(PLAYERSpectreur.nom), False, (0, 0, 0))
        text_rect = mon_name.get_rect(center=(900/2, 585))
        gameDisplay.blit(mon_name, text_rect)

def health_bar3():
    bar_color = (0, 230, 0)
    bar_back_color = (80, 91, 75)

    if PLAYERDemonio.vie < 50:
        bar_color = (199, 23, 23)

    bar_length = 200
    
    if blaze3 == "Hagura":
        ratio = PLAYERHagura.vieMax / bar_length
        pygame.draw.rect(gameDisplay, bar_back_color, (648, 598, PLAYERHagura.vieMax / ratio + 4, 14))
        pygame.draw.rect(gameDisplay, bar_color, (650, 600, PLAYERHagura.vie / ratio, 10))
        mon_name = comp.render(str(PLAYERHagura.nom), False, (0, 0, 0))
        text_rect = mon_name.get_rect(center=(1500/2, 585))
        gameDisplay.blit(mon_name, text_rect)
    elif blaze3 == "Maj Nwar":
        ratio = PLAYERMajNwar.vieMax / bar_length
        pygame.draw.rect(gameDisplay, bar_back_color, (648, 598, PLAYERMajNwar.vieMax / ratio + 4, 14))
        pygame.draw.rect(gameDisplay, bar_color, (650, 600, PLAYERMajNwar.vie / ratio, 10))
        mon_name = comp.render(str(PLAYERMajNwar.nom), False, (0, 0, 0))
        text_rect = mon_name.get_rect(center=(1500/2, 585))
        gameDisplay.blit(mon_name, text_rect)
    elif blaze3 == "Demonio":
        ratio = PLAYERDemonio.vieMax / bar_length
        pygame.draw.rect(gameDisplay, bar_back_color, (648, 598, PLAYERDemonio.vieMax / ratio + 4, 14))
        pygame.draw.rect(gameDisplay, bar_color, (650, 600, PLAYERDemonio.vie / ratio, 10))
        mon_name = comp.render(str(PLAYERDemonio.nom), False, (0, 0, 0))
        text_rect = mon_name.get_rect(center=(1500/2, 585))
        gameDisplay.blit(mon_name, text_rect)
    elif blaze3 == "Bonzai":
        ratio = PLAYERBonzai.vieMax / bar_length
        pygame.draw.rect(gameDisplay, bar_back_color, (648, 598, PLAYERBonzai.vieMax / ratio + 4, 14))
        pygame.draw.rect(gameDisplay, bar_color, (650, 600, PLAYERBonzai.vie / ratio, 10))
        mon_name = comp.render(str(PLAYERBonzai.nom), False, (0, 0, 0))
        text_rect = mon_name.get_rect(center=(1500/2, 585))
        gameDisplay.blit(mon_name, text_rect)
    elif blaze3 == "Spectreur":
        ratio = PLAYERSpectreur.vieMax / bar_length
        pygame.draw.rect(gameDisplay, bar_back_color, (648, 598, PLAYERSpectreur.vieMax / ratio + 4, 14))
        pygame.draw.rect(gameDisplay, bar_color, (650, 600, PLAYERSpectreur.vie / ratio, 10))
        mon_name = comp.render(str(PLAYERSpectreur.nom), False, (0, 0, 0))
        text_rect = mon_name.get_rect(center=(1500/2, 585))
        gameDisplay.blit(mon_name, text_rect)


def health_text():
    health = myfont.render(str(BOSSOstario.vie), False, (0, 0, 0))
    text_rect = health.get_rect(center=(900/2, 70))
    gameDisplay.blit(health, text_rect)

def ostario_intro():
    global ostariointro
    if ostariointro == True:
        ostario_intro_face = pygame.image.load("text/ostariofacetext.png")
        gameDisplay.blit(ostario_intro_face,(680,630))
        pygame.display.update()
        pygame.time.wait(1000)
        ostario_laugh = pygame.mixer.Sound("sound/ostario_laugh.ogg")
        ostario_laugh.play()
        text_anim("AHAHAHAHAHAHAHAHAHA!!!")
        pygame.time.wait(1000)
        refresh_console()
        gameDisplay.blit(ostario_intro_face,(680,630))
        pygame.display.update()
        text_anim("Vous pensez pouvoir me battre ?!")
        pygame.time.wait(1000)
        refresh_console()
        gameDisplay.blit(ostario_intro_face,(680,630))
        pygame.display.update()
        text_anim("MOI, OSTARIO ?!!!")
        pygame.time.wait(3000)
        ostariointro = False
tab_atk()

def text_anim(string):
    text = ''
    for i in range(len(string)):
        text += string[i]
        console = myfont.render(text, False, blanc)
        gameDisplay.blit(console,(320,660))
        pygame.display.update()
        pygame.time.wait(45)

def text_anim_2(string):
    text = ''
    for i in range(len(string)):
        text += string[i]
        console = myfont.render(text, False, blanc)
        gameDisplay.blit(console,(320,690))
        pygame.display.update()
        pygame.time.wait(45)

def text_anim_3(string):
    text = ''
    for i in range(len(string)):
        text += string[i]
        console = myfont.render(text, False, blanc)
        gameDisplay.blit(console,(320,720))
        pygame.display.update()
        pygame.time.wait(45)

def HaguraAttacks():
    tab_atk()
    refresh_console()
    console = myfont.render("Que doit faire Hagura ?", False, blanc)
    gameDisplay.blit(console,(320,660))
    gameDisplay.blit(atk1,(40,670))
    gameDisplay.blit(atk2,(155,670))
    pygame.display.update()

def MajNwarAttacks():
    tab_atk()
    refresh_console()
    console = myfont.render("Que doit faire Maj Nwar ?", False, blanc)
    gameDisplay.blit(console,(320,660))
    gameDisplay.blit(atk5,(25,660))
    gameDisplay.blit(atk5_1,(40,680))
    gameDisplay.blit(atk6,(175,660))
    gameDisplay.blit(atk6_1,(175,680))
    pygame.display.update()

def DemonioAttacks():
    tab_atk()
    refresh_console()
    console = myfont.render("Que doit faire Demonio ?", False, blanc)
    gameDisplay.blit(console,(320,660))
    gameDisplay.blit(atk9,(25,660))
    gameDisplay.blit(atk5_1,(40,680))
    pygame.display.update()

def BonzaiAttacks():
    tab_atk()
    refresh_console()
    console = myfont.render("Que doit faire Bonzai ?", False, blanc)
    gameDisplay.blit(console,(320,660))
    gameDisplay.blit(atk9,(25,660))
    gameDisplay.blit(atk5_1,(40,680))
    pygame.display.update()

def SpectreurAttacks():
    tab_atk()
    refresh_console()
    console = myfont.render("Que doit faire Spectreur ?", False, blanc)
    gameDisplay.blit(console,(320,660))
    gameDisplay.blit(atk9,(25,660))
    gameDisplay.blit(atk5_1,(40,680))
    pygame.display.update()

def refresh_console():
    pygame.draw.rect(gameDisplay, noir,(301,630,600,200))

def HaguraTurn():
    global clicked
    if event.type == pygame.MOUSEBUTTONDOWN :
                if pygame.mouse.get_pressed() == (1,0,0):
                    mouse = pygame.mouse.get_pos()
                    if 0 < mouse[0] < 148 and 630 < mouse[1] < 710:
                        print("ok")
                        pygame.time.wait(1000)
                        pygame.draw.rect(gameDisplay, noir,(301,630,600,200))
                        PLAYERHagura.Hagra(BOSSOstario)
                        text_anim("Hagura met une Hagra à son adversaire!")
                        pygame.time.wait(1000)
                        refresh_console()
                        text_anim("Cela inflige 30 degats!")
                        pygame.time.wait(1000)
                        tab_atk()
                        clicked = True

                    elif 152 < mouse[0] < 300 and 630 < mouse[1] < 710:
                        print("ok")
                        pygame.time.wait(1000)
                        pygame.draw.rect(gameDisplay, noir,(301,630,600,200))
                        PLAYERHagura.FlashTatane(BOSSOstario)
                        text_anim("Hagura lance Flash Tatane")
                        tab_atk()
                        clicked = True

def MajNwarTurn():
    global clicked
    if event.type == pygame.MOUSEBUTTONDOWN :
                if pygame.mouse.get_pressed() == (1,0,0):
                    mouse = pygame.mouse.get_pos()
                    if 0 < mouse[0] < 148 and 630 < mouse[1] < 710:
                        print("ok")
                        pygame.time.wait(1000)
                        pygame.draw.rect(gameDisplay, noir,(301,630,600,200))
                        PLAYERMajNwar.ChatimentObscur(BOSSOstario)
                        text_anim("Maj Nwar inflige un douloureux châtiment à")
                        text_anim_2("son ennemi !")
                        pygame.time.wait(1000)
                        refresh_console()
                        text_anim("Cela inflige 30 degats!")
                        pygame.time.wait(1000)
                        tab_atk()
                        clicked = True

                    elif 152 < mouse[0] < 300 and 630 < mouse[1] < 710:
                        print("ok")
                        pygame.time.wait(1000)
                        pygame.draw.rect(gameDisplay, noir,(301,630,600,200))
                        PLAYERMajNwar.PulsarSombre(BOSSOstario)
                        text_anim("Maj Nwar déchaine le Pulsar Sombre...")
                        pygame.time.wait(1000)
                        refresh_console()
                        text_anim("Cela inflige 30 degats!")
                        pygame.time.wait(1000)
                        tab_atk()
                        clicked = True

def DemonioTurn():
    global clicked
    if event.type == pygame.MOUSEBUTTONDOWN :
                if pygame.mouse.get_pressed() == (1,0,0):
                    mouse = pygame.mouse.get_pos()
                    if 0 < mouse[0] < 148 and 630 < mouse[1] < 710:
                        print("ok")
                        time.sleep(1)
                        pygame.draw.rect(gameDisplay, noir,(301,630,600,200))
                        PLAYERHagura.Hagra(BOSSOstario)
                        text_anim("Hagura met une Hagra à son adversaire!")
                        tab_atk()
                        clicked = True

                    elif 152 < mouse[0] < 300 and 630 < mouse[1] < 710:
                        print("ok")
                        time.sleep(1)
                        pygame.draw.rect(gameDisplay, noir,(301,630,600,200))
                        PLAYERHagura.FlashTatane(BOSSOstario)
                        text_anim("Hagura lance Flash Tatane")
                        tab_atk()
                        clicked = True

def BonzaiTurn():
    global clicked
    if event.type == pygame.MOUSEBUTTONDOWN :
                if pygame.mouse.get_pressed() == (1,0,0):
                    mouse = pygame.mouse.get_pos()
                    if 0 < mouse[0] < 148 and 630 < mouse[1] < 710:
                        print("ok")
                        time.sleep(1)
                        pygame.draw.rect(gameDisplay, noir,(301,630,600,200))
                        PLAYERHagura.Hagra(BOSSOstario)
                        text_anim("Hagura met une Hagra à son adversaire!")
                        tab_atk()
                        clicked = True

                    elif 152 < mouse[0] < 300 and 630 < mouse[1] < 710:
                        print("ok")
                        time.sleep(1)
                        pygame.draw.rect(gameDisplay, noir,(301,630,600,200))
                        PLAYERHagura.FlashTatane(BOSSOstario)
                        text_anim("Hagura lance Flash Tatane")
                        tab_atk()
                        clicked = True

def SpectreurTurn():
    global clicked
    if event.type == pygame.MOUSEBUTTONDOWN :
                if pygame.mouse.get_pressed() == (1,0,0):
                    mouse = pygame.mouse.get_pos()
                    if 0 < mouse[0] < 148 and 630 < mouse[1] < 710:
                        print("ok")
                        time.sleep(1)
                        pygame.draw.rect(gameDisplay, noir,(301,630,600,200))
                        PLAYERHagura.Hagra(BOSSOstario)
                        text_anim("Hagura met une Hagra à son adversaire!")
                        tab_atk()
                        clicked = True

                    elif 152 < mouse[0] < 300 and 630 < mouse[1] < 710:
                        print("ok")
                        time.sleep(1)
                        pygame.draw.rect(gameDisplay, noir,(301,630,600,200))
                        PLAYERHagura.FlashTatane(BOSSOstario)
                        text_anim("Hagura lance Flash Tatane")
                        tab_atk()
                        clicked = True

affiche1(blaze1,0,70)
affiche2(blaze2,0,230)
affiche3(blaze3,0,370)

while pythomon_fighting:

    boss_health_bar()
    health_bar1()
    health_bar2()
    health_bar3()
    ostario_intro()

    if currentTurn == 0:
        tab_atk()
        if blaze1 == "Hagura":
            HaguraAttacks()
        elif blaze1 == "Maj Nwar":
            MajNwarAttacks()
        elif blaze1 == "Demonio":
            DemonioAttacks()
        elif blaze1 == "Bonzai":
            BonzaiAttacks()
        elif blaze1 == "Spectreur":
            SpectreurAttacks()
    elif currentTurn == 1:
        tab_atk()
        if blaze2 == "Hagura":
            HaguraAttacks()
        elif blaze2 == "Maj Nwar":
            MajNwarAttacks()
        elif blaze2 == "Demonio":
            DemonioAttacks()
        elif blaze2 == "Bonzai":
            BonzaiAttacks()
        elif blaze2 == "Spectreur":
            SpectreurAttacks()
    elif currentTurn == 2:
        tab_atk()
        if blaze1 == "Hagura":
            HaguraAttacks()
        elif blaze3 == "Maj Nwar":
            MajNwarAttacks()
        elif blaze3 == "Demonio":
            DemonioAttacks()
        elif blaze3 == "Bonzai":
            BonzaiAttacks()
        elif blaze3 == "Spectreur":
            SpectreurAttacks()

    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if currentTurn == 0:
            if blaze1 == "Hagura":
                HaguraTurn()
            elif blaze1 == "Maj Nwar":
                MajNwarTurn()
            elif blaze1 == "Demonio":
                DemonioTurn()
            elif blaze1 == "Bonzai":
                BonzaiTurn()
            elif blaze1 == "Spectreur":
                SpectreurTurn()
            if clicked == True:
                currentTurn += 1
                clicked = False

        elif currentTurn == 1:
            if blaze2 == "Hagura":
                HaguraTurn()
            elif blaze2 == "Maj Nwar":
                MajNwarTurn()
            elif blaze2 == "Demonio":
                DemonioTurn()
            elif blaze2 == "Bonzai":
                BonzaiTurn()
            elif blaze2 == "Spectreur":
                SpectreurTurn()
            if clicked == True:
                currentTurn += 1
                clicked = False

        elif currentTurn == 2:
            if blaze3 == "Hagura":
                HaguraTurn()
            elif blaze3 == "Maj Nwar":
                MajNwarTurn()
            elif blaze3 == "Demonio":
                DemonioTurn()
            elif blaze3 == "Bonzai":
                BonzaiTurn()
            elif blaze3 == "Spectreur":
                SpectreurTurn()
            if clicked == True:
                currentTurn += 1
                clicked = False

        elif currentTurn == 3:
            currentTurn = 0