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


def main(commands: dict, ordered_colours: list):
    """
    The main function responsible for running and simulating the ant's movements
    """
    ant = Ant(commands, ordered_colours)
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
        board.draw_ant(rows, WIN)

        board.update_ant_dir()
        board.update_ant_pos()

        if board.check_edge():
            rows, cols = (rows * 3), (cols * 3)
            board.increase_board()

        pygame.display.update()


if __name__ == '__main__':
    while True:
        colour = {}
        ordered_colours = []
        num = int(input('Please enter the desired length of the ant cycle (minimum of 2):'))
        for i in range(num):
            key = input("Enter colour in the exact format of R,G,B for the ant to use:")
            tuptup = tuple(int(e) for e in key.split(","))
            value = input("Enter either L or R for what the ant should do at that colour:")
            colour[tuptup] = value
            ordered_colours.append(tuptup)

        if not (len(colour) >= 2):
            print("Invalid dict entered, not long enough.")
            continue
        else:
            # we're happy with the value given
            main(colour, ordered_colours)
            break
