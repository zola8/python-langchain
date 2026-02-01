# https://github.com/mCodingLLC/VideosSampleCode/blob/master/videos/111_python_closures/closures.py

x = "global x"


def level_one():
    return x


def level_two(v):
    print(v)
    if v:
        x = "local x"
    return x


def level_three():
    z = "outer z"

    def inner(y):
        return x, y, z

    return inner("y arg")


def level_four():
    z = "first outer z"

    def inner(y):
        return x, y, z

    print(inner.__closure__)

    z = "second outer z"
    print(inner.__closure__)
    return inner("y arg")


def level_five(n):
    z = f"outer z {n}"

    def inner(y):
        return x, y, z

    return inner


def call_n_times(n):
    def inner(f):
        for _ in range(n):
            f()

    return inner


def level_six():
    z = "outer z"

    def donky():
        def inner(y):
            return x, y, z

        z = "donky z"
        return inner

    def chonky():
        x = "chonky x"
        f = donky()
        return f("y arg")

    return chonky()


def what_about_nonlocal_and_global():
    x = "nonlocal x"

    def f():
        nonlocal x
        x = "overwritten nonlocal"
        return x

    def g():
        global x
        x = "overwritten global"
        return x

    print(x)
    print(f())
    print(x)
    print(g())
    print(x)

    # this is needed if you want to assign to a variable from an outer scope within the inner function

    return f, g


def what_about_lambdas_and_comprehensions():
    l = [x * x for x in range(10)]
    l = list(x * x for x in range(10))
    l = list((x * x for x in range(10)))

    g = (x * x for x in range(10))

    def gen():
        for x in range(10):
            yield x * x

    g = gen()


def level_seven():
    def please_dont_do_this():
        if False:
            a = None

        def gen_func():
            nonlocal a
            for v in range(10):
                a = v
                yield v

        return gen_func(), lambda: a

    gen, fun = please_dont_do_this()

    # print(fun()) # error
    next(gen)
    print(fun())  # 0
    next(gen)
    print(fun())  # 1


_empty = object()


class Cell:
    def __init__(self, cell_contents=_empty):
        self._cell_contents = cell_contents

    def __repr__(self):
        contents = self._cell_contents
        if contents is _empty:
            contents_str = "empty"
        else:
            contents_str = f"{contents.__class__.__name__} object at {id(contents):016X}"
        return f"<{self.__class__.__name__} at {id(self):016X}: {contents_str}>"

    @property
    def cell_contents(self):
        if self._cell_contents is _empty:
            raise ValueError("Cell is empty")
        return self._cell_contents

    @cell_contents.setter
    def cell_contents(self, value):
        # except you can't do this from Python
        self._cell_contents = value


def main():
    # print(level_one())
    # print(level_two(False))
    # print(level_three())
    # print(level_four())

    # f = level_five(1)
    # g = level_five(2)
    # print(f("y arg"), g("another y"))

    # print(level_six())

    # level_seven()
    # call_3_times = call_n_times(3)
    # call_3_times(lambda: print("hello"))

    what_about_nonlocal_and_global()


if __name__ == '__main__':
    main()

# closure is an object that wraps up a function with some kind of extra environment
