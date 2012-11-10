__author__ = 'oleksandr'

import copy
import random

class Cube():

    def __init__(self, observer = None):
        self.fringe = {}
        self.__init__fringes()
        self.observer = observer
        self.directions = ('L+', 'L-', 'R+', 'R-', 'U+', 'U-', 'D+', 'D-', 'B+', 'B-', 'F+', 'F-')

        if not self.observer is None:
            self.observer.notify('created', self)

    def rotate(self, direction):

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

        if direction == 'L-':
            self.rotate('L+')
            self.rotate('L+')
            self.rotate('L+')

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

        if direction == 'R-':
            self.rotate('R+')
            self.rotate('R+')
            self.rotate('R+')

        if direction == 'U+':
            cache = self.fringe['left'][0]
            self.fringe['left'][0] = self.fringe['back'][0]
            self.fringe['back'][0] = self.fringe['right'][0]
            self.fringe['right'][0] = self.fringe['front'][0]
            self.fringe['front'][0] = cache

        if direction == 'U-':
            self.rotate('U+')
            self.rotate('U+')
            self.rotate('U+')

        if direction == 'D+':
            cache = self.fringe['left'][2]
            self.fringe['left'][2] = self.fringe['back'][2]
            self.fringe['back'][2] = self.fringe['right'][2]
            self.fringe['right'][2] = self.fringe['front'][2]
            self.fringe['front'][2] = cache

        if direction == 'D-':
            self.rotate('D+')
            self.rotate('D+')
            self.rotate('D+')

        if direction == 'B+':
            pass

        if direction == 'B-':
            self.rotate('B+')
            self.rotate('B+')
            self.rotate('B+')

        if direction == 'F+':
            pass

        if direction == 'F-':
            self.rotate('F+')
            self.rotate('F+')
            self.rotate('F+')

        if not self.observer is None:
            self.observer.notify('rotated', (self, direction))

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
        self.fringe['bottom'] = Cube.__gen_fringe('B')
        self.fringe['back'] = Cube.__gen_fringe('W')
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