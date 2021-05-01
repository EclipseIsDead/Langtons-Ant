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
FPS = 60


def main():
    """
    The main function responsible for running and simulating the ant's movements
    """
    ant = Ant('up', (1, 1,))
    board = Board(ant)
    run = True
    clock = pygame.time.Clock()
    rows, cols = ROWS, COLS

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            board.draw_board(rows, cols, WIN)
            # board.draw_pieces(rows, cols, STARTING_BOARD, WIN)
            pygame.display.update()

            rows, cols = rows * 3, cols * 3

            pygame.time.wait(1000)


if __name__ == '__main__':
    main()
