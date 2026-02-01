arr = [1, 2, 3]

print(sum(1 for _ in arr))
print(sum(_ for _ in arr))


def power_of_two():
    x = 1
    while True:
        yield x
        x *= 2


# infinite loop
# print(list(power_of_two()))
