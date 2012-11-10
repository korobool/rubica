__author__ = 'oleksandr'

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