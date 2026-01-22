import inspect
from dataclasses import dataclass, astuple, asdict, field
from pprint import pprint


@dataclass(frozen=True, order=True)
class Comment:
    id: int
    text: str
    replies: list[int] = field(default_factory=list, compare=False, hash=False, repr=True)


if __name__ == '__main__':
    c = Comment(1, 'hello world')
    print(c)
    print(astuple(c))
    print(asdict(c))

    # c.text = 'alma'
    # 'Comment' object attribute 'text' is read-only

    pprint(inspect.getmembers(Comment, inspect.isfunction))

    c1 = Comment(1, 'BB', [10, 15])
    c2 = Comment(2, 'AA', [6, 12])
    print(c1 < c2, c2 < c1, c1 == c2)

    c.replies.append(1)
    print(c)
