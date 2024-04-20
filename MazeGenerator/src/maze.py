import pygame
from abc import ABC, abstractmethod
from src.params import Params
from src.cell import Cell

class Maze():
    def __init__(self, params: Params):
        self.params = params
        mn_sz = max(params.height, params.width)
        self.grid = [[Cell(x, y, self.params.glob_sz / mn_sz * 0.8) for y in range(params.height)] for x in range(params.width)]
        if len(self.grid) != 0:
            self.grid[params.width - 1][params.height - 1].walls['right'] = False
    def draw(self, display):
        display.fill(pygame.Color('black'))
        for cell_line in self.grid:
            for cell in cell_line:
                cell.draw(display)
        pygame.display.flip()

    def save(self):
        with open(self.params.file_to, "w+") as file_to:
            file_to.write(str(self.params.width))
            file_to.write("\n")
            file_to.write(str(self.params.height))
            file_to.write("\n")
            for cell_line in self.grid:
                for cell in cell_line:
                    for side in ['bottom', 'left', 'right', 'top']:
                        if cell.walls[side]:
                            file_to.write("1")
                        else:
                            file_to.write("0")

    @abstractmethod
    def generate(self, display):
        pass