from random import randint as rand
from time import sleep


def getValue(name, path):
    Fil = open(path, "r")
    vale = -1
    for i in Fil:
        pierw = ""
        Scrstr = ""
        for x in i:

            if pierw != name:
                pierw += x

            else:
                if x == "=":
                    continue

                if pierw == name:

                    if i.index("\n") == i.index(x):

                        vale = int(Scrstr)
                        break

                    else:

                        Scrstr += str(x)


    if vale != -1:
        return vale
    else:
        return -1









IS_PROGRAM_RUN = True
IS_GAME_RUN = False
GET_PATH_TO_SAVE_AND_READ = "Zapis.txt"
MAX_ROUND = 10
WCHIH_ROUND = 0

PAGE_GAME_COIN = 0
PLAYER_SCORE = 0
PLAYER_SCORE_GAME = 0
PLAYER_CHECK_GAME = 0
COMPUTER_SCORE_GAME = 0
COMPUTER_CHECK_GAME = 0

def getCheckValue(check):
    if check == 1:
        return "Orzel"
    elif check == 2:
        return "Reszka"

def printNewLine():
    print(" ")

def showRules():
   print("Gra w orła i reszkę")
   print("Obstawiasz wynik i rzucasz monetą")
   print("Gra toczy sie do 10 rzutów monetą")
   print("Rzucacie na przemian")
   print("Za trafienie otrzymujesz 10 punktów")
   print("Za porażke odejmuje 5")
   print("Kto ma wiecej punktów wygrywa")
   printNewLine()

def showMenu():
    print("Masz punktów:",str(PLAYER_SCORE))
    printNewLine()
    print("Menu:")
    print("G - Graj")
    print("Z - Zasady")
    print("E - Exit")
    printNewLine()


def zapisz():
    plikx = open(GET_PATH_TO_SAVE_AND_READ,"w")
    if plikx.writable():
        plikx.write("PLAYERSCORE="+str(PLAYER_SCORE) + "\n")
    plikx.close()

def wczytajPlik():
    global  PLAYER_SCORE
    try:
        plikx = open(GET_PATH_TO_SAVE_AND_READ,"r")
        if plikx.readline():
            PLAYER_SCORE = getValue("PLAYERSCORE",GET_PATH_TO_SAVE_AND_READ)
    except FileNotFoundError:
        plikx = open(GET_PATH_TO_SAVE_AND_READ, "w")
        if plikx.writable():
            plikx.write("PLAYERSCORE=0\n")
    plikx.close()


while IS_PROGRAM_RUN:
    wczytajPlik()
    zapisz()
    showMenu()


    print("Co chcesz zrobić?")
    odp = input(">> ")
    printNewLine()
    if odp.lower() == "g":
        WCHIH_ROUND += 1
        print("Runda:",WCHIH_ROUND)

        while WCHIH_ROUND != MAX_ROUND:
            printNewLine()
            print("Twoje punkty:", PLAYER_SCORE_GAME)
            print("Punkty komputera:", COMPUTER_SCORE_GAME)
            printNewLine()

            ruch = rand(1,6)
            if ruch <= 3:
                print("Twoje ruch! Podaj wartość (Orzel lub o, Reszka lub r)")

                odp = input(">> ")

                if odp.lower() == "orzel" or odp.lower() == "o":
                    PLAYER_CHECK_GAME = 1
                    COMPUTER_CHECK_GAME = 2
                elif odp.lower() == "reszka" or odp.lower() == "r":
                    PLAYER_CHECK_GAME = 2
                    COMPUTER_CHECK_GAME = 1
                else:
                    continue
            else:
                ruch = rand(1, 2)
                print("Ruch komputera")
                sleep(1)
                if ruch == 1:
                    PLAYER_CHECK_GAME = 2
                    COMPUTER_CHECK_GAME = 1
                elif ruch == 2:
                    PLAYER_CHECK_GAME = 1
                    COMPUTER_CHECK_GAME = 2
            sleep(1)
            printNewLine()
            print("Twoje wybór:", getCheckValue(PLAYER_CHECK_GAME))
            print("Wybór komputera:", getCheckValue(COMPUTER_CHECK_GAME))
            printNewLine()

            if PAGE_GAME_COIN == 0:
                print("Rzut! ...")
                PAGE_GAME_COIN = rand(1,5)
                WCHIH_ROUND +=1
                sleep(1)

                if PAGE_GAME_COIN > 3:
                    if PLAYER_CHECK_GAME == 1:
                        print("Wypadł orzeł!")
                        print("Tafiłes! otrzymujesz 10 puntków")
                        PLAYER_SCORE_GAME += 10
                        COMPUTER_SCORE_GAME -= 5
                    elif COMPUTER_CHECK_GAME == 1:
                        print("Wypadł orzeł!")
                        print("Przegrałeś :c tracisz 5 puntków")
                        PLAYER_SCORE_GAME -= 5
                        COMPUTER_SCORE_GAME += 10

                elif PAGE_GAME_COIN < 3:
                    if PLAYER_CHECK_GAME == 2:
                        print("Wypadła reszka!")
                        print("Tafiłes! otrzymujesz 10 puntków")
                        PLAYER_SCORE_GAME += 10
                        COMPUTER_SCORE_GAME -= 5
                    elif COMPUTER_CHECK_GAME == 2:
                        print("Wypadła reszka!")
                        print("Przegrałeś :c tracisz 5 puntków")
                        PLAYER_SCORE_GAME -= 5
                        COMPUTER_SCORE_GAME += 10

                else:
                    print("Moneta sie zgubiła")
                    print("Oboje tracicie 5 punktów")
                    PLAYER_SCORE_GAME -= 5
                    COMPUTER_SCORE_GAME -= 5
                PAGE_GAME_COIN = 0

        if PLAYER_SCORE_GAME < COMPUTER_SCORE_GAME:
            printNewLine()
            print("Twoje wybór:", getCheckValue(PLAYER_CHECK_GAME))
            print("Wybór komputera:", getCheckValue(COMPUTER_CHECK_GAME))
            print("Wygral komputer nie otrzymujesz punktów")
            printNewLine()
        elif PLAYER_SCORE_GAME > COMPUTER_SCORE_GAME:
            printNewLine()

            print("Twoje wybór:", getCheckValue(PLAYER_CHECK_GAME))
            print("Wybór komputera:", getCheckValue(COMPUTER_CHECK_GAME))
            print("Wygrałeś! Otrzymujesz 50 punktów")
            printNewLine()
            PLAYER_SCORE += 50
        else:
            printNewLine()

            print("Twoje wybór:", getCheckValue(PLAYER_CHECK_GAME))
            print("Wybór komputera:", getCheckValue(COMPUTER_CHECK_GAME))
            print("Remis! Otrzymujesz 10 punktów")
            PLAYER_SCORE += 10
            printNewLine()
        zapisz()
        WCHIH_ROUND = 0
        PAGE_GAME_COIN = 0
        PLAYER_SCORE_GAME = 0
        PLAYER_CHECK_GAME = 0
        COMPUTER_SCORE_GAME = 0
        COMPUTER_CHECK_GAME = 0
        continue
    elif odp.lower() == "z":
        showRules()
        continue
    elif odp.lower() == "e":
        IS_PROGRAM_RUN = False
        zapisz()
    else:

        continue