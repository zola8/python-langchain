class Flyer:
    def __init__(self, max_altitude):
        self.max_altitude = max_altitude
        print('Flyer init')

    def fly(self):
        return f"Flying at {self.max_altitude} meters!"


class Swimmer:
    def __init__(self, max_depth):
        self.max_depth = max_depth
        print('Swimmer init')

    def swim(self):
        return f"Swimming at {self.max_depth} meters deep!"


class Duck(Flyer, Swimmer):
    def __init__(self):
        Flyer.__init__(self, 30)
        Swimmer.__init__(self, 15)
        print('Duck init')


if __name__ == '__main__':
    duck = Duck()
    print(duck.fly())
    print(duck.swim())
