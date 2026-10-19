numere = list(map(int, input("Introdu numerele: ").split()))

n = len(numere)

for pozitie in range(n):
    pozitie_minim = pozitie

    for pozitie_cautare in range(pozitie + 1, n):
        if numere[pozitie_cautare] < numere[pozitie_minim]:
            pozitie_minim = pozitie_cautare

    numere[pozitie], numere[pozitie_minim] = numere[pozitie_minim], numere[pozitie]

print("Lista sortata:", numere)