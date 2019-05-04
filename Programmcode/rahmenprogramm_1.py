# import random module
import random

Spieler1 = False
Spieler2 = False

while (Spieler1 == False):
    Spieler1 = input("Spieler 1 gib bitte eine Zahl zwischen 1-100 ein: ")

    try:
        Spieler1 = int(Spieler1)
    except:
        print("Du musst schon eine Zahl eingeben.")
        Spieler1 = False
        continue

    if Spieler1 > 100 or Spieler1 < 1:
        print("Deine Zahl muss zwischen 1-100 liegen.")
        Spieler1 = False

while (Spieler2 == False):
    Spieler2 = input("Spieler 2 gib bitte eine Zahl zwischen 1-100 ein: ")

    try:
        Spieler2 = int(Spieler2)
    except:
        print("Du musst schon eine Zahl eingeben.")
        Spieler2 = False
        continue

    if Spieler2 > 100 or Spieler2 < 1:
        print("Deine Zahl muss zwischen 1-100 liegen.")
        Spieler2 = False



random.seed()
Zufall = random.randint(1, 100)


#TODO: Schreibt ab hier euer Spiel