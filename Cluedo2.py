while True:
    sollicitatie = input("Bent u klaar voor de sollicitatie? ")
    if sollicitatie == "ja":
        break
    else:
        print("Wat doe je hier dan? ")

print ("Sollicitatie wordt ingeladen.") 
print ("----------------------------------------------------------------")

naam = input ("Beste sollicitant hoe heet u? ")
leeftijd = input ("Wat is uw leeftijd? ")

Geslacht = input ("Bent u een man of een vrouw? ")
if Geslacht == "vrouw":
    diploma = input ("Heeft u een acteurs diploma? ")
    if diploma == "ja":
        print ("Antwoord opgeslagen")
        oud = input ("Staat u bereid om een ouder character te acteren?")
        if oud == "ja":
            print ("Antwoord opgeslagen")
        elif oud == "nee":
            print ("Antwoord opgeslagen")
            
elif Geslacht == "man":
    diploma = input ("Heeft u een acteurs diploma? ")
    if diploma == "nee":
        print("Antwoord opgeslagen")
    

