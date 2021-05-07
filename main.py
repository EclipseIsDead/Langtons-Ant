"""
The main file

This file is Copyright (c) 2021 Siddarth Dagar, Daniel Zhu, Ryan Alizadeh, and Bradley Mathi.
"""
import pygame
from board import Board
from ant import Ant
from constants import *

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Langton\'s Ant')
FPS = 60


def main(commands: str):
    """
    The main function responsible for running and simulating the ant's movements
    """
    ant = Ant(commands)
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

            if event.type == pygame.MOUSEBUTTONDOWN:
                board.draw_board(rows, cols, WIN)
                board.draw_ant(rows, WIN)
                # something wrong, i can feel it!
                board.update_ant_dir()
                board.update_ant_pos()

                if board.check_edge():
                    rows, cols = (rows * 3), (cols * 3)
                    board.increase_board()

            pygame.display.update()


if __name__ == '__main__':
    while True:
        data = input('Please input a sequence of commands in the format of LRLRRRL, for example,'
                     + '\n' +
                     'greater than 2 commands, or characters, in length:')
        if not (len(data) >= 2):
            print("Invalid command entered, not long enough.")
            continue
        else:
            # we're happy with the value given
            main(data)
            break
