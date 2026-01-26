from dataclasses import dataclass

from design_patterns.a02_specification_rules import predicate


@dataclass
class User:
    id: int
    is_admin: bool
    is_active: bool


@predicate
def is_admin(u: User) -> bool:
    return u.is_admin


@predicate
def is_active(u: User) -> bool:
    return u.is_active


def main():
    user = User(1, True, True)
    rule = is_admin & is_active

    print(rule(user))


if __name__ == '__main__':
    main()

# https://www.youtube.com/watch?v=KqfMiuL3cx4
# https://github.com/ArjanCodes/examples/blob/main/2026/spec/rule_config.json
