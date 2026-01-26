import time
from time import sleep


def timer_dec(base_function):
    def enhanced_function():
        start_time = time.time()
        base_function()
        end_time = time.time()
        print(f"task time: {end_time - start_time}")

    return enhanced_function


def my_func1():
    sleep(1)
    print("my_func1 finished")


@timer_dec
def my_func2():
    sleep(2)
    print("my_func2 finished")


if __name__ == '__main__':
    my_func_call = timer_dec(my_func1)
    my_func_call()

    my_func2()
