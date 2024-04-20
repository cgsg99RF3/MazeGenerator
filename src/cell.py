import pygame.draw

class Cell:
    def __init__(self, x: int, y: int, size=50, width=3):
        self.x = x
        self.y = y
        self.is_checked = False
        self.walls = {'top': True, 'bottom': True, 'right': True, 'left': True}
        self.size = size
        self.width = width
        self.in_path = False

    def get_neighbours(self, grid: list) -> list:
        neighbours = []

        if self.x + 1 < len(grid) and not (grid[self.x + 1][self.y].is_checked):
            neighbours.append(grid[self.x + 1][self.y])
        if self.x - 1 >= 0 and not (grid[self.x - 1][self.y].is_checked):
            neighbours.append(grid[self.x - 1][self.y])
        if self.y + 1 < len(grid[self.x]) and not (grid[self.x][self.y + 1].is_checked):
            neighbours.append(grid[self.x][self.y + 1])
        if self.y - 1 >= 0 and not (grid[self.x][self.y - 1].is_checked):
            neighbours.append(grid[self.x][self.y - 1])
        return neighbours


    def get_used_neighbours(self, grid: list) -> list:
        neighbours = []

        if self.x + 1 < len(grid) and grid[self.x + 1][self.y].is_checked:
            neighbours.append(grid[self.x + 1][self.y])
        if self.x - 1 >= 0 and grid[self.x - 1][self.y].is_checked:
            neighbours.append(grid[self.x - 1][self.y])
        if self.y + 1 < len(grid[self.x]) and grid[self.x][self.y + 1].is_checked:
            neighbours.append(grid[self.x][self.y + 1])
        if self.y - 1 >= 0 and grid[self.x][self.y - 1].is_checked:
            neighbours.append(grid[self.x][self.y - 1])
        return neighbours

    @staticmethod
    def is_passage(first, second):
        dx = first.x - second.x
        dy = first.y - second.y

        if (dx == 1):
            return first.walls['right']
        if (dx == -1):
            return first.walls['left']
        if (dy == -1):
            return first.walls['bottom']
        if (dy == 1):
            return first.walls['top']

    @staticmethod
    def is_wall(first, second):
        return not is_passage(first, second)

    @staticmethod
    def set_path(first, second, is_wall):
        dx = first.x - second.x
        dy = first.y - second.y

        if (dx == -1):
            first.walls['right'] = is_wall
            second.walls['left'] = is_wall
        if (dx == 1):
            second.walls['right'] = is_wall
            first.walls['left'] = is_wall
        if (dy == -1):
            first.walls['bottom'] = is_wall
            second.walls['top'] = is_wall
        if (dy == 1):
            first.walls['top'] = is_wall
            second.walls['bottom'] = is_wall

    def draw(self, display):
        coord_x = self.x * self.size
        coord_y = self.y * self.size

        if self.walls['top']:
            pygame.draw.line(display, pygame.Color('cyan'),
                    (coord_x, coord_y), (coord_x + self.size, coord_y), self.width)
        if self.walls['right']:
            pygame.draw.line(display, pygame.Color('cyan'),
                    (coord_x + self.size, coord_y), (coord_x + self.size, coord_y + self.size), self.width)
        if self.walls['bottom']:
            pygame.draw.line(display, pygame.Color('cyan'),
                             (coord_x, coord_y + self.size), (coord_x + self.size, coord_y + self.size), self.width)
        if self.walls['left']:
            pygame.draw.line(display, pygame.Color('cyan'),
                             (coord_x, coord_y + self.size), (coord_x, coord_y), self.width)

        if self.is_checked:
            pygame.draw.rect(display, pygame.Color('black'),
                             (coord_x, coord_y, self.size, self.size))
        if self.in_path:
            pygame.draw.rect(display, pygame.Color('green'),
                             (coord_x + self.size * 0.4, coord_y + self.size * 0.4, self.size * 0.2, self.size * 0.2))
