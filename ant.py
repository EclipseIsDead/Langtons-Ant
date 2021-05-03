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
    gradient: int

    def __init__(self, commands: str = 'RL', pos: tuple = (0, 0)):
        self.commands = commands
        self.gradient = 255 // (len(commands) - 1)
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
        mapping = {}

        for command in range(0, len(commands)):
            colour = self.gradient * command
            mapping[(colour, colour, colour)] = commands[command]

        return mapping

    def update_pos(self, new_pos) -> None:
        """
        This updates the ant's current position with the new one.
        """
        self.pos = new_pos

    def update_direction(self, new_dir) -> None:
        """
        This updates the ant's current direction with the new one.
        """
        self.direction = new_dir
