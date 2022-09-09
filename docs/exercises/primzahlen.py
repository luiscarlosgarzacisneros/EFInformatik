

zahlen = []
primzahlen = []
ka = True
for i in range(2, 100):
    zahlen.append(i)
for q in zahlen:
    for p in primzahlen:
        if q % p == 0:
            ka = False
            break
    if ka == True:
        primzahlen.append(q)
    ka = True
print(primzahlen)
