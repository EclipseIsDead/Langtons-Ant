"""
This file is Copyright (c) 2021 Siddarth Dagar, Daniel Zhu, Ryan Alizadeh, and Bradley Mathi.
"""
import pygame
from ant import Ant
from constants import *


class Board:
    """This is the Board Class

     Instnace Attributes:
        - ant: The type of ant that will be moving on the board
    """

    def __init__(self, ant: Ant) -> None:
        self.ant = ant

    def draw_board(self, rows: int, cols: int, window) -> None:
        """
        A frunction that draws the intial board
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

