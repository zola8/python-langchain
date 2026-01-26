import time
from multiprocessing import Pool

RANGE_NUMBER = 256
N_NUMBER = 10_000


def func1(x, N):
    for i in range(N):
        x += 2 * (i % 2) - 1
    return x


def single_core_work():
    start = time.perf_counter()
    for x in range(RANGE_NUMBER):
        func1(0, N_NUMBER)
    end = time.perf_counter()
    print("single_core_work:", end - start)


def multiprocess_work():
    start = time.perf_counter()
    p = Pool(processes=4)
    p.starmap(func1, [(1, N_NUMBER) for j in range(RANGE_NUMBER)])
    end = time.perf_counter()
    print("multiprocess_work:", end - start)

# https://www.youtube.com/watch?v=DThU1DN_bMs

if __name__ == '__main__':
    single_core_work()
    multiprocess_work()


# RANGE_NUMBER = 256
# N_NUMBER = 1_000_000
# single_core_work: 10.49481940001715
# multiprocess_work: 4.298851700004889

# RANGE_NUMBER = 256
# N_NUMBER = 100_000
# single_core_work: 1.1307135999959428
# multiprocess_work: 0.6341337000194471

# RANGE_NUMBER = 256
# N_NUMBER = 10_000
# single_core_work: 0.10049030001391657
# multiprocess_work: 0.21099699998740107
