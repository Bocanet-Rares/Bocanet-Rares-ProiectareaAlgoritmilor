numere = list(map(int, input("Introdu numerele: ").split()))

for pozitie in range(1, len(numere)):
    numar = numere[pozitie]
    pozitie_anterioara = pozitie - 1

    while pozitie_anterioara >= 0 and numere[pozitie_anterioara] > numar:
        numere[pozitie_anterioara + 1] = numere[pozitie_anterioara]
        pozitie_anterioara -= 1

    numere[pozitie_anterioara + 1] = numar

print("Lista sortata:", numere)