
boodschappenlijst = []

while True:
    artikel = input("Voeg een artikel toe aan de boodschappenlijst: ")
    if artikel in boodschappenlijst:
        print("Dit artikel is al toegevoegd aan de lijst!")
        continue

    boodschappenlijst.append(artikel)
    print(f"{artikel} is toegevoegd aan de lijst.")

    doorgaan = input("Wil je nog een artikel toevoegen? (ja/nee) ")
    if doorgaan.lower() != "ja":
        break

with open("boodschappenlijst.txt", "w") as f:
    for artikel in boodschappenlijst:
        f.write(f"{artikel}\n")

print("Bedankt voor het gebruik van de boodschappenlijst-app!")
