"""
This file is Copyright (c) 2021 Siddarth Dagar, Daniel Zhu, Ryan Alizadeh, and Bradley Mathi.
"""
import pygame
from ant import Ant
from constants import *


class Board:
    """
    This is the Board Class

     Instance Attributes:
        - ant: The ant object that will be moving on the board
    """

    def __init__(self, ant: Ant) -> None:
        self.ant = ant

    def draw_board(self, rows: int, cols: int, window) -> None:
        """
        A function that draws the initial board
        """
        window.fill(pygame.color.Color(255, 178, 102))

        square_size = WIDTH // rows

        for row in range(rows):
            for col in range(cols):
                pygame.draw.rect(window, pygame.color.Color(153, 76, 0), (row * square_size,
                                                                          col * square_size,
                                                                          square_size,
                                                                          square_size), LINE_THICC)

    def draw_pieces(self, rows: int, cols: int, board: list[list], window) -> None:
        """
        A function that draws pieces onto the board
        """
        square_size = WIDTH // rows

        for row in range(rows):
            for col in range(cols):
                if board[row][col] == 'black':
                    pygame.draw.rect(window, pygame.color.Color(153, 76, 0),
                                     (col * square_size + LINE_THICC,
                                      row * square_size + LINE_THICC,
                                      square_size - (2 * LINE_THICC),
                                      square_size - (2 * LINE_THICC)), 0)

    def draw_ant(self) -> None:
        """
        This function draws the ant on the board, but without obscuring the square it is on.
        """
        raise NotImplementedError

    def update_ant_pos(self) -> None:
        """
        This function updates the ant's position using the direction the ant is facing.
        """
        ant = self.ant
        x = ant.pos[0]
        y = ant.pos[1]

        if ant.direction == 'N':
            ant.pos = (x, y + 1)
        elif ant.direction == 'S':
            ant.pos = (x, y - 1)
        elif ant.direction == 'E':
            ant.pos = (x + 1, y)
        elif ant.direction == 'W':
            ant.pos = (x - 1, y)
        else:
            raise Exception("Invalid Direction Present")

    def update_ant_dir(self) -> None:
        """
        This updates the ant's current direction with the colour dictionary. This should then update
        the ant's direction.
         """
        ant = self.ant
        directions = ['N', 'E', 'S', 'W']
        # get board color at self.position
        curr_color = (0, 0, 0)
        index = directions.index(ant.direction)

        if ant.colours[curr_color] == 'R':
            new_dir = directions[(index + 1) % 4]
        else:
            new_dir = directions[(index - 1) % 4]

        # set board color to curr_color + gradient
        ant.direction = new_dir
