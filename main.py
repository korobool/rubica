__author__ = 'oleksandr'

# This file is just script for development and testing purposes for Rubica.Cube class

import Rubica
import ViewCube

cube = Rubica.Cube(ViewCube.Visualizer())

goal_cube = Rubica.Cube()

old = cube.copy()
#cube.rotate('L+')
print 'are equal:', cube.is_equal_to(old)
#print 'distance:', cube.get_distance(old)
cube.randomize()
print 'distance:', cube.get_distance(old)
cube.print_cube()
#cube.rotate('L-')
print 'are equal:', cube.is_equal_to(old)
#print 'distance:', cube.get_distance(old)
#
#old.print_cube()
#cube.print_cube()


cube.solve()