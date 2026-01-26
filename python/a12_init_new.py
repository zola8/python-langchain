class UppercaseTuple(tuple):
    def __new__(cls, iterable):
        upper_iterable = (s.upper() for s in iterable)
        return super().__new__(cls, upper_iterable)

    # Error: tuples are immutable, even in init
    # def __init__(self, iterable):
    #     print(f'init {iterable}')
    #     for i, arg in enumerate(iterable):
    #         self[i] = arg.upper()


class Singleton:  # eg global config object, I discourage actually using this pattern
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance


def singleton_example():
    print("-- SINGLETON EXAMPLE --")
    x = Singleton()
    y = Singleton()
    print(f'{x is y=}')


class Client:
    _loaded = {}
    _db_file = "file.db"

    def __new__(cls, client_id):
        if (client := cls._loaded.get(client_id)) is not None:
            print(f'returning existing client {client_id} from cache')
            return client
        client = super().__new__(cls)
        cls._loaded[client_id] = client
        client._init_from_file(client_id, cls._db_file)
        return client

    def _init_from_file(self, client_id, file):
        # lookup client in file and read properties
        print(f'reading client {client_id} data from file, db, etc.')
        name = ...
        email = ...
        self.name = name
        self.email = email
        self.id = client_id


def cached_clients_example():
    print("-- CLIENT CACHE EXAMPLE --")
    x = Client(0)
    y = Client(0)
    print(f'{x is y=}')
    z = Client(1)


if __name__ == '__main__':
    print(UppercaseTuple(["hi", "there"]))
    singleton_example()
    cached_clients_example()
