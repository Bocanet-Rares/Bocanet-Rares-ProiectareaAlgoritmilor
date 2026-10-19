numere = list(map(int, input("Introdu numerele: ").split()))

n = len(numere)

for i in range(n):
    for pozitie in range(n - i - 1):
        if numere[pozitie] > numere[pozitie + 1]:
            numere[pozitie], numere[pozitie + 1] = numere[pozitie + 1], numere[pozitie]

print("Lista sortata:", numere)