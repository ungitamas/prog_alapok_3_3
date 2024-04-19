# 3.	A mellékelt csigak.txt állomány különböző, Magyarországon is előforduló csigák latin és magyar neveit tartalmazza. Minden sorban egy csiga latin és magyar neve található, pontosvesszővel elválasztva. A fájlnak nincs fejlécsora. Olvassa be az állományt egy erre alkalmas adatszerkezetbe, majd válaszolja meg az alábbi kérdéseket:
# a.	Hány csiga adatai találhatók meg az állományban?
# b.	Hány meztelencsiga található az állományban? (Vegye figyelembe, hogy a félmeztelencsiga nem meztelencsiga!)
# c.	Kérje be egy csiga latin nevét, majd ha megtalálható az adatok között, írja ki a hozzá tartozó magyar nevet! Oldja meg, hogy a keresés akkor is hozzon eredményt, ha a latin nevet nem nagy kezdőbetűvel kezdjük (a keresés legyen kis/nagybetűre érzéketlen)! Ha nem található ilyen latin név, azt is jelezzük a felhasználónak! A keresés során ügyeljen arra, hogy a keresést ne folytassa, ha a választ biztosan meg tudja adni!

csigak = []
csiga = {}

with open("csigak.txt", "r", encoding="utf-8") as bemenet:
    for sor in bemenet:
        adatok = sor.strip().split(";")
        csiga["latin"] = adatok[0]
        csiga["magyar"] = adatok[1]
        csigak.append(csiga)
        csiga = {}

print(f"{len(csigak)} csiga adatai vannak a fájlban.")


db = 0
for i in range(len(csigak)):
    if 'meztelen' in csigak[i]['magyar'] and 'fél' not in csigak[i]['magyar']:
        db +=1
    
print(f"{db} db meztelencsiga található az adatok között")
