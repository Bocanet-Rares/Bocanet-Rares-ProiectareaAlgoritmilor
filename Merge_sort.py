def merge_sort(numere):
    if len(numere) <= 1:
        return numere

    mijloc = len(numere) // 2

    prima_parte = merge_sort(numere[:mijloc])
    a_doua_parte = merge_sort(numere[mijloc:])

    rezultat = []
    pozitie1 = 0
    pozitie2 = 0

    while pozitie1 < len(prima_parte) and pozitie2 < len(a_doua_parte):
        if prima_parte[pozitie1] <= a_doua_parte[pozitie2]:
            rezultat.append(prima_parte[pozitie1])
            pozitie1 += 1
        else:
            rezultat.append(a_doua_parte[pozitie2])
            pozitie2 += 1

    while pozitie1 < len(prima_parte):
        rezultat.append(prima_parte[pozitie1])
        pozitie1 += 1

    while pozitie2 < len(a_doua_parte):
        rezultat.append(a_doua_parte[pozitie2])
        pozitie2 += 1

    return rezultat


numere = list(map(int, input("Introdu numerele: ").split()))

print("Lista sortata:", merge_sort(numere))