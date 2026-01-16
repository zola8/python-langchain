from fastmcp import FastMCP

notes_mcp = FastMCP(name="Notes Service")


class NoteManager:
    def __init__(self):
        self.notes = []

    def get_my_notes(self):
        return "Your notes:\n" + "\n".join(f"note: {n}" for n in self.notes)

    def add_note(self, content: str):
        self.notes.append(content)
        return f"added note: {content}"


nm = NoteManager()


@notes_mcp.tool()
def get_my_notes() -> str:
    """Get all notes for a user"""
    return nm.get_my_notes()


@notes_mcp.tool()
def add_note(content: str) -> str:
    """Add a note for a user"""
    return nm.add_note(content)


if __name__ == "__main__":
    pass
