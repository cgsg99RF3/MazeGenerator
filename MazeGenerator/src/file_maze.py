from src.maze import Maze
from src.cell import Cell

class FileMaze(Maze):
    def generate(self, display):
        with open(self.params.file_from) as file_from:
            self.params.width = int(file_from.readline())
            self.params.height = int(file_from.readline())
            mn_sz = max(self.params.height, self.params.width)
            self.grid = [[Cell(x, y,self.params.glob_sz / mn_sz * 0.8) for y in range(self.params.height)] for x in range(self.params.width)]
            for x in range(self.params.width):
                for y in range(self.params.height):
                    for side in ['bottom', 'left', 'right', 'top']:
                        is_wall = file_from.read(1)
                        if is_wall == '1':
                            self.grid[x][y].walls[side] = True
                        else:
                            self.grid[x][y].walls[side] = False

