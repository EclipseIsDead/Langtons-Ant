"""
This file is Copyright (c) 2021 Siddarth Dagar, Daniel Zhu, Ryan Alizadeh, and Bradley Mathi.
"""
import pygame
from ant import Ant
from constants import *


class Board:
    """
    This is the Board Class.

     Instance Attributes:
        - ant: The ant object that will be moving on the board
        - arr: The list of lists representation of the board
    """
    ant: Ant
    arr: list

    def __init__(self, ant: Ant) -> None:
        self.ant = ant
        self.arr = STARTING_BOARD

    def draw_board(self, rows: int, cols: int, window) -> None:
        """
        A function that draws the initial board
        """
        window.fill(pygame.Color("#3A3A3A"))

        square_size = WIDTH // rows

        for row in range(rows):
            for col in range(cols):
                pygame.draw.rect(window, pygame.Color('#' + self.arr[row][col][2:]),
                                 (row * square_size, col * square_size,
                                  square_size - (2 * LINE_THICC),
                                  square_size - (2 * LINE_THICC)), 0)

    def draw_ant(self, rows: int, window) -> None:
        """
        This function draws the ant on the board, but without obscuring the square it is on.
        """
        square_size = WIDTH // rows
        ant_size = square_size // 2

        # Makes the ant image
        big_ant = pygame.image.load("ant.png")
        ant_img = pygame.transform.scale(big_ant, (ant_size, ant_size))

        # Draws the ant image
        window.blit(ant_img, (self.ant.pos[0] * square_size + square_size // 4,
                              self.ant.pos[1] * square_size + square_size // 4))
        pygame.display.flip()

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

        arr_midpoint = len(self.arr) // 2  # assumes that self.arr is a square of odd length
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

    def increase_board(self) -> None:
        """
        Increases the board by 3 times its size, keeping the original board in the middle of the
        new one
        """
        len_rol_col = len(self.arr)
        new_board = []

        # Creates a new array 3 times the previous board's that is filled with 0's
        for row in range(3 * len_rol_col):
            list_so_far = []

            for col in range(3 * len_rol_col):
                list_so_far.append("0xFFFFFF")

            new_board.append(list_so_far)

        # Place the appropriate values in the center of the array
        for row in range(len_rol_col):
            for col in range(len_rol_col):
                new_board[row + len_rol_col][col + len_rol_col] = self.arr[row][col]

        # Updates new ant position on the board
        ant_row, ant_col = self.ant.pos[0], self.ant.pos[1]
        self.ant.pos = (ant_row + len_rol_col, ant_col + len_rol_col)

        self.arr = new_board

    def check_edge(self) -> bool:
        """
        This function should check whether the ant is on the edge of the current board and return
        said check as a boolean value.
        """
        ant = self.ant
        x = ant.pos[0]
        y = ant.pos[1]

        if x == 0 or x == len(self.arr) or y == 0 or y == len(self.arr):
            return True
        else:
            return False
