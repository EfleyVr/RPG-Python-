import random
import time
import os

#def perso
def Chevalier(Vie, Attaque1, Attaque2, Soin):
    Vie = 100
    Attaque1 = 15
    Attaque2 = 20
    Soin = 10
    return (Vie, Attaque1, Attaque2, Soin)

def Archet(Vie, Attaque1, Attaque2, Soin):
    Vie = 85
    Attaque1 = 20
    Attaque2 = 23
    Soin = 15
    return (Vie, Attaque1, Attaque2, Soin)

def Voleur(Vie, Attaque1, Attaque2, Soin):
    Vie = 55
    Attaque1 = 25
    Attaque2 = 35
    Soin = 12
    return (Vie, Attaque1, Attaque2, Soin)

def Mage(Vie, Attaque1, Attaque2, Soin):
    Vie = 115
    Attaque1 = 8
    Attaque2 = 16
    Soin = 25
    return (Vie, Attaque1, Attaque2, Soin)

#Accueil
def Accueil():
    choix_joueur = [1, 2, 3, 4]
    print("Choisis ton personnage :")
    time.sleep(0.3)
    print("1 → Le chevalier. Vie: 100pv ; Attaque 1: -15pv ; Attaque 2: -20pv ; Soin: +10pv")
    time.sleep(0.3)
    print("2 → L'archet. Vie: 85pv ; Attaque 1: -20pv ; Attaque 2: -23pv ; Soin: +15pv")
    time.sleep(0.3)
    print("3 → Le voleur. Vie: 55pv ; Attaque 1: -25pv ; Attaque 2: -35pv ; Soin: +12pv")
    time.sleep(0.3)
    print("4 → Le mage. Vie: 115pv ; Attaque 1: -8pv ; Attaque 2: -16pv ; Soin: +20pv")
    time.sleep(0.3)
    while True:
        try:
            PersoJ = int(input("→ "))
            if PersoJ in choix_joueur:
                break
            print("Erreur: choisis un personnage valide")
        except ValueError:
            print("Erreur: choisis un personnage valide")
    return(PersoJ)

NuméroPerso = {1:"Chevalier", 2:"Archet", 3:"Voleur", 4:"Mage"}
#Perso Joueur
os.system('cls')
input("Bienvenue sur votre jeu RPG.\nAppuyer sur entrer pour commencer [<⨼]")
while True:
    os.system('cls')
    PersoJ = Accueil()
    print("Tu as choisis", NuméroPerso[PersoJ])
    time.sleep(0.5)

    if PersoJ == 1:
        VieJ, Attaque1J, Attaque2J, SoinJ = Chevalier(0, 0, 0, 0)
    elif PersoJ == 2:
        VieJ, Attaque1J, Attaque2J, SoinJ = Archet(0, 0, 0, 0)
    elif PersoJ == 3:
        VieJ, Attaque1J, Attaque2J, SoinJ = Voleur(0, 0, 0, 0)
    else:
        VieJ, Attaque1J, Attaque2J, SoinJ = Mage(0, 0, 0, 0)

    #Perso Bot
    Choix_bot = [1, 2, 3, 4]
    PersoB = PersoJ
    while PersoB == PersoJ:
        PersoB = random.choice(Choix_bot)

    if PersoB == 1:
        VieB, Attaque1B, Attaque2B, SoinB = Chevalier(0, 0, 0, 0)
    elif PersoB == 2:
        VieB, Attaque1B, Attaque2B, SoinB = Archet(0, 0, 0, 0)
    elif PersoB == 3:
        VieB, Attaque1B, Attaque2B, SoinB = Voleur(0, 0, 0, 0)
    else:
        VieB, Attaque1B, Attaque2B, SoinB = Mage(0, 0, 0, 0)

    print("Le bot a choisis", NuméroPerso[PersoB])
    time.sleep(2.5)
    os.system('cls')

    mémoireJ = 0
    mémoireB = 0
    VieJM = VieJ
    VieBM = VieB
    manche = 0
    while True:
        actionJP = [1, 2, 3]
        #action joueur
        manche = manche + 1
        print("---------- Manche", manche, "----------")
        print("Vie Bot:", VieB, "pv ; Vie Joueur:", VieJ, "\nChoisis ton attaque.")
        time.sleep(0.3)
        print("1 → Attaque 1: -",Attaque1J,"pv")
        time.sleep(0.3)
        print("2 → Attaque 2: -",Attaque2J,"pv")
        time.sleep(0.3)
        print("3 → Soin: +",SoinJ,"pv")
        time.sleep(0.3)
        while True:
            try:
                actionJ = int(input("→ "))
                if actionJ in actionJP:
                    if actionJ == 2 and mémoireJ == 1:
                        print("Tu dois attendre le tour prochain pour utiliser 'Attaque 2'")
                    else:
                        break
                print("Erreur : Choisis une action correct.")
            except ValueError:
                print("Erreur : Choisis une action correct.")
        if actionJ == 1:
            mémoireJ = 0
            VieB = VieB - Attaque1J
            if VieB < 0:
                VieB = 0
            print("Tu as descendue la vie du bot à:", VieB)
            time.sleep(1)
        elif actionJ == 2:
            mémoireJ = 1
            VieB = VieB - Attaque2J
            if VieB < 0:
                VieB = 0
            print("Tu as descendue la vie du bot à:", VieB)
            time.sleep(1)
        else:
            mémoireJ = 0
            VieJ = VieJ + SoinJ
            if VieJ > VieJM:
                VieJ = VieJM
            print("Tu as remonter t'as vie à", VieJ)
            time.sleep(1)
        if VieB <= 0:
            break
        #action bot
        actionBP = [1, 1, 1, 2, 2, 3]
        actionBPC = [1, 1, 2]
        nom_action = {1:"Attaque 1", 2:"Attaque 2", 3:"Soin"}
        if VieB <= VieBM / 15:
            actionB = 3
        elif VieB <= VieBM / 2:
            chance_soin = random.random()
            if chance_soin <= 0.55:
                actionB = 3
            else:
                actionB = random.choice(actionBPC)
                while actionB == 2 and mémoireB == 1:
                    actionB = random.choice(actionBPC)
        else:
            actionB = random.choice(actionBP)
            while actionB == 2 and mémoireB == 1:
                actionB = random.choice(actionBP)
        time.sleep(0.6)
        print("Le bot à choisis", nom_action[actionB])
        time.sleep(1)
        if actionB == 1:
            mémoireB = 0
            VieJ = VieJ - Attaque1B
            if VieJ < 0:
                VieJ = 0
            print("Le bot a descendue t'as vie à", VieJ)
            time.sleep(1)
        elif actionB == 2:
            mémoireB = 1
            VieJ = VieJ - Attaque2B
            if VieJ < 0:
                VieJ = 0
            print("Le bot a descendue t'as vie à", VieJ)
            time.sleep(1)
        else:
            mémoireB = 0
            VieB = VieB + SoinB
            if VieB > VieBM:
                VieB = VieBM
            print("Le bot a remonté sa vie à", VieB)
            time.sleep(1)
        if VieJ <= 0:
            break
        time.sleep(1)
        os.system('cls')

    if VieB <= 0:
        print("Tu as gagner! Bravo.")
    else:
        print("Tu as perdus! Dommage.")
    continuer = ["o", "n"]
    while True:
        try:
            continuer_choix = str(input("Veux-tu rejouer ? o=oui n=non\n")).strip().lower()
            if continuer_choix in continuer:
                break
            print("Erreur : écris une réponsse valide.")
        except ValueError:
            print("Erreur : écris une réponsse valide.")
    time.sleep(0.5)
    if continuer_choix == "n":
        os.system('cls')
        print("Au revoir. Et à bientôt.")
        break