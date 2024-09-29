n = int(input("What number do you want?"))


def thepowerof(n):
    total = 0
    for i in range(n):
        L = i+1
        total += L**2
        if L!=n:
            print(L**2, end=" + ")
        else:
            print(L**2, end=" = ")
    print(total)
    


thepowerof(n)