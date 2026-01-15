def count_up_to(max_num):
    """Generator that yields numbers from 1 to max_num"""
    current = 1
    while current <= max_num:
        yield current
        current += 1


def fibonacci():
    """Infinite Fibonacci sequence generator"""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b



def flatten_with_path(obj, path=""):
    """
    Recursively yield (path, value) pairs from a nested structure.
    Supports dict, list, tuple. Treats strings and other primitives as leaves.
    """
    if isinstance(obj, dict):
        for key, value in obj.items():
            new_path = f"{path}.{key}" if path else str(key)
            yield from flatten_with_path(value, new_path)
    elif isinstance(obj, (list, tuple)):
        for i, value in enumerate(obj):
            new_path = f"{path}[{i}]"
            yield from flatten_with_path(value, new_path)
    else:
        # Primitive value (str, int, bool, None, etc.)
        yield (path, obj)


# Realistic nested data (e.g., from an API response)
data = {
    "user": {
        "id": 123,
        "name": "Alice",
        "emails": ["alice@example.com", "a.person@work.com"],
        "metadata": {
            "settings": {
                "theme": "dark",
                "notifications": [True, False]
            }
        }
    },
    "status": "active"
}



if __name__ == '__main__':

    # Using the generator
    # for number in count_up_to(5):
    #     print(number)

    # Get first 10 Fibonacci numbers
    # fib = fibonacci()
    # for _ in range(10):
    #     print(next(fib))


    for path, value in flatten_with_path(data):
        print(f"{path} = {value!r}")
