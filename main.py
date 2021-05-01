"""
The main file

This file is Copyright (c) 2021 Siddarth Dagar, Daniel Zhu, Ryan Alizadeh, and Bradley Mathi.
"""
import pygame
from board import Board
from ant import Ant
from constants import *

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Deez nuts lmfao gottem')


def main():
    """
    The main function responsible for running and simulating the ant's movements
    """
    ant = Ant('up', (1, 1,))
    board = Board(ant)
    board.draw_board(WIN)
    pygame.display.update()


if __name__ == '__main__':
    main()
