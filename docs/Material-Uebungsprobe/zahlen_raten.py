from random import randint


def to_int(r):
    try:
        return int(r)
    except:
        return -1


def is_valid(l):
    if l < 0 or l > 100:
        return -1
    else:
        return l


def abfrage(runde):
    geraten = input(f'{runde}. Versuch: Gib eine ganze Zahl zwischen 0 und 100 ein: ')
    zahl = to_int(geraten)
    z = is_valid(zahl)
    return z


def play():
    runde = 1
    gesucht = randint(0, 100)
    geraten = -1
    while geraten != gesucht:
        geraten = abfrage(runde)
        runde = runde + 1
        if geraten != -1:
            if geraten > gesucht:
                print('Die eingegebene Zahl ist zu gross')
            elif geraten < gesucht:
                print('Die eingegebene Zahl ist zu klein')
    print(f'Bravo, du hast in {runde} Runden die gesuchte Zahl {gesucht} gefunden.')


play()
