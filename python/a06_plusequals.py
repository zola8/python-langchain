pro_and_cons = (['aa', 'bb'], ['cc'])

if __name__ == '__main__':
    x = 1
    print(id(x))

    x += 1
    print(id(x), "changed")

    print(pro_and_cons)

    try:
        pro_and_cons[1] += ['dd']
        # TypeError: 'tuple' object does not support item assignment
    except TypeError:
        print("error happened but item added:", pro_and_cons)

    # this is the same:
    # x[0] += y
    # result = x[0].__iadd__(y) = calls __getitem__
    # x[0] = result = calls __setitem__

    x = []
    print(id(x))
    x += [1]
    print(id(x), "same")
    # doesn't copy the whole list to other object, so ID remains the same
    