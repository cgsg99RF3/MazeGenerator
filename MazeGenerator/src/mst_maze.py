import pygame
from random import choice
from random import randint
from src.maze import Maze
from src.cell import Cell

class MSTMaze(Maze):
    def generate(self, display):
        running_verts = set()
        x = randint(0, self.params.width - 1)
        y = randint(0, self.params.height - 1)
        running_verts.add(self.grid[x][y])

        while running_verts:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

            display.fill(pygame.Color('black'))

            for cell_line in self.grid:
                for cell in cell_line:
                    cell.draw(display)

            cur_cell = choice(tuple(running_verts))
            running_verts.remove(cur_cell)
            cur_cell.is_checked = True
            neighbours = cur_cell.get_used_neighbours(self.grid)
            frontier = cur_cell.get_neighbours(self.grid)
            for front_cell in frontier:
                running_verts.add(front_cell)

            if len(neighbours) > 0:
                prev_cell = choice(neighbours)
                Cell.set_path(cur_cell, prev_cell, False)

            pygame.display.flip()
