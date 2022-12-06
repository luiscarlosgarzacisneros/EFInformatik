def luis():

    grösse = input('Wie gross soll das Viereck sein?')
    grösse = int(grösse)

    for i in range(grösse):
        print('*', end='')
        print(' ', end='')
    print()

    for f in range(grösse - 2):
        print('*', end='')
        for e in range((grösse * 2) - 3):
            print(' ', end='')
        print('*', end='')
        print()

    for i in range(grösse):
        print('*', end='')
        print(' ', end='')
    print()


luis()
