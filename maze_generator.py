import pygame
from src.params import Params
from src.path import Path
from src.dfs_maze import DFSMaze
from src.file_maze import FileMaze
from src.mst_maze import MSTMaze

if __name__ == '__main__':
    pygame.init()
    glob_h = 700
    glob_w = 700
    sz = glob_w, glob_h
    display = pygame.display.set_mode(sz)
    param = Params(min(glob_h, glob_w))

    if param.type == 0:
        maze = FileMaze(param)
    elif param.type == 1:
        maze = DFSMaze(param)
    elif param.type == 2:
        maze = MSTMaze(param)
    maze.generate(display)
    maze.draw(display)

    if len(param.file_to) != 0:
        maze.save()

    print("Find Path? (Y/N)")
    ans = input()
    if ans == 'Y':
        path = Path(maze)
        if not path.find(0, 0, maze):
            print("NO PATH")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        maze.draw(display)
