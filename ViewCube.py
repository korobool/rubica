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
        self.cube = []
        
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
#        if args[2] == 'L+':
#            self.L_pluse()
        pass

    def init_drawing(self, args):
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
        
        self.cube.append(box1)
        self.cube.append(box1_1)
#        self.cube['4'] = [box4]
#        self.cube['7'] = [box7]
    
    def rotate_X(self, figure):
        
        pass#figure
    
    def L_pluse(self):
#        cube_list = [self.cube[1],
#                     self.cube[4],
#                     self.cube[7]
#                     ]
#        import pdb;pdb.set_trace()
        #L_pluse_list = [cube_list[i][i] for i in cube_list]

#        for i in range(self.range_rotate):
#            rate(self.speed_rotate)
#            box1.rotate(angle=-pi/(self.range_rotate*2), axis=vector((1,0,0)),
#                        origin=(0,0,0))
#            box1_1.rotate(angle=-pi/(self.range_rotate*2), axis=vector((1,0,0)),
#                          origin=(0,0,0))
#        
#        for elements in 
        pass
    
class Box:
    def __init__(self, id, box):
        self.id = id
        self.box = box
    