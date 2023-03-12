for i in [4, 3, 2, 1, 0, 1, 2, 3, 4] :
    for e in range(0, i):
        print(' ', end = " ")
    for e in range(0,(4-i)*2+1):

        print('^', end = " ")
    print()