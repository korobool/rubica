__author__ = 'oleksandr'

import copy
import random
import weakref


class Cube():
    __global_visualizer = None
    def __init__(self, observer = None):
        self.fringe = {}
        self.__init__fringes()
        Cube.__global_visualizer = observer
        self.directions = ('L+', 'L-', 'R+', 'R-', 'U+', 'U-', 'D+', 'D-', 'B+', 'B-', 'F+', 'F-')

        if not Cube.__global_visualizer is None:
            Cube.__global_visualizer.notify('created', sender = self)

        self.previous_state = self.copy()

    def rotate(self, direction, is_recursive_call = False):
        previous_state = self.copy()

        if not direction in self.directions:
            print 'Cannot apply unsupported rotation:', direction
            return False

        if direction == 'L+':
            cache = [self.fringe['front'][0][0], self.fringe['front'][1][0], self.fringe['front'][2][0]]
            self.fringe['front'][0][0] = self.fringe['bottom'][0][0]
            self.fringe['front'][1][0] = self.fringe['bottom'][1][0]
            self.fringe['front'][2][0] = self.fringe['bottom'][1][0]

            self.fringe['bottom'][0][0] = self.fringe['back'][0][0]
            self.fringe['bottom'][1][0] = self.fringe['back'][1][0]
            self.fringe['bottom'][2][0] = self.fringe['back'][1][0]

            self.fringe['back'][0][0] = self.fringe['top'][0][0]
            self.fringe['back'][1][0] = self.fringe['top'][1][0]
            self.fringe['back'][2][0] = self.fringe['top'][1][0]

            self.fringe['top'][0][0] = cache[0]
            self.fringe['top'][1][0] = cache[1]
            self.fringe['top'][2][0] = cache[2]

            ########
            cache = [self.fringe['left'][0][0], self.fringe['left'][0][1]]
            self.fringe['left'][0][0] = self.fringe['left'][0][2]
            self.fringe['left'][0][1] = self.fringe['left'][1][2]
            self.fringe['left'][0][2] = self.fringe['left'][2][2]
            self.fringe['left'][1][2] = self.fringe['left'][2][1]
            self.fringe['left'][2][2] = self.fringe['left'][2][0]
            self.fringe['left'][2][1] = self.fringe['left'][1][0]
            self.fringe['left'][2][0] = cache[0]
            self.fringe['left'][1][0] = cache[1]


        if direction == 'L-':
            self.rotate('L+', True)
            self.rotate('L+', True)
            self.rotate('L+', True)

        if direction == 'R+':
            cache = [self.fringe['front'][0][2], self.fringe['front'][1][2], self.fringe['front'][2][2]]
            self.fringe['front'][0][2] = self.fringe['bottom'][0][2]
            self.fringe['front'][1][2] = self.fringe['bottom'][1][2]
            self.fringe['front'][2][2] = self.fringe['bottom'][1][2]

            self.fringe['bottom'][0][2] = self.fringe['back'][0][2]
            self.fringe['bottom'][1][2] = self.fringe['back'][1][2]
            self.fringe['bottom'][2][2] = self.fringe['back'][1][2]

            self.fringe['back'][0][2] = self.fringe['top'][0][2]
            self.fringe['back'][1][2] = self.fringe['top'][1][2]
            self.fringe['back'][2][2] = self.fringe['top'][1][2]

            self.fringe['top'][0][2] = cache[0]
            self.fringe['top'][1][2] = cache[1]
            self.fringe['top'][2][2] = cache[2]
            ########
            cache = [self.fringe['right'][0][0], self.fringe['right'][0][1]]
            self.fringe['right'][0][0] = self.fringe['right'][2][0]
            self.fringe['right'][0][1] = self.fringe['right'][1][0]
            self.fringe['right'][2][0] = self.fringe['right'][2][2]
            self.fringe['right'][1][0] = self.fringe['right'][2][1]
            self.fringe['right'][2][2] = self.fringe['right'][0][2]
            self.fringe['right'][2][1] = self.fringe['right'][1][2]
            self.fringe['right'][0][2] = cache[0]
            self.fringe['right'][1][2] = cache[1]

        if direction == 'R-':
            self.rotate('R+', True)
            self.rotate('R+', True)
            self.rotate('R+', True)

        if direction == 'U+':
            cache = [self.fringe['left'][0][0], self.fringe['left'][0][1], self.fringe['left'][0][2]]
            self.fringe['left'][0][0] = self.fringe['back'][2][2]
            self.fringe['left'][0][1] = self.fringe['back'][2][1]
            self.fringe['left'][0][2] = self.fringe['back'][2][0]

            self.fringe['back'][2][0] = self.fringe['right'][0][2]
            self.fringe['back'][2][1] = self.fringe['right'][0][1]
            self.fringe['back'][2][2] = self.fringe['right'][0][0]

            self.fringe['right'][0][0] = self.fringe['front'][0][0]
            self.fringe['right'][0][1] = self.fringe['front'][0][1]
            self.fringe['right'][0][2] = self.fringe['front'][0][2]

            self.fringe['front'][0][0] = cache[0]
            self.fringe['front'][0][1] = cache[1]
            self.fringe['front'][0][2] = cache[2]

            ########
            cache = [self.fringe['top'][0][0], self.fringe['top'][0][1]]
            self.fringe['top'][0][0] = self.fringe['top'][0][2]
            self.fringe['top'][0][1] = self.fringe['top'][1][2]
            self.fringe['top'][0][2] = self.fringe['top'][2][2]
            self.fringe['top'][1][2] = self.fringe['top'][2][1]
            self.fringe['top'][2][2] = self.fringe['top'][2][0]
            self.fringe['top'][2][1] = self.fringe['top'][1][0]
            self.fringe['top'][2][0] = cache[0]
            self.fringe['top'][1][0] = cache[1]

        if direction == 'U-':
            self.rotate('U+', True)
            self.rotate('U+', True)
            self.rotate('U+', True)

        if direction == 'D+':
            cache = [self.fringe['left'][2][0], self.fringe['left'][2][1], self.fringe['left'][2][2]]
            self.fringe['left'][2][0] = self.fringe['back'][0][2]
            self.fringe['left'][2][1] = self.fringe['back'][0][1]
            self.fringe['left'][2][2] = self.fringe['back'][0][0]

            self.fringe['back'][0][0] = self.fringe['right'][2][2]
            self.fringe['back'][0][1] = self.fringe['right'][2][1]
            self.fringe['back'][0][2] = self.fringe['right'][2][0]

            self.fringe['right'][2][0] = self.fringe['front'][2][0]
            self.fringe['right'][2][1] = self.fringe['front'][2][1]
            self.fringe['right'][2][2] = self.fringe['front'][2][2]

            self.fringe['front'][2][0] = cache[0]
            self.fringe['front'][2][1] = cache[1]
            self.fringe['front'][2][2] = cache[2]

            ########
            cache = [self.fringe['bottom'][0][0], self.fringe['bottom'][0][1]]
            self.fringe['bottom'][0][0] = self.fringe['bottom'][2][0]
            self.fringe['bottom'][0][1] = self.fringe['bottom'][1][0]
            self.fringe['bottom'][2][0] = self.fringe['bottom'][2][2]
            self.fringe['bottom'][1][0] = self.fringe['bottom'][2][1]
            self.fringe['bottom'][2][2] = self.fringe['bottom'][0][2]
            self.fringe['bottom'][2][1] = self.fringe['bottom'][1][2]
            self.fringe['bottom'][0][2] = cache[0]
            self.fringe['bottom'][1][2] = cache[1]

        if direction == 'D-':
            self.rotate('D+', True)
            self.rotate('D+', True)
            self.rotate('D+', True)

        if direction == 'B+':
            cache = [self.fringe['top'][0][0], self.fringe['top'][0][1], self.fringe['top'][0][2]]
            self.fringe['top'][0][0] = self.fringe['left'][2][0]
            self.fringe['top'][0][1] = self.fringe['left'][1][0]
            self.fringe['top'][0][2] = self.fringe['left'][0][0]

            self.fringe['left'][0][0] = self.fringe['bottom'][2][0]
            self.fringe['left'][1][0] = self.fringe['bottom'][2][1]
            self.fringe['left'][2][0] = self.fringe['bottom'][2][2]

            self.fringe['bottom'][2][0] = self.fringe['right'][2][2]
            self.fringe['bottom'][2][1] = self.fringe['right'][1][2]
            self.fringe['bottom'][2][2] = self.fringe['right'][0][2]

            self.fringe['right'][0][2] = cache[0]
            self.fringe['right'][1][2] = cache[1]
            self.fringe['right'][2][2] = cache[2]

            ########
            cache = [self.fringe['back'][0][0], self.fringe['back'][0][1]]
            self.fringe['back'][0][0] = self.fringe['back'][0][2]
            self.fringe['back'][0][1] = self.fringe['back'][1][2]
            self.fringe['back'][0][2] = self.fringe['back'][2][2]
            self.fringe['back'][1][2] = self.fringe['back'][2][1]
            self.fringe['back'][2][2] = self.fringe['back'][2][0]
            self.fringe['back'][2][1] = self.fringe['back'][1][0]
            self.fringe['back'][2][0] = cache[0]
            self.fringe['back'][1][0] = cache[1]

        if direction == 'B-':
            self.rotate('B+', True)
            self.rotate('B+', True)
            self.rotate('B+', True)

        if direction == 'F+':
            cache = [self.fringe['top'][2][0], self.fringe['top'][2][1], self.fringe['top'][2][2]]
            self.fringe['top'][2][0] = self.fringe['left'][2][2]
            self.fringe['top'][2][1] = self.fringe['left'][1][2]
            self.fringe['top'][2][2] = self.fringe['left'][0][2]

            self.fringe['left'][0][2] = self.fringe['bottom'][0][0]
            self.fringe['left'][1][2] = self.fringe['bottom'][0][1]
            self.fringe['left'][2][2] = self.fringe['bottom'][0][2]

            self.fringe['bottom'][0][0] = self.fringe['right'][2][0]
            self.fringe['bottom'][0][1] = self.fringe['right'][1][0]
            self.fringe['bottom'][0][2] = self.fringe['right'][0][0]

            self.fringe['right'][0][0] = cache[0]
            self.fringe['right'][1][0] = cache[1]
            self.fringe['right'][2][0] = cache[2]

            ########
            cache = [self.fringe['front'][0][0], self.fringe['front'][0][1]]
            self.fringe['front'][0][0] = self.fringe['front'][2][0]
            self.fringe['front'][0][1] = self.fringe['front'][1][0]
            self.fringe['front'][2][0] = self.fringe['front'][2][2]
            self.fringe['front'][1][0] = self.fringe['front'][2][1]
            self.fringe['front'][2][2] = self.fringe['front'][0][2]
            self.fringe['front'][2][1] = self.fringe['front'][1][2]
            self.fringe['front'][0][2] = cache[0]
            self.fringe['front'][1][2] = cache[1]

        if direction == 'F-':
            self.rotate('F+', True)
            self.rotate('F+', True)
            self.rotate('F+', True)

        if not is_recursive_call and not Cube.__global_visualizer is None:
            Cube.__global_visualizer.notify('rotated', sender = self, args = (previous_state, direction))

        self.previous_state = previous_state

    def is_equal_to(self, cube):
        return self.get_distance(cube) == 0

    @classmethod
    def get_fringes_difference(cls, f1, f2):
        diff = 0
        for line in range(len(f1)):
            for cell in range(len(f1[line])):
                if f1[line][cell] != f2[line][cell]:
                    diff += 1
        return diff

    def randomize(self):
        count = random.randint(30, 100)
        for r in range(count):
            command = self.directions[random.randint(0, len(self.directions) - 1)]
            self.rotate(command)


    def __init__fringes(self):
        self.fringe['top'] = Cube.__gen_fringe('Y')
        self.fringe['front'] = Cube.__gen_fringe('R')
        self.fringe['bottom'] = Cube.__gen_fringe('W')
        self.fringe['back'] = Cube.__gen_fringe('B')
        self.fringe['left'] = Cube.__gen_fringe('G')
        self.fringe['right'] = Cube.__gen_fringe('O')

    def print_cube(self):
#        for f in self.fringe:
#            print f, ':\n', self.fringe[f][0], '\n', self.fringe[f][1], '\n', self.fringe[f][2]
        print '_______________________________________________'
        Cube.print_3(Cube.__gen_fringe(' '), self.fringe['top'], Cube.__gen_fringe(' '))
        Cube.print_3(self.fringe['left'], self.fringe['front'], self.fringe['right'])
        Cube.print_3(Cube.__gen_fringe(' '), self.fringe['bottom'], Cube.__gen_fringe(' '))
        Cube.print_3(Cube.__gen_fringe(' '), self.fringe['back'], Cube.__gen_fringe(' '))


    @classmethod
    def __gen_fringe(cls, color):
        return [[color, color, color],\
                [color, color, color],\
                [color, color, color]]

    def solve(self):
        pass

    @classmethod
    def print_3(cls, f1, f2, f3):
        print f1[0], f2[0], f3[0]
        print f1[1], f2[1], f3[1]
        print f1[2], f2[2], f3[2]

    def copy(self):
        return copy.deepcopy(self)

    def get_distance(self, cube):
        cube_diff = 0
        for f in self.fringe.keys():
            cube_diff += Cube.get_fringes_difference(self.fringe[f], cube.fringe[f])
        return cube_diff