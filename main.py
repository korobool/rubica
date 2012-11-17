import pdb

__author__ = 'Oleksandr Korobov'

# This file is just script for development and testing purposes for Rubica.Cube class

import Rubica
import ViewCube
from Solver import solve_cube

cube = Rubica.Cube()#ViewCube.Visualizer())

old_cube = cube.copy()

cube.randomize()

cube.print_cube()

cube.bind_visualizer(ViewCube.Visualizer())

cube.print_cube()

#print cube.is_equal_to(old_cube)

#cube.randomize()

#solve_cube(cube)

# pdb.set_trace()
