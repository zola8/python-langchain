def tricky_assignment():
    a, b = a[:] = [[]], []
    print(a, b)
    # same =
    tmp = [[]], []
    a, b = tmp
    a[:] = tmp
    print(a, b)
    print(a is a[0])
    #     Modifying a List in Place: a[:] = [1, 2, 3] replaces the contents of the original list a instead of creating a new variable
    a[:] = [1, 2, 3]
    print(a)


def multiple_assignment():
    a = b = c = d = []
    # in python an assignment is not an expression, it's a statement
    # d = [] -- doesnt return anything, only assigns the right hand side to the left
    # other languages: assignments are expression too, it returns back 'd'

    # python - assignment expressions:
    (a := (b := (c := (d := 0))))
    print(a, b, c, d)


def tricky_assignment2():
    a, b = a[b] = a = [1, 2, 3], 2
    print(a, b)


def main():
    tricky_assignment()
    multiple_assignment()
    tricky_assignment2()


if __name__ == '__main__':
    main()
