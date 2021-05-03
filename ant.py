"""
This file is Copyright (c) 2021 Siddarth Dagar, Daniel Zhu, Ryan Alizadeh, and Bradley Mathi.
"""
import random
from typing import Any

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
        self.gradient = 0xffffff // (len(commands) - 1)
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
        """
        mapping = {}

        for i, command in enumerate(commands):
            colour = self.gradient * i
            mapping[colour] = command

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

    def get_next_color(self, color) -> Any:
        """
        This function finds the color in the cycle after the color parameter and returns that. most
        likely will be done by using self.gradient.
        """
        if color + self.gradient <= 0xffffff:
            return color + self.gradient
        else:
            return 0x000000
