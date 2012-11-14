import pdb

__author__ = 'Oleksandr Korobov'

# This file is just script for development and testing purposes for Rubica.Cube class

import Rubica
import ViewCube
from Solver import solve_cube

cube = Rubica.Cube(ViewCube.Visualizer())

old_cube = cube.copy()
cube.print_cube()
cube.rotate('U+')
cube.print_cube()

solve_cube(cube)

pdb.set_trace()
