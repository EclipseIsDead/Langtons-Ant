"""
This file is Copyright (c) 2021 Siddarth Dagar, Daniel Zhu, Ryan Alizadeh, and Bradley Mathi.
"""
import random


class Ant:
    """
    This is the ant.
    """
    commands: str
    pos: tuple
    colours: dict
    direction: str

    def __init__(self, commands: str = 'RL', pos: tuple = (0, 0)):
        self.commands = commands
        self.pos = pos
        self.direction = random.choice(['N', 'S', 'E', 'W'])
        self.colours = self._get_colour_construction(commands)

    def __repr__(self):
        return "Ant()"

    def __str__(self):
        return self.commands + "\n" + \
               str(self.pos) + ', ' + \
               self.direction + "\n" + \
               str(self.colours)

    def _get_colour_construction(self, commands: str) -> dict:
        """
        This should return a dictionary that maps the colours to their respective command.
        :param commands:
        :return:
        """
        gradient = 0xffffff // (len(commands) - 1)
        mapping = {}

        for i, command in enumerate(commands):
            colour = gradient * i
            mapping[colour] = command

        return mapping

    def update_pos(self) -> None:
        """
        This updates the ant's current position with the current direction it is facing.
        """
        x = self.pos[0]
        y = self.pos[1]

        if self.direction == 'N':
            self.pos = (x, y + 1)
        elif self.direction == 'S':
            self.pos = (x, y - 1)
        elif self.direction == 'E':
            self.pos = (x + 1, y)
        elif self.direction == 'W':
            self.pos = (x - 1, y)
        else:
            raise Exception("Invalid Direction Present")

    def update_direction(self) -> None:
        """
        This updates the ant's current direction with the colour dictionary. This should then update
        the ant's direction.
        """
        return None

langton = Ant()
print(langton)