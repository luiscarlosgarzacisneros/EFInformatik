

zahlen = []
primzahlen = []
ka = True

for i in range(2, 100):
    zahlen.append(i)


for zahl in zahlen:
    for primzahl in primzahlen:
        if zahl % primzahl == 0:
            ka = False

    if ka == True:
        primzahlen.append(zahl)
    ka = True

print(primzahlen)
