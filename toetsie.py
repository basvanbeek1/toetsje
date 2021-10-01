print("+++++++++++++++++++++++++++++++++++++++++")
print("+ Welkom bij de cluedo rollen zoektocht +")
print("+++++++++++++++++++++++++++++++++++++++++")
print("+ Wij gaan je hier wat vragen stellen   +")
print("+ om te kijken of je geschikt bent      +")
print("+ voor 1 van onze vele rollen.          +")
print("+++++++++++++++++++++++++++++++++++++++++")

leeftijd = int(input("hoe oud ben je? \n"))
diploma = input("Ben je in bezit van een mbo 3 opleiding \n")
ManOfVrouw= input("Ben je een man of vrouw? \n")

leeftijd_diploma = leeftijd >= 18 and diploma == "ja"

def man():
    snor = input("Heb je een snor?\n")
    bril = input("heb je een bril?\n")
    kaal = input("ben je kaal?\n")
    VanGeelen = kaal == "nee" and bril == "ja" and snor == "nee" and leeftijd_diploma == True
    groenewoud = leeftijd_diploma == True and kaal == "ja" and bril == "nee" and snor == "nee"
    Pimpel = leeftijd_diploma == True and kaal == "nee" and bril == "ja" and snor == "ja"
    if Pimpel == True:
        return print("Je mag op auditie voor de rol van Professor Pimpel")
    elif groenewoud == True:
        return print("Je mag op auditie voor de rol van Dominee Groenewoud")
    elif VanGeelen == True:
        return print("Je mag op auditie voor de rol van Kolonel van Geelen")

if ManOfVrouw.lower() == "m":
    man()
elif ManOfVrouw.lower() == "v":
    Haar = input("heb je lang haar?\n")
    bril = input("heb je een bril\n")
    kaal = 0
    snor = 0

 



