from time import sleep
def qst1(): #Všechny tyhle funkce jsou jednotlivé otázky, rovnou i se systémem odpovědí
    sleep(0.5)
    print("How many planets are there in the solar system?")
    sleep(0.5)
    try:
        answer = int(input("Enter your answer: "))
        sleep(0.5)
        if answer == 8:
            print("Correct!")
            sleep(0.5)
        else:
            print("Wrong!")
            sleep(0.5)
    except (TypeError,ValueError):
        print("Let's try that again...")
        qst1()
def qst2():
    sleep(0.5)
    print("Where do penguins live?")
    sleep(0.5)
    answer = input("Enter your answer: ")
    sleep(0.5)
    if answer.lower() == "antarctica":
        print("Correct!")
        sleep(0.5)
    else:
        print("Wrong!")
        sleep(0.5)
def qst3():
    sleep(0.5)
    print("What is the human body's largest organ? (One word) ")
    sleep(0.5)
    answer = input("Enter your answer: ")
    sleep(0.5)
    if answer.lower() == "skin":
        print("Correct!")
        sleep(0.5)
    else:
        print("Wrong!")
        sleep(0.5)
def qst4():
    sleep(0.5)
    print("What is the largest continent?")
    sleep(0.5)
    answer = input("Enter your answer: ")
    sleep(0.5)
    if answer.lower() == "asia":
        print("Correct!")
        sleep(0.5)
    else:
        print("Wrong!")
        sleep(0.5)
def qst5():
    sleep(0.5)
    print("How many colors are in a rainbow?")
    sleep(0.5)
    try:
        answer = int(input("Enter your answer: "))
        sleep(0.5)
        if answer == 7:
            print("Correct!")
            sleep(0.5)
        else:
            print("Wrong!")
            sleep(0.5)
    except (ValueError,TypeError):
        print("Let's try that again...")
        qst5()
def qst6():
    sleep(0.5)
    print("What is the largest bird on earth? ")
    sleep(0.5)
    answer = (input("Enter your answer: "))
    sleep(0.5)
    if answer.lower() == "ostrich":
        print("Correct!")
        sleep(0.5)
    else:
        print("Wrong!")
        sleep(0.5)
def qst7():
    sleep(0.5)
    print("What mammals lay eggs? (Type only one of them)")
    sleep(0.5)
    answer = (input("Enter your answer: "))
    sleep(0.5)
    if answer.lower() in ["platypus","echidna"]:
        print("Correct!")
        sleep(0.5)
    else:
        print("Wrong!")
        sleep(0.5)
def qst8():
    sleep(0.5)
    print("In which country were french fries invented?")
    sleep(0.5)
    answer = (input("Enter your answer: "))
    sleep(0.5)
    if answer.lower() == "belgium":
        print("Correct!")
        sleep(0.5)
    else:
        print("Wrong!")
        sleep(0.5)
def qst9():
    sleep(0.5)
    print("What is the smallest state in the world? (Hint: _______ city, don't include city in your answer)")
    sleep(0.5)
    answer = (input("Enter your answer: "))
    sleep(0.5)
    if answer.lower() == "vatican":
        print("Correct!")
        sleep(0.5)
    else:
        print("Wrong!")
        sleep(0.5)
def qst10():
    sleep(0.5)
    print("What is Shrek's wife's name?")
    sleep(0.5)
    answer = (input("Enter your answer: "))
    sleep(0.5)
    if answer.lower() == "fiona":
        print("Correct!")
        sleep(0.5)
    else:
        print("Wrong!")
        sleep(0.5)
def outofrange():
    print("Type 1-10.")

qsts: dict = {1: qst1, #Tenhle celý slovník je tu, abych se vyhnul velkému bloku if-statementů.
              2: qst2,
              3: qst3,
              4: qst4,
              5: qst5,
              6: qst6,
              7: qst7,
              8: qst8,
              9: qst9,
              10: qst10
}

def game():
    try:
        select = int(input("What question do you want? 1-10 ")) #Tady si hráč vybere kterou otázku chce
        question = qsts.get(select,outofrange)  #Pomocí již vytvořeného slovníku tady převedeme číslo na otázku, kde select je klíč,
                                                #a jestliže vybraly otázku mimo 1-10 tak to půjde na outofrange, což jim prostě řekne ať 
                                                #napíšou číslo mezi 1-10.
        sleep(0.5)
        question() # Teď se nám question rovná hodnotě ze slovníku, a jelikož jsou všechny hodnoty funkce, tak se nám question rovná funkci.
    except (ValueError,TypeError): #Jestli nenapíšou číslo tak jim to řekne ať napíšou číslo a vrátí je to na začátek
        sleep(0.5)
        print("Please enter a number")
        game()

while True: #While True loop může vypadat špatně, ale máme tady break statement, takže máme jak ukončit tento program.
    game()
    Pcontinue = input(f"Please type C if you want to continue, or type anything else to quit the game.") #Kdyby hráč už nechtěl hrát.
    if Pcontinue.lower() != "c":
        sleep(0.5)
        print(f"Goodbye!")
        break
    else:
        continue