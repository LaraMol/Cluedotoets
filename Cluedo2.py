
while True:
    sollicitatie = input("Bent u klaar voor de sollicitatie? ")
    if sollicitatie == "ja":
        break
    else:
        print("Wat doe je hier dan? ")
print ("----------------------------------------------------------------")
naam = input ("Wat is uw naam? ")


geslacht = input ("\nBent u een man of vrouw? ")
leeftijd = int(input("\nHoe oud bent u? "))
diploma = input ("\nHeeft u een acteurs diploma? ")
oud = input ("\nBent u bereid om een ouder personage te spelen? ")
koken = input ("Kunt u koken? ")
snor = input ("\nKunt u een snor laten groeien? ")
haar = input ("\nZit u meer aan de blond, bruin of grijze kant qua haar? ")
verf = input ("\nVind u het erg om uw haar te verven / te scheren? ")
bril = input ("\nHeeft u een bril? ")
persoonlijkheid = input ("\nBent u meer een chique persoon of meer een ouderwetse persoon? ")
feesten = input("\nVind u het leuk om naar feesten te gaan? ")
kringen = input ("\nHeeft u donkere kringen onder uw ogen? ")
leger = input ("\nHeeft u ervaring in het leger? ")
wapens = input ("\nBent u gespecialiseerd in wapens? ")

if leeftijd >= 18:
    if geslacht == "vrouw" and diploma == "ja":
        if koken == "ja" and haar == "grijze" and oud == "ja":
            print ("U kunt op auditie voor Mw. De Wit.")
        elif persoonlijkheid == "ouderwets" and haar == "blond" and feesten == "ja":
            print ("U kunt op auditie voor Mw. Blaauw Van Draet.")
        elif persoonlijkheid == "chique" and haar == "bruin" and kringen == "ja":
            print ("U kunt op auditie voor Rosa Roodhart.")
        else:
            print ("Je mag helaas niet op auditie.")

    if geslacht == "man" and diploma == "ja":
        if leger == "ja" and haar == "grijze" and wapens == "ja":
            print ("U kunt op auditie voor Kolonel van Geelen.")
        elif oud == "ja" and bril == "ja" and snor == "ja":
            print ("U kunt op auditie voor Professor Pimpel.")
        elif oud == "ja" and verf == "ja" and feesten == "nee":
            print ("U kunt op auditie voor Dominee Groenenwoud.")
        else:
            print("Je mag helaas niet op auditie.")

elif leeftijd < 18 and diploma == "nee":
    print ("Je mag helaas niet op auditie.")

