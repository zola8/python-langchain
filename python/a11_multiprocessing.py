from multiprocessing import Pool


def f(x):
    return x * x

# https://docs.python.org/3/library/multiprocessing.html

if __name__ == '__main__':
    with Pool(5) as p:
        print(p.map(f, [1, 2, 3]))
