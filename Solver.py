__author__ = 'Oleksandr Korobov'

# This file contains rubica cube solver logic based on A*

from Rubica import Cube


open_list = []
close_list = []

def opposite_direction(direction):
    sign = chr('-')

    if direction[1] == chr('-'):
        sign = chr('+')

    return direction[0] + sign

def is_in_close_list(cube):
    for state in close_list:
        if cube.is_equal_to(state):
            return True
    return False


def get_equal_from_open_list(cube):
    for state in open_list:
        if cube.is_equal_to(state):
            return state
    return None

def delete_state_from_open_list(cube):
    state_to_delete = get_equal_from_open_list(cube)
    open_list.remove(state_to_delete)

def move_to_close_list(cube):
    delete_state_from_open_list(cube)
    close_list.append(cube.copy())

def get_cheapest_from_open_list():
    cheapest = None
    for state in open_list:
        if cheapest is None or state.f < cheapest.f:
            cheapest = state
    return cheapest

def solve_cube(cube, goal = Cube()):
    cursor = cube.copy()

    open_list.append(cursor)

    cursor.g = 0

    path_found = False

    while not path_found:
        current_state = cursor.copy()
        for direction in cursor.directions:
            current_state.rotate(direction)
            if current_state.is_equal_to(goal):
                path_found = True

            current_state.parent_direction = opposite_direction(direction)

            current_state.h = current_state.get_distance(goal)
            current_state.g = cursor.g + 1

            if not is_in_close_list(current_state):
                form_open_list = get_equal_from_open_list(current_state)
                if form_open_list is None:
                    open_list.append(current_state.copy())
                else:
                    if form_open_list.g > current_state.g:
                        form_open_list.g = current_state.g
                        current_state.parent_direction = current_state.parent_direction
                current_state = cursor.copy()

        move_to_close_list(cursor)
        cursor = get_cheapest_from_open_list()

    print ''