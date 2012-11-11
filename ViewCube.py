__author__ = 'oleksandr'

# The idea of this class is to visualize cubic rubica states and transformations
# using VPython or pygame or something else. Cube class supports observer object 
# injection which is in fact just an event processing subsystem. To make visualizer 
# work properly developer should use contract (Cube will notify instance of this 
# class automaticaly)

from visual import *

class Visualizer:
    
    def __init__(self):
        self.speed_rotate = 100
        self.range_rotate = 50
        self.axes()
        self.d = 0.05 # delta between boxes
        self.arris = 1
        scene.center = (0, 0, 0)
        scene.forward = (-1, -1, -1)
        scene.scale = (0.2,0.2,0.2)
        self.cube = {}
        
    def axes(self):
        x = arrow(pos=(0,0,0), axis=(5,0,0), shaftwidth=0.1)
        y = arrow(pos=(0,0,0), axis=(0,0,5), shaftwidth=0.1)
        z = arrow(pos=(0,0,0), axis=(0,5,0), shaftwidth=0.1)

    #self.observer().notify('rotated', sender = self, args = (previous_state, direction))
    def notify(self, notification, sender = None, args = None):
        if notification == 'created':
            self.init_drawing(sender) # Init drawing window and subsystem
        if notification == 'rotated':
            self.animate(args)

    def animate(self, args):
        if args[1] == 'L+':
            self.L_pluse()
        pass

    def init_drawing(self, model):
        color_height = 0.01
        color_wide = 0.9
        
        box1 = box(pos=(-1-self.d,1+self.d,1+self.d),
                   length=self.arris, height=self.arris, width=self.arris,
                   color=color.white)
        box1_1 = box(pos=(box1.pos[0]-(self.arris/2.0),box1.pos[2],box1.pos[2]),
                     length=color_height, height=color_wide, width=color_wide,
                     color=color.green)
        box4 = box(pos=(-1-self.d,0,1+self.d),
                   length=self.arris, height=self.arris, width=self.arris,
                   color=color.white)
        box7 = box(pos=(-1-self.d,-1-self.d,1+self.d),
                   length=self.arris, height=self.arris, width=self.arris,
                   color=color.white)
        box10 = box(pos=(-1-self.d,1+self.d,0),
                   length=self.arris, height=self.arris, width=self.arris,
                   color=color.white)
        box13 = box(pos=(-1-self.d,0,0),
                   length=self.arris, height=self.arris, width=self.arris,
                   color=color.white)
        box16 = box(pos=(-1-self.d,-1-self.d,0),
                   length=self.arris, height=self.arris, width=self.arris,
                   color=color.white)
        box19 = box(pos=(-1-self.d,1+self.d,-1-self.d),
                   length=self.arris, height=self.arris, width=self.arris,
                   color=color.white)
        box22 = box(pos=(-1-self.d,0,-1-self.d),
                   length=self.arris, height=self.arris, width=self.arris,
                   color=color.white)
        box25 = box(pos=(-1-self.d,-1-self.d,-1-self.d),
                   length=self.arris, height=self.arris, width=self.arris,
                   color=color.white)
        
        self.cube[1] = [box1, box1_1]
        self.cube[4] = [box4]
        self.cube[7] = [box7]
        self.cube[10] = [box10]
        self.cube[13] = [box13]
        self.cube[16] = [box16]
        self.cube[19] = [box19]
        self.cube[22] = [box22]
        self.cube[25] = [box25]
    
    def rotate_X(self, figure):
        figure.rotate(angle=-pi/(self.range_rotate*2), axis=vector((1,0,0)),
            origin=(0,0,0))
    
    def L_pluse(self):
        cube_list = [self.cube[1], self.cube[4], self.cube[7],
                     self.cube[10],self.cube[13],self.cube[16],
                     self.cube[19],self.cube[22],self.cube[25],]
        L_pluse_list = [j for i in cube_list for j in i]
        for i in range(self.range_rotate):
            rate(self.speed_rotate)
            for j in L_pluse_list:
                self.rotate_X(j)
    
class Box:
    def __init__(self, id, box):
        self.id = id
        self.box = box
    