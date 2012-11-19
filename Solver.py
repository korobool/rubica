import pdb

__author__ = 'Oleksandr Korobov'

# This file contains rubica cube solver logic based on A*
# Please, be aware that heuristic here is primitiv and
# Algorithm works almost as slow as brute-force Breadth-first search
# This is just an example of possible approch.

from Rubica import Cube


open_list = []
close_list = []

def opposite_direction(direction):
    sign = '-'

    if direction[1] == '-':
        sign = '+'

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


def get_equal_from_close_list(cube):
    for state in close_list:
        if cube.is_equal_to(state):
            return state
    return None


def solve_cube(cube, goal = Cube()):
    cursor = cube.copy()

    open_list.append(cursor)

    cursor.g = 0

    path_found = False

    finish = None

    while not path_found:
        #print len(open_list), len(close_list)
        current_state = cursor.copy()


        for direction in cursor.directions:
            current_state.rotate(direction)

            current_state.parent_direction = opposite_direction(direction)

            if current_state.is_equal_to(goal):
                path_found = True
                finish = current_state.copy()

            #current_state.h = current_state.get_distance(goal)
            current_state.h = 0.5 * current_state.get_color_distance(goal)
            #current_state.h = current_state.get_distance(goal) + current_state.get_color_distance(goal)
            current_state.g = cursor.g + 1
            current_state.f = current_state.g + current_state.h

            #current_state.print_cube()

            if not is_in_close_list(current_state):
                form_open_list = get_equal_from_open_list(current_state)
                if form_open_list is None:
                    open_list.append(current_state.copy())
                    # print current_state.parent_direction
                else:
                    if form_open_list.g > current_state.g:
                        form_open_list.g = current_state.g
                        current_state.parent_direction = current_state.parent_direction
#                    d = current_state.parent_direction
                current_state = cursor.copy()


#            if cursor.g == 3:
#                return
        move_to_close_list(cursor)
        cursor = get_cheapest_from_open_list()
        print cursor.f, cursor.g, cursor.h

    path = []

    while not finish.is_equal_to(cube): #cursor.parent_direction is None:
        path.append(finish.parent_direction)
#        cursor = get_equal_from_open_list(cursor.rotate(cursor.parent_direction))
#        if cursor is None:
        finish.rotate(finish.parent_direction)
        #cursor.print_cube()
        finish = get_equal_from_close_list(finish)

    print path

