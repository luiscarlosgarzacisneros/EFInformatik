

zahlen = []
primzahlen = []
ka = True


for i in range(2, 100):
    zahlen.append(i)

for q in zahlen:
    for w in primzahlen:
        if q % w == 0:
            ka = True
            break

    if ka == True:
        primzahlen.append(q)
    ka == True

print(primzahlen)
