import pygame
import time

pygame.mixer.init()
pygame.font.init()
#pygame.init()

pygame.display.set_caption("Pythomon!")

myfont = pygame.font.SysFont('Arial Black', 30)  #c'est la police d'écriture


gameDisplay = pygame.display.set_mode((900,800))   #créer la surface d'affichage du jeu


bleu = (13,69,238)                                  #les couleurs
vert = (4,247,83)
rose = (242,13,237)
rouge = (231,24,24)
cyan = (95,252,240)
vertf = (36,107,29)
bleuf = (7,1,135)
rougef = (101,35,66)
noir = (1,1,1)
blanc = (255,255,255)


liste = []
fichier_texte = []




chant = pygame.mixer.Sound("sound/Champ_Select.ogg")
chant.play(2)




#-------------- Tous les sons -----------------------
#Sons qui se jouent lorsque le personnage est choisi
def Bonzai():
    pygame.mixer.music.load("sound/Banzai.mp3")
    pygame.mixer.music.play()

def Souffle():
    pygame.mixer.music.load("sound/Spectreur.mp3")
    pygame.mixer.music.play()

def pah():
    pygame.mixer.music.load("sound/Demonio10.mp3")
    pygame.mixer.music.play()

def fck():
    pygame.mixer.music.load("sound/Hagura1.mp3")
    pygame.mixer.music.play()

def fck2():
    pygame.mixer.music.load("sound/Hagura2.mp3")
    pygame.mixer.music.play()

def MageNwarSon():
    pygame.mixer.music.load("sound/MageNwar1.mp3")
    pygame.mixer.music.play()

#-----------------------------------------------------------

def a():                                            #permet d'actualiser l'affichage du tableau
    pygame.display.update()                         #c'est juste pour écrire a() au lieu de pygame.display.update()

def affiche(blaze,c,b):                             #permet d'afficher le personnage dans le tableau du dessous
    blaze = blaze + ".png"
    img = pygame.image.load(blaze)
    gameDisplay.blit(img,(c,b))


def dessinage():
    """
        Dessine les rectangles de l'écran
    """
    gameDisplay.fill(bleu)
    affiche("image/background",0,0)
    #pygame.draw.rect(gameDisplay, noir,(0,0,200,100))
    #pygame.draw.rect(gameDisplay, rouge,(2,2,196,96))
    affiche("image/cross",0,0)

    #pygame.draw.rect(gameDisplay, noir,(700,0,200,100))
    #pygame.draw.rect(gameDisplay, vert,(702,2,196,96))
    affiche("image/check",700,0)

    pygame.draw.rect(gameDisplay, noir,(0,450,900,300))
    affiche("image/barre",0,750)
    #pygame.draw.rect(gameDisplay, bleu,(0,750,900,50))



def verif():
    """
        Vérifie les booléens pour savoir si il faut afficher les personnages
        le résultat en gris ou en couleurs.

    """
    if not Hagura:
        affiche("image/Hagura1",250,150)
    elif Hagura:
        affiche("image/Hagura",250,150)
    if not MageNwar:
        affiche("image/Maj Nwar1",400,150)
    elif MageNwar:
        affiche("image/Maj Nwar",400,150)
    if not Demonio:
        affiche("image/Demonio1",550,150)
    elif Demonio:
        affiche("image/Demonio",550,150)
    if not Spectreur:
        affiche("image/Spectreur1",250,300)
    elif Spectreur:
        affiche("image/Spectreur",250,300)
    if not Banzai:
        affiche("image/Bonzai1",400,300)
    elif Banzai:
        affiche("image/Bonzai",400,300)

    affiche("image/Sans Titre",550,300)
    a()



#booléens qui permettront de vérifier si il faut que les personnages s'animent ou pas

animationSpectreur = True
animationMageNwar = True
animationHagura = True
animationDemonio = True
animationBonzai = True


def listage():
    """ fonction qui permet d'animer les personnages lorsqu'ils sont choisit
    """
    dessinage()
    for i in range(variable):
        affiche(liste[i],(300*i),450)
        Titre = myfont.render(liste[i][:-1][6:], False, blanc) #cette ligne affiche
        gameDisplay.blit(Titre,(((300*i)+50),750))             # le nom du personnage prit
        global animationHagura
        global animationDemonio
        global animationSpectreur
        global animationMageNwar
        global animationBonzai
        if (liste[i][:-1]) == "image/Hagura" and animationHagura:
            for n in range(3,8):
                affiche(("image/Hagura"+str(n)),(300*i),450)
                verif()
                fck()
                a()
                time.sleep(0.07)
            verif()
            a()

            animationHagura = False

        elif (liste[i][:-1]) == "image/Spectreur" and animationSpectreur:
            Souffle()
            for n in range(2,8):
                affiche(("image/Spectreur"+str(n)),(300*i),450)
                verif()

                a()
                time.sleep(0.07)
            verif()
            a()

            animationSpectreur = False



        elif (liste[i][:-1]) == "image/Maj Nwar" and animationMageNwar:
            MageNwarSon()
            for n in range(3,11):
                affiche(("image/Maj Nwar"+str(n)),(300*i),450)
                verif()
                a()
                time.sleep(0.04)
            verif()
            a()

            animationMageNwar = False


        elif (liste[i][:-1]) == "image/Demonio" and animationDemonio:
            affiche("image/Demonio2",(300*i),450)
            verif()
            a()
            time.sleep(0.06)
            for loop in range(3):
                affiche("image/Demonio3",(300*i),450)
                verif()
                a()
                time.sleep(0.06)
                affiche("image/Demonio2",(300*i),450)
                verif()
                a()
                time.sleep(0.06)

            animationDemonio = False

        elif (liste[i][:-1]) == "image/Bonzai" and animationBonzai:
            Bonzai()
            affiche("image/Bonzai2",(300*i),450)
            verif()
            a()
            time.sleep(0.1)
            for loop in range(2):
                for n in range(3,5):
                    affiche(("image/Bonzai"+str(n)),(300*i),450)
                    verif()
                    a()
                    time.sleep(0.09)
                a()
            affiche("image/Bonzai5",(300*i),450)
            verif()
            a()
            time.sleep(0.1)
            affiche("image/Bonzai2",(300*i),450)
            verif()
            a()

            animationBonzai = False


    verif()

def check(despi):
    """fonction qui permet de vérifier l'affichage des icones pour les print en couleur ou en monochrome
    """
    if despi == "image/Hagura2":
        global Hagura
        Hagura = True
    elif despi == "image/Maj Nwar2":
        global MageNwar
        MageNwar = True
    elif despi == "image/Demonio2":
        global Demonio
        Demonio = True
    elif despi == "image/Spectreur2":
        global Spectreur
        Spectreur = True
    elif despi == "image/Bonzai2":
        global Banzai
        Banzai = True
    verif()



Banzai = True
Hagura = True
MageNwar = True
Demonio = True
Spectreur = True

dessinage()
verif()




variable = 0
intro = True

while intro:
    ''' boucle de la selection de personnages '''
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN :
            if pygame.mouse.get_pressed() == (1,0,0):
                mouse = pygame.mouse.get_pos()
                if 250 < mouse[0] < 350 and 150 < mouse[1] < 250 and Hagura and len(liste) < 3:        #bouton Hagura
                    variable += 1
                    Hagura = False
                    liste.append("image/Hagura2")
                    listage()
                elif 400 < mouse[0] < 500 and 150 < mouse[1] < 250 and MageNwar and len(liste) < 3:    #bouton Mage Nwar
                    variable += 1
                    MageNwar = False
                    verif()
                    liste.append("image/Maj Nwar2")
                    listage()
                elif 550 < mouse[0] < 650 and 150 < mouse[1] < 250 and Demonio and len(liste) < 3:    #bouton Demonio
                    variable += 1
                    Demonio = False
                    liste.append("image/Demonio2")
                    pah()
                    listage()

                elif 250 < mouse[0] < 350 and 300 < mouse[1] < 400 and Spectreur and len(liste) < 3:   #bouton Spectreur
                    variable += 1
                    Spectreur = False
                    liste.append("image/Spectreur2")
                    listage()

                elif 400 < mouse[0] < 500 and 300 < mouse[1] < 400 and Banzai and len(liste) < 3:    #bouton Banzai
                    variable += 1
                    Banzai = False
                    Bonzai()
                    liste.append("image/Bonzai2")
                    listage()



                elif mouse[0] < 200 and mouse[1] < 100:
                    import menu

                elif 700 < mouse[0] < 900 and mouse[1] < 100 and len(liste) == 3:     #bouton vert -> permet d'écrire le nom des personnages dans un fichier texte afin de les récupérer dans le module suivant
                    with open("equipe.txt","w") as fo:
                        fo.write(liste[0] + '\n')
                        fo.write(liste[1] + '\n')
                        fo.write(liste[2])
                        affiche("art/LS_spectreur",0,0)
                        a()
                        chant.stop()
                        BoucleJeu = True
                        intro = False






                elif 0 < mouse[0] < 300 and 450 < mouse[1] < 750 and len(liste) >= 1:          #permet de retirer le premier personnage choisit
                    despi = liste[0]
                    check(despi)
                    del(liste[0])
                    variable -= 1
                    listage()
                    if despi == "image/Hagura2":
                        animationHagura = True
                    elif despi == "image/Demonio2":
                        animationDemonio = True
                    elif despi == "image/Maj Nwar2":
                        animationMageNwar = True
                    elif despi == "image/Spectreur2":
                        animationSpectreur = True
                    elif despi == "image/Bonzai2":
                        animationBonzai = True
                elif 300 < mouse[0] < 600 and 450 < mouse[1] < 750 and len(liste) >= 2:         #permet de retirer le deuxième personnage choisit
                    despi = liste[1]
                    check(despi)
                    del(liste[1])
                    variable -= 1
                    listage()
                    if despi == "image/Hagura2":
                        animationHagura = True
                    elif despi == "image/Demonio2":
                        animationDemonio = True
                    elif despi == "image/Maj Nwar2":
                        animationMageNwar = True
                    elif despi == "image/Spectreur2":
                        animationSpectreur = True
                    elif despi == "image/Bonzai2":
                        animationBonzai = True
                elif 600 < mouse[0] < 900 and 450 < mouse[1] < 750 and len(liste) >= 3:         #permet de retirer le troisième personnage choisit
                    despi = liste[2]
                    check(despi)
                    del(liste[2])
                    check(despi)
                    variable -= 1
                    listage()
                    if despi == "image/Hagura2":
                        animationHagura = True
                    elif despi == "image/Demonio2":
                        animationDemonio = True
                    elif despi == "image/Maj Nwar2":
                        animationMageNwar = True
                    elif despi == "image/Spectreur2":
                        animationSpectreur = True
                    elif despi == "image/Bonzai2":
                        animationBonzai = True
                elif 700< mouse[0] < 900 and mouse[1] < 100 and len(liste) == 3:        #lancement de la boucle jeu
                    BoucleJeu = True



while BoucleJeu:
    '''Affiche un écran de chargement lorsque l'on valide une équipe de 3 personnages et que l'on clique sur le bouton vert
    '''

    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print("O")
                import combat



