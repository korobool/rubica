__author__ = 'Oleksandr Korobov'

# This file contains rubica cube solver logic based on A*

from Rubica import Cube

def solve_cube(cube, goal = Cube()):

    print 'Not implemented yet. This is just a stub.'
    cube.rotate('U+')
    cache = cube.copy()
    directions = cube.directions
    print directions
    #goal.print_cube()
    print ''