class Ant:
    """This is the ant."""
    commands: str
    pos: tuple

    def __init__(self, commands: str, pos: tuple):
        self.commands = commands
        self.pos = pos
