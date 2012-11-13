__author__ = 'Oleksandr Korobov'

# This file contains rubica cube solver logic based on A*

from Rubica import Cube

def solve_cube(state, goal_state = Cube()):

    print 'Not implemented yet. This is just a stub.'

    state.rotate('L+')
    state.rotate('U+')
    state.rotate('B+')
    state.rotate('L+')
    state.rotate('U+')
    state.rotate('L+')
    state.rotate('U+')
    state.rotate('B+')
    state.rotate('L+')
    state.rotate('U+')
    state.rotate('L+')
    state.rotate('U+')
    state.rotate('B+')
    state.rotate('L+')
    state.rotate('U+')
    state.rotate('L+')
    state.rotate('U+')
    state.rotate('B+')
    state.rotate('L+')
    state.rotate('U+')
    state.rotate('L+')
    state.rotate('U+')
    state.rotate('B+')
    state.rotate('L+')
    state.rotate('U+')
    state.rotate('L+')
    state.rotate('U+')
    state.rotate('B+')
    state.rotate('L+')
    state.rotate('U+')

    goal_state.print_cube()
    print ''