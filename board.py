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
        self.board = []
        self.ant = ant

    def draw_board(self, window) -> None:
        """
        A frunction that draws the intial board
        """
        window.fill(pygame.color.Color(255, 178, 102))

        for row in range(ROWS):
            for col in range(COLS):
                pygame.draw.rect(window, pygame.color.Color(153, 76, 0), (row * SQUARE_SIZE,
                                                                          col * SQUARE_SIZE,
                                                                          SQUARE_SIZE,
                                                                          SQUARE_SIZE), LINE_THICC)
