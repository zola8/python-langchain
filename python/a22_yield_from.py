def numbers():
    yield 1
    yield 2
    yield 3


def combined():
    yield from numbers()  # Delegates to the numbers() generator
    yield 4
    yield 5


# Usage
for value in combined():
    print(value)

# numbers() is a simple generator that yields 1, 2, 3
# combined() uses yield from numbers() to delegate yielding to the numbers() generator
# After numbers() is exhausted, combined() continues yielding 4 and 5


def echo():
    """Generator that echoes back values sent to it"""
    value = yield "Ready"  # First yield returns "Ready", then receives first send()
    while True:
        value = yield f"Echo: {value}"

def wrapper():
    """Delegates to echo() using yield from"""
    print("Wrapper starting...")
    result = yield from echo()  # Forwards sends to echo(), captures its final return value
    print(f"Wrapper received from echo(): {result}")
    yield f"Final: {result}"

# Usage
gen = wrapper()

# Must start with next() or send(None)
print(next(gen))        # Output: Wrapper starting... \n Ready

# Send values - they go directly to the inner echo() generator
print(gen.send("Hello"))   # Output: Echo: Hello
print(gen.send("World"))   # Output: Echo: World
print(gen.send(None))
print(gen.send(None))

# Close the generator (triggers StopIteration in echo, which returns a value)
try:
    gen.close()
except StopIteration as e:
    print(f"Generator finished with return value: {e.value}")
