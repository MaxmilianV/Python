from random import choice
from time import sleep
import string
letters = list(string.ascii_letters) #Tady pomocí knihovny string udělám list se všemi písmeny
digits = list(string.digits) #Tady list se všemi čísly
Schars = ["đ","Đ","[","]","ł","Ł","#","&","@","{","}","!","?","_",":","<",">","/","(",")","",".",",","§","¨","$","%","^","*","+","-"]
#Tady list se všemi speciálnímí znaky které jsem potřeboval
chars = list(letters + digits + Schars) #Tady se to všechno spojí do jednoho velkého listu
def pick(characters:list,length:int):
    password = [] #Tady si uděláme seznam kam budeme ukládat všechny znaky
    for i in range(0,length): #Tenhle for loop proběhne tolikrát, kolik uživatel zadal
        password.append(choice(chars)) #Počítač vždy náhodně vybere znak z našeho velkého seznaum a dá to password seznamu
    return "".join(password) #Tady ta funkce vrátí password už ve formě stringu

def getlength(): #Tahle funkce je tu na zjištění délky hesla
    try:
        return int(input("How long do you need the password to be? ")) #Tady to vrátí to, co uživatel zadá
    except ValueError or TypeError: #Kdyby uživatel zadal něco jinýho než číslo tak to jde sem
        print("Please enter a number.")
        return getlength() #Tady se to znovu vrátí na začátek funkce

charlength = getlength() #Tuhle proměnnou nastavíme na tu funkci, protože vrací číslo které uživatel zadá.
print(pick(chars,charlength)) #Tady zavoláme tu funkci, která nám vytvoří to heslo.
