from functools import wraps
from typing import Callable

# ------------------------------------------------------------
# Generic Types
# ------------------------------------------------------------

type PredicateFn[T] = Callable[[T], bool]


# ------------------------------------------------------------
# Predicate
# ------------------------------------------------------------

class Predicate[T]:
    """
    A composable predicate that supports &, |, and ~ operators.
    Wraps a function (T -> bool).
    """

    def __init__(self, fn: PredicateFn[T]):
        self.fn = fn

    def __call__(self, obj: T) -> bool:
        return self.fn(obj)

    def __and__(self, other):
        return Predicate(lambda x: self(x) and other(x))

    def __or__(self, other):
        return Predicate(lambda x: self(x) or other(x))

    def __invert__(self):
        return Predicate(lambda x: not self(x))


# ------------------------------------------------------------
# Decorators
# ------------------------------------------------------------


def predicate[T](fn: PredicateFn[T]) -> Predicate[T]:
    @wraps(fn)
    def wrapper(obj: T) -> bool:
        return fn(obj)

    return Predicate(wrapper)
