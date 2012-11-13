__author__ = 'Oleksandr Korobov'

# This file contains rubica cube solver logic based on A*

from Rubica import Cube

def solve_cube(state, goal_state = Cube()):
    goal_state.print_cube()
    print ''