
import time

zahlen = []
primzahlen = []
ka = True

timee = time.time()

for i in range(2, 1000):
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

print(time.time() - timee)
