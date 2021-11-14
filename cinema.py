
n = int(input("Hoeveel personen gaan naar de film?"))
totaal = 0

for i in range(1,n+1):
    leeftijd = int(input("Hoe oud ben je?"))
    DrieD = input("Wil je een 3d film zien? j/n")
    Lang=input("Wil je een langspeelfilm zien? j/n")
    S=input("Ben je student? j/n")
    g = input("Werk je bij cinema of ben je gezinslid van cinemamedewerker? j/n")

    if(leeftijd <= 14):
        prijs = 4
    elif(leeftijd >= 15 and leeftijd <18):
        prijs = 5
    elif(leeftijd >= 18 and leeftijd < 21):
        prijs=6
    else:
        prijs = 7

    if(DrieD == "j"):
        prijs = prijs +2
    if Lang == "j":
        prijs = prijs+2
    if S == "j" and leeftijd <= 25:
        prijs = prijs-2
    if g=="j":
        prijs = prijs*0.9
    print("je betaalt:",prijs)
    totaal = totaal + prijs
print("Totale prijs is: ", totaal)

