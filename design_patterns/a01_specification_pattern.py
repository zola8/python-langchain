# model
from dataclasses import dataclass
from typing import Callable


# https://github.com/ArjanCodes/examples/blob/main/2026/spec/rules.py
# Specification Pattern


@dataclass
class User:
    id: int
    is_admin: bool
    is_active: bool


class Predicate():
    """
        A composable predicate that supports &, |, and ~ operators.
        Wraps a function (T -> bool).
    """

    def __init__(self, fn: Callable[[User], bool]):
        # gets a function which is a callable,
        # and this function gets a user, and returns a bool value
        self.fn = fn

    def __call__(self, user: User) -> bool:
        return self.fn(user)

    def __and__(self, other):
        return Predicate(lambda x: self(x) and other(x))

    def __or__(self, other):
        return Predicate(lambda x: self(x) or other(x))

    def __invert__(self):
        return Predicate(lambda x: not self(x))


# rules

# def is_admin(u: User) -> bool:
#     return u.is_admin
#
#
# def is_active(u: User) -> bool:
#     return u.is_active

is_admin = Predicate(lambda u: u.is_admin)
is_active = Predicate(lambda u: u.is_active)
rule = is_admin | is_active


def main():
    user = User(1, False, False)
    print(rule(user))


if __name__ == '__main__':
    main()
