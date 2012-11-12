__author__ = 'oleksandr'

# The idea of this class is to visualize cubic rubica states and transformations
# using VPython or pygame or something else. Cube class supports observer object 
# injection which is in fact just an event processing subsystem. To make visualizer 
# work properly developer should use contract (Cube will notify instance of this 
# class automaticaly)

from visual import *

class Visualizer:
    
    def __init__(self):
        self.speed_rotate = 150
        self.range_rotate = 50
        # self.axes()
        self.d = 0.05 # delta between boxes
        self.arris = 1
        scene.center = (0, 0, 0)
        scene.forward = (-1, -1, -1)
        scene.scale = (0.2,0.2,0.2)
        self.cube = {}
        
    def axes(self):
        x = arrow(pos=(0,0,0), axis=(3,0,0), shaftwidth=0.1)
        y = arrow(pos=(0,0,0), axis=(0,0,3), shaftwidth=0.1)
        z = arrow(pos=(0,0,0), axis=(0,3,0), shaftwidth=0.1)

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
        box_color = color.white
        box1 = box(pos=(-1-self.d,1+self.d,1+self.d),
                   length=self.arris, height=self.arris, width=self.arris,
                   color=box_color)
        box1_1 = box(pos=(box1.pos[0]-(self.arris/2.0),box1.pos[1],box1.pos[2]),
                     length=color_height, height=color_wide, width=color_wide,
                     color=color.green)
        box1_2 = box(pos=(box1.pos[0],box1.pos[1]+(self.arris/2.0),box1.pos[2]),
                     length=color_wide, height=color_height, width=color_wide,
                     color=color.yellow)
        box1_3 = box(pos=(box1.pos[0],box1.pos[1],box1.pos[2]+(self.arris/2.0)),
                     length=color_wide, height=color_wide, width=color_height,
                     color=color.red)
        box2 = box(pos=(0,1+self.d,1+self.d),
                   length=self.arris, height=self.arris, width=self.arris,
                   color=box_color)
        box2_1 = box(pos=(box2.pos[0],box2.pos[1]+(self.arris/2.0),box2.pos[2]),
                     length=color_wide, height=color_height, width=color_wide,
                     color=color.yellow)
        box2_2 = box(pos=(box2.pos[0],box2.pos[1],box2.pos[2]+(self.arris/2.0)),
                     length=color_wide, height=color_wide, width=color_height,
                     color=color.red)
        box3 = box(pos=(1+self.d,1+self.d,1+self.d),
                   length=self.arris, height=self.arris, width=self.arris,
                   color=box_color)
        box3_1 = box(pos=(box3.pos[0]+(self.arris/2.0),box3.pos[1],box3.pos[2]),
                     length=color_height, height=color_wide, width=color_wide,
                     color=color.orange)
        box3_2 = box(pos=(box3.pos[0],box3.pos[1]+(self.arris/2.0),box3.pos[2]),
                     length=color_wide, height=color_height, width=color_wide,
                     color=color.yellow)
        box3_3 = box(pos=(box3.pos[0],box3.pos[1],box3.pos[2]+(self.arris/2.0)),
                     length=color_wide, height=color_wide, width=color_height,
                     color=color.red)
        box4 = box(pos=(-1-self.d,0,1+self.d),
                   length=self.arris, height=self.arris, width=self.arris,
                   color=color.white)
        box4_1 = box(pos=(box4.pos[0]-(self.arris/2.0),box4.pos[1],box4.pos[2]),
                     length=color_height, height=color_wide, width=color_wide,
                     color=color.green)
        box4_2 = box(pos=(box4.pos[0],box4.pos[1],box4.pos[2]+(self.arris/2.0)),
                     length=color_wide, height=color_wide, width=color_height,
                     color=color.red)
        box5 = box(pos=(0,0,1+self.d),
                   length=self.arris, height=self.arris, width=self.arris,
                   color=color.white)
        box5_1 = box(pos=(box5.pos[0],box5.pos[1],box5.pos[2]+(self.arris/2.0)),
                     length=color_wide, height=color_wide, width=color_height,
                     color=color.red)
        box6 = box(pos=(1+self.d,0,1+self.d),
                   length=self.arris, height=self.arris, width=self.arris,
                   color=color.white)
        box6_1 = box(pos=(box6.pos[0]+(self.arris/2.0),box6.pos[1],box6.pos[2]),
                     length=color_height, height=color_wide, width=color_wide,
                     color=color.orange)
        box6_2 = box(pos=(box6.pos[0],box6.pos[1],box6.pos[2]+(self.arris/2.0)),
                     length=color_wide, height=color_wide, width=color_height,
                     color=color.red)
        box7 = box(pos=(-1-self.d,-1-self.d,1+self.d),
                   length=self.arris, height=self.arris, width=self.arris,
                   color=color.white)
        box7_1 = box(pos=(box7.pos[0]-(self.arris/2.0),box7.pos[1],box7.pos[2]),
                     length=color_height, height=color_wide, width=color_wide,
                     color=color.green)
        box7_2 = box(pos=(box7.pos[0],box7.pos[1]-(self.arris/2.0),box7.pos[2]),
                     length=color_wide, height=color_height, width=color_wide,
                     color=color.white)
        box7_3 = box(pos=(box7.pos[0],box7.pos[1],box7.pos[2]+(self.arris/2.0)),
                     length=color_wide, height=color_wide, width=color_height,
                     color=color.red)
        box8 = box(pos=(0,-1-self.d,1+self.d),
                   length=self.arris, height=self.arris, width=self.arris,
                   color=color.white)
        box8_1 = box(pos=(box8.pos[0],box8.pos[1]-(self.arris/2.0),box8.pos[2]),
                     length=color_wide, height=color_height, width=color_wide,
                     color=color.white)
        box8_2 = box(pos=(box8.pos[0],box8.pos[1],box8.pos[2]+(self.arris/2.0)),
                     length=color_wide, height=color_wide, width=color_height,
                     color=color.red)
        box9 = box(pos=(1+self.d,-1-self.d,1+self.d),
                   length=self.arris, height=self.arris, width=self.arris,
                   color=color.white)
        box9_1 = box(pos=(box9.pos[0]+(self.arris/2.0),box9.pos[1],box9.pos[2]),
                     length=color_height, height=color_wide, width=color_wide,
                     color=color.orange)
        box9_2 = box(pos=(box9.pos[0],box9.pos[1]-(self.arris/2.0),box9.pos[2]),
                     length=color_wide, height=color_height, width=color_wide,
                     color=color.white)
        box9_3 = box(pos=(box9.pos[0],box9.pos[1],box9.pos[2]+(self.arris/2.0)),
                     length=color_wide, height=color_wide, width=color_height,
                     color=color.red)
        box10 = box(pos=(-1-self.d,1+self.d,0),
                   length=self.arris, height=self.arris, width=self.arris,
                   color=color.white)
        box10_1 = box(pos=(box10.pos[0]-(self.arris/2.0),box10.pos[1],box10.pos[2]),
                     length=color_height, height=color_wide, width=color_wide,
                     color=color.green)
        box10_2 = box(pos=(box10.pos[0],box10.pos[1]+(self.arris/2.0),box10.pos[2]),
                     length=color_wide, height=color_height, width=color_wide,
                     color=color.yellow)
        box11 = box(pos=(0,1+self.d,0),
                   length=self.arris, height=self.arris, width=self.arris,
                   color=color.white)
        box11_1 = box(pos=(box11.pos[0],box11.pos[1]+(self.arris/2.0),box11.pos[2]),
                     length=color_wide, height=color_height, width=color_wide,
                     color=color.yellow)
        box12 = box(pos=(1+self.d,1+self.d,0),
                   length=self.arris, height=self.arris, width=self.arris,
                   color=color.white)
        box12_1 = box(pos=(box12.pos[0]+(self.arris/2.0),box12.pos[1],box12.pos[2]),
                     length=color_height, height=color_wide, width=color_wide,
                     color=color.orange)
        box12_2 = box(pos=(box12.pos[0],box12.pos[1]+(self.arris/2.0),box12.pos[2]),
                     length=color_wide, height=color_height, width=color_wide,
                     color=color.yellow)
        box13 = box(pos=(-1-self.d,0,0),
                   length=self.arris, height=self.arris, width=self.arris,
                   color=color.white)
        box13_1 = box(pos=(box13.pos[0]-(self.arris/2.0),box13.pos[1],box13.pos[2]),
                     length=color_height, height=color_wide, width=color_wide,
                     color=color.green)
        box14 = box(pos=(0,0,0),
                   length=self.arris, height=self.arris, width=self.arris,
                   color=box_color)
        box15 = box(pos=(1+self.d,0,0),
                   length=self.arris, height=self.arris, width=self.arris,
                   color=color.white)
        box15_1 = box(pos=(box15.pos[0]+(self.arris/2.0),box15.pos[1],box15.pos[2]),
                     length=color_height, height=color_wide, width=color_wide,
                     color=color.orange)
        box16 = box(pos=(-1-self.d,-1-self.d,0),
                   length=self.arris, height=self.arris, width=self.arris,
                   color=color.white)
        box16_1 = box(pos=(box16.pos[0]-(self.arris/2.0),box16.pos[1],box16.pos[2]),
                     length=color_height, height=color_wide, width=color_wide,
                     color=color.green)
        box16_2 = box(pos=(box16.pos[0],box16.pos[1]-(self.arris/2.0),box16.pos[2]),
                     length=color_wide, height=color_height, width=color_wide,
                     color=color.white)
        box17 = box(pos=(0,-1-self.d,0),
                   length=self.arris, height=self.arris, width=self.arris,
                   color=color.white)
        box17_1 = box(pos=(box17.pos[0],box17.pos[1]-(self.arris/2.0),box17.pos[2]),
                     length=color_wide, height=color_height, width=color_wide,
                     color=color.white)
        box18 = box(pos=(1+self.d,-1-self.d,0),
                   length=self.arris, height=self.arris, width=self.arris,
                   color=color.white)
        box18_1 = box(pos=(box18.pos[0]+(self.arris/2.0),box18.pos[1],box18.pos[2]),
                     length=color_height, height=color_wide, width=color_wide,
                     color=color.orange)
        box18_2 = box(pos=(box18.pos[0],box18.pos[1]-(self.arris/2.0),box18.pos[2]),
                     length=color_wide, height=color_height, width=color_wide,
                     color=color.white)
        box19 = box(pos=(-1-self.d,1+self.d,-1-self.d),
                   length=self.arris, height=self.arris, width=self.arris,
                   color=color.white)
        box19_1 = box(pos=(box19.pos[0]-(self.arris/2.0),box19.pos[1],box19.pos[2]),
                     length=color_height, height=color_wide, width=color_wide,
                     color=color.green)
        box19_2 = box(pos=(box19.pos[0],box19.pos[1]+(self.arris/2.0),box19.pos[2]),
                     length=color_wide, height=color_height, width=color_wide,
                     color=color.yellow)
        box19_3 = box(pos=(box19.pos[0],box19.pos[1],box19.pos[2]-(self.arris/2.0)),
                     length=color_wide, height=color_wide, width=color_height,
                     color=color.blue)
        box20 = box(pos=(0,1+self.d,-1-self.d),
                   length=self.arris, height=self.arris, width=self.arris,
                   color=color.white)
        box20_1 = box(pos=(box20.pos[0],box20.pos[1]+(self.arris/2.0),box20.pos[2]),
                     length=color_wide, height=color_height, width=color_wide,
                     color=color.yellow)
        box20_2 = box(pos=(box20.pos[0],box20.pos[1],box20.pos[2]-(self.arris/2.0)),
                     length=color_wide, height=color_wide, width=color_height,
                     color=color.blue)
        box21 = box(pos=(1+self.d,1+self.d,-1-self.d),
                   length=self.arris, height=self.arris, width=self.arris,
                   color=color.white)
        box21_1 = box(pos=(box21.pos[0]+(self.arris/2.0),box21.pos[1],box21.pos[2]),
                     length=color_height, height=color_wide, width=color_wide,
                     color=color.orange)
        box21_2 = box(pos=(box21.pos[0],box21.pos[1]+(self.arris/2.0),box21.pos[2]),
                     length=color_wide, height=color_height, width=color_wide,
                     color=color.yellow)
        box21_3 = box(pos=(box21.pos[0],box21.pos[1],box21.pos[2]-(self.arris/2.0)),
                     length=color_wide, height=color_wide, width=color_height,
                     color=color.blue)
        box22 = box(pos=(-1-self.d,0,-1-self.d),
                   length=self.arris, height=self.arris, width=self.arris,
                   color=color.white)
        box22_1 = box(pos=(box22.pos[0]-(self.arris/2.0),box22.pos[1],box22.pos[2]),
                     length=color_height, height=color_wide, width=color_wide,
                     color=color.green)
        box22_2 = box(pos=(box22.pos[0],box22.pos[1],box22.pos[2]-(self.arris/2.0)),
                     length=color_wide, height=color_wide, width=color_height,
                     color=color.blue)
        box23 = box(pos=(0,0,-1-self.d),
                   length=self.arris, height=self.arris, width=self.arris,
                   color=color.white)
        box23_1 = box(pos=(box23.pos[0],box23.pos[1],box23.pos[2]-(self.arris/2.0)),
                     length=color_wide, height=color_wide, width=color_height,
                     color=color.blue)
        box24 = box(pos=(1+self.d,0,-1-self.d),
                   length=self.arris, height=self.arris, width=self.arris,
                   color=color.white)
        box24_1 = box(pos=(box24.pos[0]+(self.arris/2.0),box24.pos[1],box24.pos[2]),
                     length=color_height, height=color_wide, width=color_wide,
                     color=color.orange)
        box24_2 = box(pos=(box24.pos[0],box24.pos[1],box24.pos[2]-(self.arris/2.0)),
                     length=color_wide, height=color_wide, width=color_height,
                     color=color.blue)
        box25 = box(pos=(-1-self.d,-1-self.d,-1-self.d),
                   length=self.arris, height=self.arris, width=self.arris,
                   color=color.white)
        box25_1 = box(pos=(box25.pos[0]-(self.arris/2.0),box25.pos[1],box25.pos[2]),
                     length=color_height, height=color_wide, width=color_wide,
                     color=color.green)
        box25_2 = box(pos=(box25.pos[0],box25.pos[1]-(self.arris/2.0),box25.pos[2]),
                     length=color_wide, height=color_height, width=color_wide,
                     color=color.white)
        box25_3 = box(pos=(box25.pos[0],box25.pos[1],box25.pos[2]-(self.arris/2.0)),
                     length=color_wide, height=color_wide, width=color_height,
                     color=color.blue)
        box26 = box(pos=(0,-1-self.d,-1-self.d),
                   length=self.arris, height=self.arris, width=self.arris,
                   color=box_color)
        box26_1 = box(pos=(box26.pos[0],box26.pos[1]-(self.arris/2.0),box26.pos[2]),
                     length=color_wide, height=color_height, width=color_wide,
                     color=color.white)
        box26_2 = box(pos=(box26.pos[0],box26.pos[1],box26.pos[2]-(self.arris/2.0)),
                     length=color_wide, height=color_wide, width=color_height,
                     color=color.blue)
        box27 = box(pos=(1+self.d,-1-self.d,-1-self.d),
                   length=self.arris, height=self.arris, width=self.arris,
                   color=box_color)
        box27_1 = box(pos=(box27.pos[0]+(self.arris/2.0),box27.pos[1],box27.pos[2]),
                     length=color_height, height=color_wide, width=color_wide,
                     color=color.orange)
        box27_2 = box(pos=(box27.pos[0],box27.pos[1]-(self.arris/2.0),box27.pos[2]),
                     length=color_wide, height=color_height, width=color_wide,
                     color=color.white)
        box27_3 = box(pos=(box27.pos[0],box27.pos[1],box27.pos[2]-(self.arris/2.0)),
                     length=color_wide, height=color_wide, width=color_height,
                     color=color.blue)
        
        self.cube[1] = [box1, box1_1, box1_2, box1_3]
        self.cube[2] = [box2, box2_1, box2_2]
        self.cube[3] = [box3, box3_1, box3_2, box3_3]
        self.cube[4] = [box4, box4_1, box4_2]
        self.cube[5] = [box5, box5_1]
        self.cube[6] = [box6, box6_1, box6_2]
        self.cube[7] = [box7, box7_1, box7_2, box7_3]
        self.cube[8] = [box8, box8_1, box8_2]
        self.cube[9] = [box9, box9_1, box9_2, box9_3]
        self.cube[10] = [box10, box10_1, box10_2]
        self.cube[11] = [box1, box11_1]
        self.cube[12] = [box12, box12_1, box12_2]
        self.cube[13] = [box13, box13_1]
        self.cube[14] = [box14]
        self.cube[15] = [box15, box15_1]
        self.cube[16] = [box16, box16_1, box16_2]
        self.cube[17] = [box17, box17_1]
        self.cube[18] = [box18, box18_1, box18_2]
        self.cube[19] = [box19, box19_1, box19_2, box19_3]
        self.cube[20] = [box20, box20_1, box20_2]
        self.cube[21] = [box21, box21_1, box21_2, box21_3]
        self.cube[22] = [box22, box22_1, box22_2]
        self.cube[23] = [box23, box23_1]
        self.cube[24] = [box24, box24_1, box24_2]
        self.cube[25] = [box25, box25_1, box25_2, box25_3]
        self.cube[26] = [box26, box26_1, box26_2]
        self.cube[27] = [box27, box27_1, box27_2, box27_3]
    
    def rotate_X(self, figure):
        figure.rotate(angle=-pi/(self.range_rotate*2), axis=vector((1,0,0)),
            origin=(0,0,0))
    
    def L_pluse(self):
        cube_list = [self.cube[1], self.cube[4], self.cube[7],
                     self.cube[10],self.cube[13],self.cube[16],
                     self.cube[19],self.cube[22],self.cube[25]]
        L_pluse_list = [j for i in cube_list for j in i]
        for i in range(self.range_rotate):
            rate(self.speed_rotate)
            for cube in L_pluse_list:
                self.rotate_X(cube)
        # TODO: set new indexes for boxes.
        # import pdb;pdb.set_trace()
