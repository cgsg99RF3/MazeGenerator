import pygame

from random import choice

from src.maze import Maze
from src.cell import Cell


class DFSMaze(Maze):
    def generate(self, display):
        cur_cell = self.grid[0][0]
        running_verts = []
        start = True

        while start or len(running_verts) != 0:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
            start = False
            display.fill(pygame.Color('black'))

            for cell_line in self.grid:
                for cell in cell_line:
                    cell.draw(display)

            cur_cell.is_checked = True

            neighbours = cur_cell.get_neighbours(self.grid)
            if len(neighbours) > 0:
                next_cell = choice(neighbours)
                running_verts.append(cur_cell)
                Cell.set_path(cur_cell, next_cell, False)
                cur_cell = next_cell
            elif running_verts:
                cur_cell = running_verts.pop()
            for cell in running_verts:
                pygame.draw.rect(display, (100, 10, 0),
                                 (cell.x * cell.size, cell.y * cell.size,
                                  cell.size - 2, cell.size - 2))

            pygame.display.flip()
