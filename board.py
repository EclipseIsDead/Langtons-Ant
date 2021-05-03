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
    ant: Ant
    arr: list

    def __init__(self, ant: Ant) -> None:
        self.ant = ant
        self.arr = constants.STARTING_BOARD

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
            ant.update_pos((x, y + 1))
        elif ant.direction == 'S':
            ant.update_pos((x, y - 1))
        elif ant.direction == 'E':
            ant.update_pos((x + 1, y))
        elif ant.direction == 'W':
            ant.update_pos((x - 1, y))
        else:
            raise Exception("Invalid Direction Present")

    def update_ant_dir(self) -> None:
        """
        This updates the ant's current direction with the colour dictionary. This should then update
        the ant's direction.
         """
        ant = self.ant
        x = ant.pos[0]
        y = ant.pos[1]
        directions = ['N', 'E', 'S', 'W']

        arr_midpoint = len(self.arr) // 2 # assumes that self.arr is a square of odd length
        curr_color = self.arr[arr_midpoint + x][arr_midpoint + y]
        index = directions.index(ant.direction)

        if ant.colours[curr_color] == 'R':
            new_dir = directions[(index + 1) % 4]
        elif ant.colours[curr_color] == 'L':
            new_dir = directions[(index - 1) % 4]
        else:
            raise Exception("Invalid Command Present")

        ant.direction = new_dir
        self.arr[arr_midpoint + x][arr_midpoint + y] = ant.get_next_color(curr_color)
        self.update_ant_pos()
