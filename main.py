__author__ = 'oleksandr'

# This file is just script for development and testing purposes for Rubica.Cube class

import Rubica
import ViewCube

cube = Rubica.Cube(ViewCube.Visualizer())

cube.print_cube()

old_cube = cube.copy()

cube.rotate('L+')

cube.print_cube()

print 'Diff distance:', cube.get_distance(old_cube)
print 'equality:', cube.is_equal_to(old_cube)

#cube.is_equal_to()

#goal_cube = Rubica.Cube()

#old = cube.copy()
#cube.rotate('L+')
#print 'are equal:', cube.is_equal_to(old)
#print 'distance:', cube.get_distance(old)
#cube.randomize()
#print 'distance:', cube.get_distance(old)
#cube.print_cube()
#cube.rotate('L-')
#print 'are equal:', cube.is_equal_to(old)
#print 'distance:', cube.get_distance(old)
#
#old.print_cube()
#cube.print_cube()


#cube.solve()