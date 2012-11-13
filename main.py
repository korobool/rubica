import pdb

__author__ = 'Oleksandr Korobov'

# This file is just script for development and testing purposes for Rubica.Cube class

import Rubica
import ViewCube
from Solver import solve_cube

cube = Rubica.Cube(ViewCube.Visualizer())

old_cube = cube.copy()

cube.rotate('U+')

solve_cube(cube)

pdb.set_trace()
