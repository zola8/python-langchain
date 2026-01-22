# matching patterns
# https://www.youtube.com/watch?v=-79HGfWmH_w
from dataclasses import dataclass


def command_split(command):
    match command.split():
        case ["make"]:
            print("default make")
        case ["make", cmd]:
            print(f"make command: {cmd}")
        case _:
            print("no match (wildcard)")


def match_alternatives(command):
    match command.split():
        case ["north"] | ["go", "north"]:
            print("going north")
        case ["get", obj] | ["pick", "up", obj] | ["pick", obj, "up"]:
            print(f"picking up {obj}")


def match_capture_subpattern(command):
    match command.split():
        case ["go", ("north" | "east" | "west" | "south") as direction]:
            print(f"going {direction}")


def match_guard(command, available_list):
    match command.split():
        case ["go", direction] if direction in available_list:
            print(f"going {direction}")
        case ["go", _]:
            print("can't go that way")


@dataclass
class Click:
    position: tuple[int, int]
    button: str


@dataclass
class KeyPress:
    key_name: str


@dataclass
class Quit:
    pass


def match_by_class(event):
    match event:
        case Click(position=(x, y), button="left"):
            print(f"handling left click at {x, y}")
        case Click(position=(x, y)):
            print(f"handling other click at {x, y}")
        case KeyPress("Q" | "q") | Quit():
            print("quitting")
        case KeyPress(key_name="up"):
            print("going up")
        case KeyPress():
            pass  # ignore other keys
        case other_event:
            raise ValueError(f"unrecognized event: {other_event}")


def match_json_event(event):
    match event:
        case {"transport": "http"}:
            print("insecure event")
        case {"method": "POST", "page": page}:
            print(f"handling page: {page}")


def main():
    command_split("make")
    command_split("make tea")
    command_split("aaa")

    match_alternatives("go")
    match_alternatives("go north")
    match_alternatives("pick up pen")

    match_capture_subpattern("go west")

    match_guard("go east", available_list=["east", "west"])
    match_guard("go north", available_list=["east", "west"])

    try:
        match_by_class("badvalue")
    except ValueError:
        pass

    match_by_class(Quit())
    match_by_class(Click(position=(1, 2), button="left"))
    match_by_class(KeyPress(key_name="a"))

    match_json_event({"transport": "http"})
    match_json_event({"transport": "http", "a": "b"})
    match_json_event({"method": "POST", "page": "login"})


if __name__ == "__main__":
    main()
