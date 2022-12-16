

def square(länge, breite):
    print('::', end='')
    for i in range(breite):
        print('=', end='')
    print('::',)
    for i in range(länge):
        print('II', end='')
        for i in range(breite):
            print(' ', end='')
        print('II')
    print('::', end='')
    for i in range(breite):
        print('=', end='')
    print('::')


länge = int(input('länge'))
breite = int(input('breite'))

square(länge, breite)
