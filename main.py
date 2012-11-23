import pdb

__author__ = 'Oleksandr Korobov'

# This file is just script for development and testing purposes for Rubica.Cube class

import Rubica
import ViewCube
from Solver import solve_cube

# Here you can inject vizualizer or bind it later
# cube = Rubica.Cube(ViewCube.Visualizer())
cube = Rubica.Cube()

old_cube = cube.copy()

cube.bind_visualizer(ViewCube.Visualizer())

cube.rotate('R-')
cube.rotate('U+')
cube.rotate('L+')
cube.rotate('D+')

old_cube.print_cube()
cube.print_cube()
print solve_cube(cube)

