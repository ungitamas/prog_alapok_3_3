"""
1.	Írjon programot, ami bekéri három egymás utáni nap átlaghőmérsékletét! Az átlaghőmérséklet lehet nem egész szám is. A bekérés után ellenőrizze, hogy voltak-e olyan napok, amelyeken ugyanannyi volt az átlaghőmérséklet! Ha igen, írja ki ezt a képernyőre! Ha nem voltak ilyen napok, döntse el, hogy melyik napon volt a legmelegebb és írja ki a nap számát a képernyőre! (8p)
"""

homersekletek=[]
for i in range(3):
    homersekletek.append(float(input(f"Kérem a(z) {i+1}. nap átlaghőmérsékletét: ")))

if homersekletek[0]==homersekletek[1] or homersekletek[0]==homersekletek[2] or homersekletek[1]==homersekletek[2]:
    print("Voltak olyan napok, amikor ugyanannyi volt az átlaghőmérséklet")
elif homersekletek[0]>homersekletek[1] and homersekletek[0]>homersekletek[2]:
    print("Az 1. nap volt a legmelegebb")
elif homersekletek[1]>homersekletek[0] and homersekletek[1]>homersekletek[2]:
    print("A 2. nap volt a legmelegebb")
else:
    print("A 3. nap volt a legmelegebb")


"""
2.	Írjon programot, amelynek kódjában hozzon létre egy fiuk és egy lanyok nevű listát. A fiuk listában 5 fiú keresztnevet, a lanyok listában 5 lány keresztnevet tároljon el! Ezt követően a felhasználótól addig kérjen be neveket, amíg a felhasználó olyan nevet ad, ami a listák valamelyikében szerepel! Ha olyan név, vagy üres string érkezik, ami nincs a listák egyikében sem, írjuk ki nemek szerint csoportosítva, hogy az egyes neveket a felhasználó hányszor írta be a programba! Csak azok a nevek jelenjenek meg, akiket legalább egyszer megemlítettek! (14p)
"""


"""
fiuk = ["Peti", "Laci", "Sanyi", "Gabi", "Zoli"]
lanyok = ["Julcsi", "Timi", "Rita", "Zita", "Edina"]
statisztika_f={}
statisztika_l={}

nev = input("Kérem egy tanuló nevét: ")
while (nev in fiuk or nev in lanyok):
    if nev in fiuk:
        if nev in statisztika_f:
            statisztika_f[nev]+=1
        else:
            statisztika_f[nev]=1
    else:
        if nev in statisztika_l:
            statisztika_l[nev]+=1
        else:
            statisztika_l[nev]=1
    nev = input("Kérem egy tanuló nevét: ")

print("\nFiúk előfordulása:", sum(statisztika_f.values()))
for key in statisztika_f:
    print(f"{key} {statisztika_f[key]}")
print("\nLányok előfordulása:", sum(statisztika_l.values()))
for key in statisztika_l:
    print(f"{key} {statisztika_l[key]}")
"""



"""
a.	Hány csiga adatai találhatók meg az állományban?
b.	Hány meztelencsiga található az állományban? (Vegye figyelembe, hogy a félmeztelencsiga nem meztelencsiga!)
c.	Kérje be egy csiga latin nevét, majd ha megtalálható az adatok között, írja ki a hozzá tartozó magyar nevet! Oldja meg, hogy a keresés akkor is hozzon eredményt, ha a latin nevet nem nagy kezdőbetűvel kezdjük (a keresés legyen kis/nagybetűre érzéketlen)! Ha nem található ilyen latin név, azt is jelezzük a felhasználónak! A keresés során ügyeljen arra, hogy a keresést ne folytassa, ha a választ biztosan meg tudja adni! 

"""    

"""
csiga={}
csigak=[]
with open("csigak.txt","r",encoding="utf-8") as fin:
    for sor in fin:
        seged_lista=sor.strip().split(";")
        csiga["latin"]=seged_lista[0]
        csiga["magyar"]=seged_lista[1]
        csigak.append(csiga)
        csiga={}

print(f"{len(csigak)} csiga adatai találhatók meg az állományban.")

def megszamolas(csigak,s):
    db=0
    for csiga in csigak:
        if s in csiga["magyar"]:
            db+=1
    return db

print(f"{megszamolas(csigak,'meztelen')} db meztelencsiga található az adatok között.")

be_csiga=input("Kérem egy csiga latin nevét:") or "limax maximus"

def kereses(csigak, s):
    i=0
    while i<len(csigak) and not(csigak[i]["latin"].lower()==s.lower()):
        i+=1
    if i<len(csigak):
        return csigak[i]["magyar"]
    else:
        return "Nincs ilyen latin nevű csiga az adatok között"

print(f"A csiga magyar neve: \n{kereses(csigak, be_csiga)}")
"""


        