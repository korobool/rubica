__author__ = 'oleksandr'

# The idea of this class is to visualize cubic rubica states and transformations
# using VPython or pygame or something else. Cube class supports injecting observer
# object which is in fact just an event processing subsystem. To make visualizer 
# work properly developer should use contract (Cube will notify instance of this 
# class automaticaly)

class Visualizer:
    def notify(self, notification, args):
        print notification, args
        if notification == 'created':
            self.__init_drawing(args) # Init drawing window and subsystem
        if notification == 'rotated':
            self.__animate(args)

    def __animate(self, args):
        pass

    def __init_drawing(self, args):
        pass