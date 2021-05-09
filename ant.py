"""
This file is Copyright (c) 2021 Siddarth Dagar, Daniel Zhu, Ryan Alizadeh, and Bradley Mathi.
"""
import random


class Ant:
    """
    This is the ant.
    """
    pos: tuple
    direction: str
    colours: dict
    order: list

    def __init__(self, colours: dict, ordered_colours: list, pos: tuple = (1, 1)):
        self.pos = pos
        self.direction = random.choice(['N', 'S', 'E', 'W'])
        self.colours = colours
        self.order = ordered_colours

    def __repr__(self):
        return "Ant()"

    def __str__(self):
        return str(self.pos) + ', ' + \
               self.direction + "\n" + \
               str(self.colours)

    # def _get_colour_construction(self, commands: str) -> dict:
    #     """
    #     This should return a dictionary that maps the colours to their respective command.
    #     """
    #     mapping = {}
    #
    #     for i, command in enumerate(commands):
    #         colour = (self.gradient * i, self.gradient * i, self.gradient * i)
    #         mapping[colour] = command
    #
    #     return mapping

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

    def get_next_color(self, color) -> tuple:
        """
        This function finds the color in the cycle after the color parameter and returns that.
        Most likely will be done by using self.gradient.
        """
        index = self.order.index(color)
        return self.order[(index + 1) % len(self.order)]
