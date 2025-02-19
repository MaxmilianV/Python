from random import choice
from time import sleep
choices = ["r", "p", "s"] #Z tohohle si počítač vybere
Dchoice = { #Tenhle slovník tu máme abychom převedli to co zadá hráč a počítač na slova
    "r": "Rock",
    "s": "Scissors",
    "p": "Paper"
} 

Pscore = 0
Cscore = 0
def game(choiceList:list,):
    global Pscore
    global Cscore
    Dchoice = { #Tenhle slovník tu máme abychom převedli to co zadal hráč na slova
        "r": "Rock",
        "s": "Scissors",
        "p": "Paper"
    } 
    Pchoice = input("Choose your move! Type R for rock, P for paper and S for scissors ") #Tady zadá hráč co chce vybrat
    while Pchoice.lower() not in choiceList: #While loop tady je aby se to hráče ptalo na volbu dokud nevybere něco z choices listu
        Pchoice = input("Choose your move! Type R for rock, P for paper and S for scissors ")
    Cchoice = choice(choiceList) #Tady si pomocí funkce choice() vybere počítač něco z choices listu
    print(f"You chose: {Dchoice[Pchoice]}") #V tomhle f stringu se převede písmeno na slovo a řekne hráči co kdo vybral.
    sleep(0.5)
    print(f"The computer chose: {Dchoice[Cchoice]}")
    sleep(0.5)
    if Pchoice.lower() == Cchoice: # Jestli vybral hráč i počítač to samé tak to dá remízu, a nepřipočte to bod nikomu
        print(f"Draw! The score is now {Pscore}:{Cscore}" "\n")
    elif Pchoice.lower() == "p" and Cchoice == "r": #Tady jsem použil 3 elif řádky na všechny možnosti výhry.
        Pscore +=  1 #Tady to připočte bod hráči
        print(f"You won! The score is now {Pscore}:{Cscore}" "\n")
    elif Pchoice.lower() == "r" and Cchoice == "s":
        Pscore +=  1
        print(f"You won! The score is now {Pscore}:{Cscore}" "\n")
    elif Pchoice.lower() == "s" and Cchoice == "p":
        Pscore +=  1
        print(f"You won! The score is now {Pscore}:{Cscore}" "\n")
    else: #Teď už máme vyřešené možnosti remízy i výhry, takže jediný co nám zbývá je prohra.
        Cscore += 1 #Tady to připočte bod počítači
        print(f"You lost! The score is now {Pscore}:{Cscore}" "\n")
        
def get_rounds(): #Tahle funkce je tu aby jsme zjistili kolik kol chce hráč hrát
    try:
        return int(input("How many rounds do you want to play? " ))
    except ValueError or TypeError: #Tohle je tu pro případ že hráč napíše něco jinýho než číslo
        print("Please enter a number.")
        return get_rounds() #Tady se to vrátí na start té funkce
rounds = get_rounds() #Jelikož nám ta funkce vrátí číslo zadané od hráče, tak můžeme nastavit kola na tu funkci.

for i in range(0,rounds): #Tohle tu je aby ta hra pokračovala dokud neproběhne ten počet kol který uživatel zadal
    game(choices)

sleep(1)
if Pscore == Cscore: #Tady se určí jestli to je výhra, remíza nebo prohra a podle toho se vybere věta.
    print(f"It's a draw! The final score is {Pscore}:{Cscore}")
elif Pscore > Cscore:
    print(f"You win! The final score is {Pscore}:{Cscore}")
else:
    print(f"The computer wins! The final score is {Pscore}:{Cscore}")
