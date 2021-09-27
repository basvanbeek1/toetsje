#Kolonel van Geelen:
#1. heb je een Militaire achtergrond 
#2. ben je een specialist in wapens en tactische complotten
#3. ben je een politie deskundige 

#Mevrouw de Wit
#ben je een kok
#heb je een fors postuur  
#ben je wit haar 

#Dominee Groenewoud
#ben je 
#ben je kaal 
#heb je een fors postuur 




print("+++++++++++++++++++++++++++++++++++++++++")
print("+ Welkom bij de cluedo rollen zoektocht +")
print("+++++++++++++++++++++++++++++++++++++++++")
print("+ Wij gaan je hier wat vragen stellen   +")
print("+ om te kijken of je geschikt bent      +")
print("+ voor 1 van onze vele rollen.          +")
print("+++++++++++++++++++++++++++++++++++++++++")

leeftijd = input("hoe oud ben je? \n")
diploma = input("Ben je in bezit van een mbo 3 opleiding \n")
ManOfVrouw= input("Ben je een man of vrouw? \n")

 
def leeftijd_diploma():
    if leeftijd >= 18 and diploma == "ja":
        return True 
    else:
        False

def man():
    VanGeelen = leeftijd_diploma == True and kaal == "nee" and bril == "ja" and snor == "nee"
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
    snor = input("Heb je een snor?\n")
    bril = input("heb je een bril?\n")
    kaal = input("ben je kaal?\n")
    Haar = 0 
elif ManOfVrouw.lower() == "v":
    Haar = input("heb je lang haar?\n")
    bril = input("heb je een bril\n")
    kaal = 0
    snor = 0
    
 



