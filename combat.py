#On importe les modules dont on a besoin (PyGame, Time, Random et OS)
import pygame
import time
import random
import os


pygame.init() #On initialise PyGame
pygame.display.set_caption("Pythomon!") #Pour que le nom de la fenêtre soit Pythomon

pythomon_fighting = True #Pour valider la condition qui consiste a faire tourner la boucle de jeu
ostariointro = True #Booleen qui s'occupe de lancer l'intro du Boss : Ostario
clicked = False #Introduction du booleen "clicked" qui va vérifier si une attaque à été pressée pour passer au tour suivant
clock = pygame.time.Clock()

#COULEURS#
bleu = (13,69,238)
blanc = (255,255,255)
noir = (0,0,0)
#COULEURS#

#POLICES#
myfont = pygame.font.Font("fonts/dogicapixel.ttf", 15)
comp = pygame.font.Font("fonts/dogicapixel.ttf", 13)
#POLICES#

#INTRODUCTION DE PLUSIEURS DONNEES POUR LE JEU#
gameDisplay = pygame.display.set_mode((900,800))
imgfond = pygame.image.load("image/baron2.png")
gameDisplay.blit(imgfond,(0,0))

atkimg = pygame.image.load("combat/atk.png")

pygame.draw.rect(gameDisplay, noir,(301,630,600,200))
pygame.draw.rect(gameDisplay, bleu,(0,630,300,200))

boss_name = myfont.render("Ostario, Maître des devoreurs", False, (0, 0, 0))
text_rect = boss_name.get_rect(center=(900/2, 20))
gameDisplay.blit(boss_name, text_rect)

#HAGURA#
atk1 = myfont.render("Hagra", False, (0, 0, 0))
atk2 = myfont.render("Flash Tatane", False, (0, 0, 0))
atk3 = myfont.render("Hagura", False, (0, 0, 0))
atk3_1 = myfont.render("Fist", False, (0, 0, 0))
atk4 = myfont.render("Fracass", False, (0, 0, 0))
#HAGURA#

#MAJ NWAR#
atk5 = myfont.render("Châtiment", False, (0, 0, 0))
atk5_1 = myfont.render("Obscur", False, (0,0,0))
atk6 = myfont.render("Pulsar", False, (0, 0, 0))
atk6_1 = myfont.render("Sombre", False, (0, 0, 0))
atk7 = myfont.render("Deflagration", False, (0, 0, 0))
atk8 = myfont.render("Vanite", False, (0, 0, 0))
atk8_1 = myfont.render("Obscure", False, (0, 0, 0))
#MAJ NWAR#

#DEMONIO#
atk9 = myfont.render("Empal'", False, (0, 0, 0))
atk9_1 = myfont.render("Flamme", False, (0, 0, 0))
atk10 = myfont.render("Tartarus", False, (0, 0, 0))
atk11 = myfont.render("Souffle", False, (0, 0, 0))
atk11_1 = myfont.render("Embrase", False, (0, 0, 0))
atk12 = myfont.render("Naraku", False, (0, 0, 0))
#DEMONIO#

#SPECTREUR#
atk13 = myfont.render("Faux", False, (0, 0, 0))
atk13_1 = myfont.render("Spectrale", False, (0, 0, 0))
atk14 = myfont.render("Backstab", False, (0, 0, 0))
atk15 = myfont.render("Fauch'", False, (0, 0, 0))
atk15_1 = myfont.render("Ame", False, (0, 0, 0))
atk16 = myfont.render("Thanatos", False, (0, 0, 0))
#SPECTREUR#

#BONZAI#
atk17 = myfont.render("Mauvaise", False, (0, 0, 0))
atk17_1 = myfont.render("Pousse", False, (0, 0, 0))
atk18 = myfont.render("Bain de", False, (0, 0, 0))
atk18_1 = myfont.render("Soleil", False, (0, 0, 0))
atk19 = myfont.render("Main", False, (0, 0, 0))
atk19_1 = myfont.render("Verte", False, (0, 0, 0))
atk20 = myfont.render("Bamboula", False, (0, 0, 0))
#BONZAI#



#INTRODUCTION DE PLUSIEURS DONNEES POUR LE JEU#

#ICI ON S'OCCUPE DE TROUVER QUELS PYTHOMONS ONT ETES SELECTIONNE POUR LES INTRODUIRE DANS LA PARTIE COMBAT#
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
#ICI ON S'OCCUPE DE TROUVER QUELS PYTHOMONS ONT ETES SELECTIONNE POUR LES INTRODUIRE DANS LA PARTIE COMBAT#


theme = pygame.mixer.Sound("sound/fight.ogg") ####Musique du combat
theme.play(2) ####Musique du combat


#GESTION DES PYTHOMONS (VIE, ATTAQUE, ENERGIE)#
class personnage():
    def __init__(self, nbredeVie, nbredeVieMax, nomduPerso,): #On initialise de la classe personnage.
        """
            Initialisation de la classe qui gère les Pythomons (objet)
        """
        self.vie=nbredeVie
        self.vieMax=nbredeVieMax
        self.nom=nomduPerso
        if self.vie > self.vieMax:
            self.vie = self.vieMax
    def infos(self):
        """
            Fonction qui renvoie les PV restants du Pythomon
        """
        print(str(self.nom) + " => " + "PV restants: " + str(self.vie))

#BOSS#
class Ostario(personnage):  #Hérite de la classe PERSONNAGE #Ici on définit notre 1er boss, Ostario, le poisson-chat
    def __init__(self, nbredeVie, nbredeVieMax, nomduPerso):
        personnage.__init__(self, nbredeVie, nbredeVieMax, nomduPerso)

    def BulletDeCanon(self, cible): #Attaque 1
        nbreDegat = 20
        print('Ostario souffle des bulles explosives, cela inflige ' +str(nbreDegat))
        cible.vie -= nbreDegat
        print("Ca sent le savon...")

    def SplashRafale(self, cible1, cible2, cible3): #Attaque 2
        nbreDegat = 10
        print('Ostario rafale ses ennemis de gouttes toxiques, cela inflige ' +str(nbreDegat))
        cible1.vie -= nbreDegat
        cible2.vie -= nbreDegat
        cible3.vie -= nbreDegat

    def NuageToxique(self, cible1, cible2, cible3): #Attaque 3
        nbreDegat = 10
        print('Ostario lance une brume empoisonnée sur les ennemis, cela inflige ' +str(nbreDegat))
        cible1.vie -= nbreDegat
        cible2.vie -= nbreDegat
        cible3.vie -= nbreDegat
        print("Les Pythomons toussent")

    def KarateDesHommesPoissons(self, cible): #Attaque 4
        nbreDegat = 20
        print('Ostario met tout son ki dans son poing et foudroie son adversaire, cela inflige ' +str(nbreDegat))
        cible.vie -= nbreDegat

class Hagura(personnage):  #Hérite de la classe PERSONNAGE #Pythomon 1 - Hagura
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
            print('Hagura tape 2 fois, cela inflige ' +str(nbreDegat*2))
            cible.vie -= nbreDegat*2
            self.PE -= 5
            print("il reste "+str(self.PE) +"PE")
        elif self.PE >= 5 and coups == 3:
            print('Hagura fracasse son ennemi et tape 3 fois !, cela inflige ' +str(nbreDegat*2.6))
            cible.vie -= nbreDegat*2.6
            self.PE -= 5
            print("il reste "+str(self.PE) +"PE")
        else:
            print("Hagura n'a plus assez de PE")

    def HaguraFist(self, cible): #Attaque 3
        nbreDegat = 45
        if self.PE >= 10:
            print("Hagura s'élance armé de son Hagura Fist !, cela inflige " +str(nbreDegat))
            cible.vie -= nbreDegat
            self.PE -= 10
            print("il reste "+str(self.PE) +"PE")
        else:
            print("Hagura n'a plus assez de PE")

    def Fracass(self, cible): #Attaque 4
        nbreDegat = 50
        if self.PE >= 6:
            print("Hagura fracasse son adversaire !, il lui inflige" +str(nbreDegat))
            cible.vie -= nbreDegat
            self.PE -= 10
            print("il reste "+str(self.PE) +"PE")
        else:
            print("Hagura n'a plus assez de PE")

class MajNwar(personnage):  #Hérite de la classe PERSONNAGE #Pythomon 2 - Maj Nwar
    def __init__(self, nbredeVie, nbredeVieMax, nomduPerso, nbrePE):
        personnage.__init__(self, nbredeVie, nbredeVieMax, nomduPerso)
        self.PE=nbrePE

    def affichePE(self):
        print(self.PE)

    def ChatimentObscur(self, cible): #Attaque 1
        nbreDegat = 35
        if self.PE >= 20:
            print('Maj Nwar châtie son opposant, cela inflige ' +str(nbreDegat))
            cible.vie -= nbreDegat
            self.PE -= 20
            print("il reste "+str(self.PE) +"PE")
        else:
            print("Arrête arrête, Maj Nwar n'a plus assez de PE")

    def PulsarSombre(self, cible): #Attaque 2
        nbreDegat = 30
        if self.PE >= 20:
            print('Maj Nwar déchaîne le Pulsar Sombre sur son ennemi, cela inflige ' +str(nbreDegat))
            cible.vie -= nbreDegat
            self.PE -= 20
            print("il reste "+str(self.PE) +"PE")
        else:
            print("Arrête arrête, Maj Nwar n'a plus assez de PE")

    def Deflagration(self, cible): #Attaque 3
        nbreDegat = 25
        if self.PE >= 20:
            print('Maj Nwar génère une déflagration sur son ennemi, cela inflige ' +str(nbreDegat))
            cible.vie -= nbreDegat
            self.PE -= 20
            print("il reste "+str(self.PE) +"PE")
        else:
            print("Arrête arrête, Maj Nwar n'a plus assez de PE")

    def VaniteObscure(self, cible): #On crée une attaque pour notre personnage et elle infligue 40 dégats
        nbreDegat = 40
        if self.PE >= 5:
            print("Avec toute la vanite du monde il inflige " +str(nbreDegat))
            cible.vie -= nbreDegat
            self.PE -= 5
            print("il reste "+str(self.PE) +"PE")
        else:
            print("Arrête arrête, Maj Nwar n'a plus assez de PE")

class Demonio(personnage):  #Hérite de la classe PERSONNAGE #Pythomon 3 - Demonio
    def __init__(self, nbredeVie, nbredeVieMax, nomduPerso, nbrePE):
        personnage.__init__(self, nbredeVie, nbredeVieMax, nomduPerso)
        self.PE=nbrePE

    def affichePE(self):
        print(self.PE)

    def EmpalFlamme(self, cible): #Attaque 1
        nbreDegat = 45
        if self.PE >= 20:
            print('Demonio empale violemment son ennemi , cela inflige ' +str(nbreDegat))
            cible.vie -= nbreDegat
            self.PE -= 20
            print("il reste "+str(self.PE) +"PE")
        else:
            print("Demonio n'a plus assez de PE")

    def Tartarus(self, cible): #Attaque 2
        nbreDegat = 45
        if self.PE >= 20:
            print('Demonio emmène son ennemi au Tartarus, cela inflige ' +str(nbreDegat))
            cible.vie -= nbreDegat
            self.PE -= 20
            print("il reste "+str(self.PE) +"PE")
        else:
            print("Demonio n'a plus assez de PE")

    def SouffleEmbrase(self, cible): #Attaque 3
        nbreDegat = 45
        if self.PE >= 20:
            print('Demonio brûle son ennemi de son Souffle Embrasé, cela inflige ' +str(nbreDegat))
            cible.vie -= nbreDegat
            self.PE -= 20
            print("il reste "+str(self.PE) +"PE")
        else:
            print("Demonio n'a plus assez de PE")

    def Naraku(self, cible): #On crée une attaque pour notre personnage et elle infligue des dégât monstrueux
        nbreDegat = 40
        if self.PE >= 5:
            print("Frappe avec toutes les monstrueuses ténèbres qui l'habite et inflige " +str(nbreDegat))
            cible.vie -= nbreDegat
            self.PE -= 5
            print("il reste "+str(self.PE) +"PE")
        else:
            print("Demonio n'a plus assez de PE")

class Bonzai(personnage):  #Hérite de la classe PERSONNAGE #Pythomon 4 - Bonzai
    def __init__(self, nbredeVie, nbredeVieMax, nomduPerso, nbrePE):
        personnage.__init__(self, nbredeVie, nbredeVieMax, nomduPerso)
        self.PE=nbrePE

    def affichePE(self):
        print(self.PE)

    def MauvaisePousse(self, cible): #Attaque 1
        nbreDegat = 25
        if self.PE >= 20:
            print("Bonzai ordonne à sa plante d'attaquer, cela inflige " +str(nbreDegat))
            cible.vie -= nbreDegat
            self.PE -= 20
            print("il reste "+str(self.PE) +"PE")
        else:
            print("Bonzai n'a plus assez de PE")

    def MainVerte(self, cible): #On crée une attaque pour notre personnage et ele infligue 45 dégats
        nbreDegat = 35
        if self.PE >= 5:
            print("Bonzai Sort sa main de son pot et frappe avec sa MainVerte!, cela inflige " +str(nbreDegat))
            cible.vie -= nbreDegat
            self.PE -= 5
            print("il reste "+str(self.PE) +"PE")
        else:
            print("Bonzai n'a plus assez de PE")

    def BaindeSoleil(self, cible): #On crée une attaque pour notre personnage et elle ne sert a rien
        nbreDegat = 1
        if self.PE >= 5:
            print("Bonzai prend son meilleur bain de soleil, cela ne fait rien mais il prend son pied :)")
            cible.vie -= nbreDegat
            self.PE -= 5
            print("il reste "+str(self.PE) +"PE")
        else:
            print("Bonzai n'a plus assez de PE")

    def Bamboula(self, cible): #On crée une attaque pour notre personnage
        nbreDegat = 30
        if self.PE >= 5:
            print("Bonzai utilise plein de bambous, là..., cela inflige " +str(nbreDegat))
            cible.vie -= nbreDegat
            self.PE -= 5
            print("il reste "+str(self.PE) +"PE")
        else:
            print("Bonzai n'a plus assez de PE")

class Spectreur(personnage):  #Hérite de la classe PERSONNAGE #Pythomon 5 - Spectreur
    def __init__(self, nbredeVie, nbredeVieMax, nomduPerso, nbrePE):
        personnage.__init__(self, nbredeVie, nbredeVieMax, nomduPerso)
        self.PE=nbrePE

    def affichePE(self):
        print(self.PE)

    def FauxSpectrale(self, cible): #Attaque 1
        nbreDegat = 35
        if self.PE >= 20:
            print("Spectreur tranche son ennemi par sa Faux Spectrale, cela inflige " +str(nbreDegat))
            cible.vie -= nbreDegat
            self.PE -= 20
            print("il reste "+str(self.PE) +"PE")
        else:
            print("Spectreur n'a plus assez de PE")

    def Backstab(self, cible): #Attaque 2
        nbreDegat = 60
        if self.PE >= 20:
            print("Spectreur a planté son adversaire dans le dos, cela inflige " +str(nbreDegat))
            cible.vie -= nbreDegat
            self.PE -= 20
            print("il reste "+str(self.PE) +"PE")
        else:
            print("Spectreur n'a plus assez de PE")

    def Fauchame(self, cible):
        nbreDegat = 35
        if self.PE >= 5:
            print("Specteur armée de sa faux, fauche l'âme de son ennemi!, cela inflige " +str(nbreDegat))
            cible.vie -= nbreDegat
            self.PE -= 5
            print("il reste "+str(self.PE) +"PE")
        else:
            print("Spectreur n'a plus assez de PE")


    def Thanatos(self, cible):
        nbreDegat = 40
        if self.PE >= 5:
            print("Specteur devient le dieu de la mort et oblitère ca cible, cela inflige " +str(nbreDegat))
            cible.vie -= nbreDegat
            self.PE -= 5
            print("il reste "+str(self.PE) +"PE")
        else:
            print("Spectreur n'a plus assez de PE")


#GESTION DES PYTHOMONS (VIE, ATTAQUE, ENERGIE)#


#INITIALISATION DES PYTHOMONS#
PLAYERHagura = Hagura(300, 300, "Hagura", 99999999)
PLAYERMajNwar = MajNwar(250, 250, "Maj Nwar", 99999999)
PLAYERDemonio = Demonio(240, 240, "Demonio", 99999999)
PLAYERBonzai = Bonzai(355, 355, "Bonzai", 99999999)
PLAYERSpectreur = Spectreur(200, 200, "Spectreur", 99999999)
BOSSOstario = Ostario(100, 700, "Ostario")
#INITIALISATION DES PYTHOMONS#



def affiche1(blaze1,c,b):
    """
        Affiche le premier Pythomon de la liste
    """
    blaze1 = ("sprite/" + blaze1 + ".png")
    img1 = pygame.image.load(blaze1)
    gameDisplay.blit(img1,(c,b))

def affiche2(blaze2,c,b):
    """
        Affiche le second Pythomon de la liste
    """
    blaze2 = ("sprite/" + blaze2 + ".png")
    img2 = pygame.image.load(blaze2)
    gameDisplay.blit(img2,(c,b))

def affiche3(blaze3,c,b):
    """
        Affiche le dernier Pythomon de la liste
    """
    blaze3 = ("sprite/" + blaze3 + ".png")
    img3 = pygame.image.load(blaze3)
    gameDisplay.blit(img3,(c,b))

def tab_atk():
    """
        Permet de rafraîchir l'affichage des 4 arrières plans d'attaques
    """
    gameDisplay.blit(atkimg,(0,634))
    gameDisplay.blit(atkimg,(152,634))
    gameDisplay.blit(atkimg,(0,718))
    gameDisplay.blit(atkimg,(152,718))


def boss_health_bar():
    """
        Fonction qui gère la barre de vie du boss Ostario
    """
    bar_color = (153, 0, 204)
    bar_back_color = (60, 50, 61)

    bar_length = 500
    ratio = BOSSOstario.vieMax / bar_length

    pygame.draw.rect(gameDisplay, bar_back_color, (198, 38, BOSSOstario.vieMax / ratio + 4, 14))
    pygame.draw.rect(gameDisplay, bar_color, (200, 40, BOSSOstario.vie / ratio, 10))


def health_bar1():
    """
        Fonction qui gère la barre de vie du premier Pythomon
    """
    bar_color = (0, 230, 0)
    bar_back_color = (80, 91, 75)

    if PLAYERHagura.vie < 50:
        bar_color = (199, 23, 23)

    bar_length = 200

    #Liste de vérifications pour savoir quel Pythomon est en première place puis afficher sa barre de vie#
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
    """
        Fonction qui gère la barre de vie du deuxieme Pythomon
    """
    bar_color = (0, 230, 0)
    bar_back_color = (80, 91, 75)

    if PLAYERMajNwar.vie < 50:
        bar_color = (199, 23, 23)

    bar_length = 200

    #Liste de vérifications pour savoir quel Pythomon est en deuxième place puis afficher sa barre de vie#
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
    """
        Fonction qui gère la barre de vie du dernier Pythomon
    """
    bar_color = (0, 230, 0)
    bar_back_color = (80, 91, 75)

    if PLAYERDemonio.vie < 50:
        bar_color = (199, 23, 23)

    bar_length = 200

    #Liste de vérifications pour savoir quel Pythomon est en dernière place puis afficher sa barre de vie#
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
    """
        Fonction qui gère le nom du boss au dessus de sa barre de vie
    """
    health = myfont.render(str(BOSSOstario.vie), False, (0, 0, 0))
    text_rect = health.get_rect(center=(900/2, 70))
    gameDisplay.blit(health, text_rect)

def ostario_intro():
    """
        Fonction qui gère l'introduction dès que la partie est lancée du boss Ostario, Le Dévoreur des Marais'
    """
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
    """
        Fonction qui se charge d'animer l'affichage du texte dans la console du jeu
        Elle prend en paramètre le texte voulu
    """
    text = ''
    for i in range(len(string)):
        text += string[i]
        console = myfont.render(text, False, blanc)
        gameDisplay.blit(console,(320,660))
        pygame.display.update()
        pygame.time.wait(45)

def text_anim_2(string):
    """
        Fonction qui se charge d'animer l'affichage du texte dans la console du jeu, cette fois sur la seconde ligne (on s'en sert si le texte est long et dépasse de l'écran)
        Elle prend en paramètre le texte voulu
    """
    text = ''
    for i in range(len(string)):
        text += string[i]
        console = myfont.render(text, False, blanc)
        gameDisplay.blit(console,(320,690))
        pygame.display.update()
        pygame.time.wait(45)

def text_anim_3(string):
    """
        Fonction qui se charge d'animer l'affichage du texte dans la console du jeu, cette fois sur la troisième ligne (on s'en sert si le texte est long et dépasse de l'écran)
        Elle prend en paramètre le texte voulu
    """
    text = ''
    for i in range(len(string)):
        text += string[i]
        console = myfont.render(text, False, blanc)
        gameDisplay.blit(console,(320,720))
        pygame.display.update()
        pygame.time.wait(45)

def HaguraAttacks():
    """
        Fonction qui affiche les attaques de Hagura quand c'est à son tour
    """
    tab_atk()
    refresh_console()
    console = myfont.render("Que doit faire Hagura ?", False, blanc)
    gameDisplay.blit(console,(320,660))
    gameDisplay.blit(atk1,(40,670))
    gameDisplay.blit(atk2,(155,670))
    gameDisplay.blit(atk3,(40,740))
    gameDisplay.blit(atk3_1,(50,760))
    gameDisplay.blit(atk4,(180,752))
    pygame.display.update()

def MajNwarAttacks():
    """
        Fonction qui affiche les attaques de Maj Nwar quand c'est à son tour
    """
    tab_atk()
    refresh_console()
    console = myfont.render("Que doit faire Maj Nwar ?", False, blanc)
    gameDisplay.blit(console,(320,660))
    gameDisplay.blit(atk5,(25,660))
    gameDisplay.blit(atk5_1,(40,680))
    gameDisplay.blit(atk6,(175,660))
    gameDisplay.blit(atk6_1,(175,680))
    gameDisplay.blit(atk7,(3,752))
    gameDisplay.blit(atk8,(180,742))
    gameDisplay.blit(atk8_1,(180,762))
    pygame.display.update()

def DemonioAttacks():
    """
        Fonction qui affiche les attaques de Demonio quand c'est à son tour
    """
    tab_atk()
    refresh_console()
    console = myfont.render("Que doit faire Demonio ?", False, blanc)
    gameDisplay.blit(console,(320,660))
    gameDisplay.blit(atk9,(35,660))
    gameDisplay.blit(atk9_1,(29,680))
    gameDisplay.blit(atk10,(175,670))
    gameDisplay.blit(atk11,(32,740))
    gameDisplay.blit(atk11_1,(30,760))
    gameDisplay.blit(atk12,(186,752))
    pygame.display.update()

def BonzaiAttacks():
    """
        Fonction qui affiche les attaques de Bonzai quand c'est à son tour
    """
    tab_atk()
    refresh_console()
    console = myfont.render("Que doit faire Bonzai ?", False, blanc)
    gameDisplay.blit(console,(320,660))
    gameDisplay.blit(atk17,(25,660))
    gameDisplay.blit(atk17_1,(40,680))
    gameDisplay.blit(atk18,(175,660))
    gameDisplay.blit(atk18_1,(180,680))
    gameDisplay.blit(atk19,(48,740))
    gameDisplay.blit(atk19_1,(48,760))
    gameDisplay.blit(atk20,(176,752))
    pygame.display.update()

def SpectreurAttacks():
    """
        Fonction qui affiche les attaques de Spectreur quand c'est à son tour
    """
    tab_atk()
    refresh_console()
    console = myfont.render("Que doit faire Spectreur ?", False, blanc)
    gameDisplay.blit(console,(320,660))
    gameDisplay.blit(atk13,(50,660))
    gameDisplay.blit(atk13_1,(25,680))
    gameDisplay.blit(atk14,(175,670))
    gameDisplay.blit(atk15,(42,740))
    gameDisplay.blit(atk15_1,(47,760))
    gameDisplay.blit(atk16,(176,752))
    pygame.display.update()

def refresh_console():
    """
        Fonction qui va nettoyer la console du jeu pour pas que le nouveau texte soit superposé sur l'ancien
    """
    pygame.draw.rect(gameDisplay, noir,(301,630,600,200))

def HaguraTurn():
    """
        Fonction qui permet de gérer les entrées de la souris avec PyGame pour permettre d'intéragir avec Hagura et de lancer ses attaques quand c'est à son tour
    """
    global clicked
    if event.type == pygame.MOUSEBUTTONDOWN :
                if pygame.mouse.get_pressed() == (1,0,0):
                    mouse = pygame.mouse.get_pos()
                    if 0 < mouse[0] < 148 and 630 < mouse[1] < 710:
                        print("ok")
                        pygame.time.wait(1000)
                        pygame.draw.rect(gameDisplay, noir,(301,630,600,200))
                        PLAYERHagura.Hagra(BOSSOstario)
                        text_anim("Hagura met une Hagra à son adversaire !")
                        pygame.time.wait(1000)
                        refresh_console()
                        text_anim("Cela inflige 30 degats !")
                        pygame.time.wait(1000)
                        tab_atk()
                        clicked = True

                    elif 152 < mouse[0] < 300 and 630 < mouse[1] < 710:
                        print("ok")
                        pygame.time.wait(1000)
                        pygame.draw.rect(gameDisplay, noir,(301,630,600,200))
                        PLAYERHagura.FlashTatane(BOSSOstario)
                        text_anim("Hagura rafale son ennemi de Tatanes Fulgurantes !")
                        pygame.time.wait(1000)
                        refresh_console()
                        text_anim("Cela inflige 28 degats !")
                        pygame.time.wait(1000)
                        tab_atk()
                        clicked = True

                    elif 0 < mouse[0] < 148 and 718 < mouse[1] < 798:
                        print("ok")
                        pygame.time.wait(1000)
                        pygame.draw.rect(gameDisplay, noir,(301,630,600,200))
                        PLAYERHagura.HaguraFist(BOSSOstario)
                        text_anim("Hagura charge son Hagura Fist sur")
                        text_anim_2("l'adversaire")
                        pygame.time.wait(1000)
                        refresh_console()
                        text_anim("Cela inflige 45 degats !")
                        pygame.time.wait(1000)
                        tab_atk()
                        clicked = True

                    elif 152 < mouse[0] < 300 and 718 < mouse[1] < 798:
                        print("ok")
                        pygame.time.wait(1000)
                        pygame.draw.rect(gameDisplay, noir,(301,630,600,200))
                        PLAYERHagura.Fracass(BOSSOstario)
                        text_anim("Hagura FRACASSE l'opposant !!!!!!")
                        pygame.time.wait(1000)
                        refresh_console()
                        text_anim("Cela inflige 50 degats!")
                        pygame.time.wait(1000)
                        tab_atk()
                        clicked = True

def MajNwarTurn():
    """
        Fonction qui permet de gérer les entrées de la souris avec PyGame pour permettre d'intéragir avec Maj Nwar et de lancer ses attaques quand c'est à son tour
    """
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
                        text_anim("Cela inflige 35 degats !")
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
                        text_anim("Cela inflige 30 degats !")
                        pygame.time.wait(1000)
                        tab_atk()
                        clicked = True

                    elif 0 < mouse[0] < 148 and 718 < mouse[1] < 798:
                        print("ok")
                        pygame.time.wait(1000)
                        pygame.draw.rect(gameDisplay, noir,(301,630,600,200))
                        PLAYERMajNwar.Deflagration(BOSSOstario)
                        text_anim("Maj Nwar provoque une Deflagration")
                        text_anim_2("d'energie nwaaar sur l'adversaire !")
                        pygame.time.wait(1000)
                        refresh_console()
                        text_anim("Cela inflige 25 degats !")
                        pygame.time.wait(1000)
                        tab_atk()
                        clicked = True

                    elif 152 < mouse[0] < 300 and 718 < mouse[1] < 798:
                        print("ok")
                        pygame.time.wait(1000)
                        pygame.draw.rect(gameDisplay, noir,(301,630,600,200))
                        PLAYERMajNwar.VaniteObscure(BOSSOstario)
                        text_anim("Maj Nwar se vante auprès de son ennemi,")
                        text_anim_2("ce qui le blesse.")
                        pygame.time.wait(1000)
                        refresh_console()
                        text_anim("Cela inflige 40 degats !")
                        pygame.time.wait(1000)
                        tab_atk()
                        clicked = True

def DemonioTurn():
    """
        Fonction qui permet de gérer les entrées de la souris avec PyGame pour permettre d'intéragir avec Demonio et de lancer ses attaques quand c'est à son tour
    """
    global clicked
    if event.type == pygame.MOUSEBUTTONDOWN :
                if pygame.mouse.get_pressed() == (1,0,0):
                    mouse = pygame.mouse.get_pos()
                    if 0 < mouse[0] < 148 and 630 < mouse[1] < 710:
                        print("ok")
                        pygame.time.wait(1000)
                        pygame.draw.rect(gameDisplay, noir,(301,630,600,200))
                        PLAYERDemonio.EmpalFlamme(BOSSOstario)
                        text_anim("Demonio empale son ennemi de sa fourche")
                        text_anim_2("enflammée !")
                        pygame.time.wait(1000)
                        refresh_console()
                        text_anim("Cela inflige 45 degats !")
                        pygame.time.wait(1000)
                        tab_atk()
                        clicked = True

                    elif 152 < mouse[0] < 300 and 630 < mouse[1] < 710:
                        print("ok")
                        pygame.time.wait(1000)
                        pygame.draw.rect(gameDisplay, noir,(301,630,600,200))
                        PLAYERDemonio.Tartarus(BOSSOstario)
                        text_anim("Demonio emmène son adversaire au Tartare,")
                        text_anim_2("Royaume des Enfers")
                        pygame.time.wait(1000)
                        refresh_console()
                        text_anim("Cela inflige 45 degats !")
                        pygame.time.wait(1000)
                        tab_atk()
                        clicked = True

                    elif 0 < mouse[0] < 148 and 718 < mouse[1] < 798:
                        print("ok")
                        pygame.time.wait(1000)
                        pygame.draw.rect(gameDisplay, noir,(301,630,600,200))
                        PLAYERDemonio.SouffleEmbrase(BOSSOstario)
                        text_anim("Demonio brule l'ennemi de son Souffle")
                        text_anim_2("Embrase !")
                        pygame.time.wait(1000)
                        refresh_console()
                        text_anim("Cela inflige 45 degats !")
                        pygame.time.wait(1000)
                        tab_atk()
                        clicked = True

                    elif 152 < mouse[0] < 300 and 718 < mouse[1] < 798:
                        print("ok")
                        pygame.time.wait(1000)
                        pygame.draw.rect(gameDisplay, noir,(301,630,600,200))
                        PLAYERDemonio.Naraku(BOSSOstario)
                        text_anim("Demonio dechaine les enfers et frappe l'ennemi")
                        text_anim_2("de toute sa puissance")
                        pygame.time.wait(1000)
                        refresh_console()
                        text_anim("Cela inflige 40 degats !")
                        pygame.time.wait(1000)
                        tab_atk()
                        clicked = True

def BonzaiTurn():
    """
        Fonction qui permet de gérer les entrées de la souris avec PyGame pour permettre d'intéragir avec Bonzai et de lancer ses attaques quand c'est à son tour
    """
    global clicked
    if event.type == pygame.MOUSEBUTTONDOWN :
                if pygame.mouse.get_pressed() == (1,0,0):
                    mouse = pygame.mouse.get_pos()
                    if 0 < mouse[0] < 148 and 630 < mouse[1] < 710:
                        print("ok")
                        pygame.time.wait(1000)
                        pygame.draw.rect(gameDisplay, noir,(301,630,600,200))
                        PLAYERBonzai.MauvaisePousse(BOSSOstario)
                        text_anim("Bonzai ordonne à ses plantes d'attaquer !")
                        pygame.time.wait(1000)
                        refresh_console()
                        text_anim("Cela inflige 25 degats !")
                        pygame.time.wait(1000)
                        tab_atk()
                        clicked = True

                    elif 152 < mouse[0] < 300 and 630 < mouse[1] < 710:
                        print("ok")
                        pygame.time.wait(1000)
                        pygame.draw.rect(gameDisplay, noir,(301,630,600,200))
                        PLAYERBonzai.BaindeSoleil(BOSSOstario)
                        text_anim("Bonzai prend un petit un bain de soleil :D")
                        pygame.time.wait(1000)
                        tab_atk()
                        clicked = True

                    elif 0 < mouse[0] < 148 and 718 < mouse[1] < 798:
                        print("ok")
                        pygame.time.wait(1000)
                        pygame.draw.rect(gameDisplay, noir,(301,630,600,200))
                        PLAYERBonzai.MainVerte(BOSSOstario)
                        text_anim("Bonzai sort sa main de son pot et frappe")
                        text_anim_2("l'ennemi de sa Main Verte !")
                        pygame.time.wait(1000)
                        refresh_console()
                        text_anim("Cela inflige 35 degats !")
                        pygame.time.wait(1000)
                        tab_atk()
                        clicked = True

                    elif 152 < mouse[0] < 300 and 718 < mouse[1] < 798:
                        print("ok")
                        pygame.time.wait(1000)
                        pygame.draw.rect(gameDisplay, noir,(301,630,600,200))
                        PLAYERBonzai.Bamboula(BOSSOstario)
                        text_anim("Bonzai brandit ses bambous là et il attaque")
                        text_anim_2("son ennemi")
                        pygame.time.wait(1000)
                        refresh_console()
                        text_anim("Cela inflige 30 degats !")
                        pygame.time.wait(1000)
                        tab_atk()
                        clicked = True

def SpectreurTurn():
    """
        Fonction qui permet de gérer les entrées de la souris avec PyGame pour permettre d'intéragir avec Spectreur et de lancer ses attaques quand c'est à son tour
    """
    global clicked
    if event.type == pygame.MOUSEBUTTONDOWN :
                if pygame.mouse.get_pressed() == (1,0,0):
                    mouse = pygame.mouse.get_pos()
                    if 0 < mouse[0] < 148 and 630 < mouse[1] < 710:
                        print("ok")
                        pygame.time.wait(1000)
                        pygame.draw.rect(gameDisplay, noir,(301,630,600,200))
                        PLAYERSpectreur.FauxSpectrale(BOSSOstario)
                        text_anim("Spectreur tranche avec sa Faux Spectrale...")
                        pygame.time.wait(1000)
                        refresh_console()
                        text_anim("Cela inflige 35 degats !")
                        pygame.time.wait(1000)
                        tab_atk()
                        clicked = True

                    elif 152 < mouse[0] < 300 and 630 < mouse[1] < 710:
                        print("ok")
                        pygame.time.wait(1000)
                        pygame.draw.rect(gameDisplay, noir,(301,630,600,200))
                        PLAYERSpectreur.Backstab(BOSSOstario)
                        text_anim("!!!!!")
                        pygame.time.wait(1000)
                        refresh_console()
                        text_anim("Spectreur poignarde son ennemi dans le dos !")
                        pygame.time.wait(1000)
                        refresh_console()
                        text_anim("Cela inflige 60 degats !")
                        pygame.time.wait(1000)
                        tab_atk()
                        clicked = True

                    elif 0 < mouse[0] < 148 and 718 < mouse[1] < 798:
                        print("ok")
                        pygame.time.wait(1000)
                        pygame.draw.rect(gameDisplay, noir,(301,630,600,200))
                        PLAYERSpectreur.Fauchame(BOSSOstario)
                        text_anim("Spectreur s'élance armé de sa faux et")
                        text_anim_2("fauche l'ame de sa cible !")
                        pygame.time.wait(1000)
                        refresh_console()
                        text_anim("Cela inflige 35 degats !")
                        pygame.time.wait(1000)
                        tab_atk()
                        clicked = True

                    elif 152 < mouse[0] < 300 and 718 < mouse[1] < 798:
                        print("ok")
                        pygame.time.wait(1000)
                        pygame.draw.rect(gameDisplay, noir,(301,630,600,200))
                        PLAYERSpectreur.Thanatos(BOSSOstario)
                        text_anim("Spectreur se remplit de toute la puissance")
                        text_anim_2("de Thanatos, la mort elle meme !")
                        text_anim_3("Il frappe l'ennemi de toute sa force !")
                        pygame.time.wait(1000)
                        refresh_console()
                        text_anim("Cela inflige 40 degats !")
                        pygame.time.wait(1000)
                        tab_atk()
                        clicked = True

affiche1(blaze1,0,70) #Affiche le premier Pythomon en haut de l'écran
affiche2(blaze2,0,230) #Affiche le second Pythomon au milieu de l'écran
affiche3(blaze3,0,370) #Affiche le dernier Pythomon en bas de l'écran

currentTurn = 0 #Permet de garder une trace du tour en cours
#0 = premier pythomon
#1 = deuxieme pythomon
#2 = dernier pythomon
#3 = boss

while pythomon_fighting: #Boucle de jeu

    boss_health_bar()
    health_bar1()
    health_bar2()
    health_bar3()
    #ostario_intro()

    if blaze1 == "Hagura":
        pytho_1 = PLAYERHagura
        if PLAYERHagura.vie <= 0:
            dead1 = ("sprite/HaguraDead.png")
            deadimg1 = pygame.image.load(dead1)
            gameDisplay.blit(deadimg1,(0,70))
            pygame.display.update()
    elif blaze1 == "Maj Nwar":
        pytho_1 = PLAYERMajNwar
        if PLAYERMajNwar.vie <= 0:
            dead1 = ("sprite/Maj NwarDead.png")
            deadimg1 = pygame.image.load(dead1)
            gameDisplay.blit(deadimg1,(0,70))
            pygame.display.update()
    elif blaze1 == "Demonio":
        pytho_1 = PLAYERDemonio
        if PLAYERDemonio.vie <= 0:
            dead1 = ("sprite/DemonioDead.png")
            deadimg1 = pygame.image.load(dead1)
            gameDisplay.blit(deadimg1,(0,70))
            pygame.display.update()
    elif blaze1 == "Bonzai":
        pytho_1 = PLAYERBonzai
        if PLAYERBonzai.vie <= 0:
            dead1 = ("sprite/BonzaiDead.png")
            deadimg1 = pygame.image.load(dead1)
            gameDisplay.blit(deadimg1,(0,70))
            pygame.display.update()
    elif blaze1 == "Spectreur":
        pytho_1 = PLAYERSpectreur
        if PLAYERSpectreur.vie <= 0:
            dead1 = ("sprite/SpectreurDead.png")
            deadimg1 = pygame.image.load(dead1)
            gameDisplay.blit(deadimg1,(0,70))
            pygame.display.update()

    if blaze2 == "Hagura":
        pytho_2 = PLAYERHagura
        if PLAYERHagura.vie <= 0:
            dead2 = ("sprite/HaguraDead.png")
            deadimg2 = pygame.image.load(dead2)
            gameDisplay.blit(deadimg2,(0,230))
            pygame.display.update()
    elif blaze2 == "Maj Nwar":
        pytho_2 = PLAYERMajNwar
        if PLAYERMajNwar.vie <= 0:
            dead2 = ("sprite/Maj NwarDead.png")
            deadimg2 = pygame.image.load(dead2)
            gameDisplay.blit(deadimg2,(0,230))
            pygame.display.update()
    elif blaze2 == "Demonio":
        pytho_2 = PLAYERDemonio
        if PLAYERDemonio.vie <= 0:
            dead2 = ("sprite/DemonioDead.png")
            deadimg2 = pygame.image.load(dead2)
            gameDisplay.blit(deadimg2,(0,230))
            pygame.display.update()
    elif blaze2 == "Bonzai":
        pytho_2 = PLAYERBonzai
        if PLAYERBonzai.vie <= 0:
            dead2 = ("sprite/BonzaiDead.png")
            deadimg2 = pygame.image.load(dead2)
            gameDisplay.blit(deadimg2,(0,230))
            pygame.display.update()
    elif blaze2 == "Spectreur":
        pytho_2 = PLAYERSpectreur
        if PLAYERSpectreur.vie <= 0:
            dead2 = ("sprite/SpectreurDead.png")
            deadimg2 = pygame.image.load(dead2)
            gameDisplay.blit(deadimg2,(0,230))
            pygame.display.update()

    if blaze3 == "Hagura":
        pytho_3 = PLAYERHagura
        if PLAYERHagura.vie <= 0:
            dead3 = ("sprite/HaguraDead.png")
            deadimg3 = pygame.image.load(dead3)
            gameDisplay.blit(deadimg3,(0,370))
            pygame.display.update()
    elif blaze3 == "Maj Nwar":
        pytho_3 = PLAYERMajNwar
        if PLAYERMajNwar.vie <= 0:
            dead3 = ("sprite/Maj NwarDead.png")
            deadimg3 = pygame.image.load(dead3)
            gameDisplay.blit(deadimg3,(0,370))
            pygame.display.update()
    elif blaze3 == "Demonio":
        pytho_3 = PLAYERDemonio
        if PLAYERDemonio.vie <= 0:
            dead3 = ("sprite/DemonioDead.png")
            deadimg3 = pygame.image.load(dead3)
            gameDisplay.blit(deadimg3,(0,370))
            pygame.display.update()
    elif blaze3 == "Bonzai":
        pytho_3 = PLAYERBonzai
        if PLAYERBonzai.vie <= 0:
            dead3 = ("sprite/BonzaiDead.png")
            deadimg3 = pygame.image.load(dead3)
            gameDisplay.blit(deadimg3,(0,370))
            pygame.display.update()
    elif blaze3 == "Spectreur":
        pytho_3 = PLAYERSpectreur
        if PLAYERSpectreur.vie <= 0:
            dead3 = ("sprite/SpectreurDead.png")
            deadimg3 = pygame.image.load(dead3)
            gameDisplay.blit(deadimg3,(0,370))
            pygame.display.update()

    #Liste de vérifications pour afficher les bonnes attaques au bon moment
    if currentTurn == 0:
        tab_atk()
        if blaze1 == "Hagura":
            HaguraAttacks()
        elif blaze1 == "Maj Nwar":
            pass
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
        if blaze3 == "Hagura":
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

        #Vérifications pour savoir qui joue, à quel tour
        if currentTurn == 0:
            if pytho_1.vie <= 0:
                currentTurn += 1
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
            if pytho_2.vie <= 0:
                currentTurn += 1
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
            if pytho_3.vie <= 0:
                currentTurn += 1
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
            atkbosstab = [1,2,3,4]
            atkboss = random.choice(atkbosstab)
            if blaze1 == "Hagura":
                pytho_cible1 = PLAYERHagura
            elif blaze1 == "Maj Nwar":
                pytho_cible1 = PLAYERMajNwar
            elif blaze1 == "Demonio":
                pytho_cible1 = PLAYERDemonio
            elif blaze1 == "Bonzai":
                pytho_cible1 = PLAYERBonzai
            elif blaze1 == "Spectreur":
                pytho_cible1 = PLAYERSpectreur

            if blaze2 == "Hagura":
                pytho_cible2 = PLAYERHagura
            elif blaze2 == "Maj Nwar":
                pytho_cible2 = PLAYERMajNwar
            elif blaze2 == "Demonio":
                pytho_cible2 = PLAYERDemonio
            elif blaze2 == "Bonzai":
                pytho_cible2 = PLAYERBonzai
            elif blaze2 == "Spectreur":
                pytho_cible2 = PLAYERSpectreur

            if blaze3 == "Hagura":
                pytho_cible3 = PLAYERHagura
            elif blaze3 == "Maj Nwar":
                pytho_cible3 = PLAYERMajNwar
            elif blaze3 == "Demonio":
                pytho_cible3 = PLAYERDemonio
            elif blaze3 == "Bonzai":
                pytho_cible3 = PLAYERBonzai
            elif blaze3 == "Spectreur":
                pytho_cible3 = PLAYERSpectreur

            ciblerandom = [pytho_cible1, pytho_cible2, pytho_cible3]
            tab_atk()
            refresh_console()

            if atkboss == 1:
                choix_cible = random.choice(ciblerandom)
                BOSSOstario.BulletDeCanon(choix_cible)
                print("boss1")
                pygame.time.wait(1000)
                pygame.draw.rect(gameDisplay, noir,(301,630,600,200))
                text_anim("Ostario utilise Bullet de Canon et bombarde")
                text_anim_2(choix_cible.nom + " de Bulles Explosives !")
                pygame.time.wait(1000)
                refresh_console()
                text_anim("Cela inflige 20 degats !")
                pygame.time.wait(1000)
                tab_atk()
                currentTurn += 1
            elif atkboss == 2:
                choix_cible = random.choice(ciblerandom)
                BOSSOstario.KarateDesHommesPoissons(choix_cible)
                print("boss2")
                pygame.time.wait(1000)
                pygame.draw.rect(gameDisplay, noir,(301,630,600,200))
                text_anim("Ostario remplit son poing de Ki et utilise le")
                text_anim_2("Karaté des Hommes Poissons sur " + choix_cible.nom + " !")
                pygame.time.wait(1000)
                refresh_console()
                text_anim("Cela inflige 20 degats !")
                pygame.time.wait(1000)
                currentTurn += 1
                tab_atk()
            elif atkboss == 3:
                choix_cible1 = pytho_cible2
                choix_cible2 = pytho_cible2
                choix_cible3 = pytho_cible2
                BOSSOstario.SplashRafale(choix_cible1, choix_cible2, choix_cible3)
                print("boss3")
                pygame.time.wait(1000)
                pygame.draw.rect(gameDisplay, noir,(301,630,600,200))
                text_anim("Ostario rafale ses ennemis de gouttes toxiques !")
                pygame.time.wait(1000)
                refresh_console()
                text_anim("Cela inflige 10 degats !")
                pygame.time.wait(1000)
                tab_atk()
                currentTurn += 1
            elif atkboss == 4:
                choix_cible1 = pytho_cible3
                choix_cible2 = pytho_cible3
                choix_cible3 = pytho_cible3
                BOSSOstario.NuageToxique(choix_cible1, choix_cible2, choix_cible3)
                print("boss4")
                pygame.time.wait(1000)
                pygame.draw.rect(gameDisplay, noir,(301,630,600,200))
                text_anim("Ostario empoisonne la brume du Marais !")
                pygame.time.wait(1000)
                refresh_console()
                text_anim("Cela inflige 10 degats !")
                pygame.time.wait(1000)
                tab_atk()
                currentTurn += 1

    if currentTurn == 4:
        currentTurn = 0

    if pytho_1.vie <= 0 and pytho_2.vie <= 0 and pytho_3.vie <= 0:
        theme.stop()
        import lose
    elif BOSSOstario.vie <= 0:
        theme.stop()
        import win


        clock.tick(60)