#!/usr/bin/python
# Dragon curve plotter
# using matplotlib.plot
#
# Actually, NSEW is not very practical
# now, direction will be measured by polar
# coordinates.
#
# all function will have this prototype
# def goDirection( coord, direction )
# @param list coord[x, y]
# @param list direction angle in radian
#
# coord = [x, y]
#

import math

# z is magnitude, ang is direction in radian
def pol2cart(z, ang):
    return z*math.cos(ang), z*math.sin(ang)

def cart2pol(x, y):
    z = math.sqrt(math.pow(x,2)+math.pow(x,2))
    return z, math.atan(y/x)

def goStraight(coord, direction):
    x,y = math.cos(direction), math.sin(direction)
    return [coord[0]+x,coord[1]+y], direction

def goRight(coord, direction):
    direction -= math.pi/2
    x,y = math.cos(direction), math.sin(direction)
    return [coord[0]+x,coord[1]+y], direction

def goLeft(coord, direction):
    direction += math.pi/2
    x,y = math.cos(direction), math.sin(direction)
    return [coord[0]+x,coord[1]+y], direction

## Pretty Plot
# usable to give -rectangular, -full, -beautiful plot
def prettyPlot(xData, yData, plotType='-k'):
    import matplotlib.pyplot as plt
    #Add 'buffer' to min-max x and y value
    buf = 5.0
    # plt.axis( [xmin, xmax, ymin, ymax] )
    plt.axis('equal')
    ax = np.array([min(xData)-buf, max(xData)+buf, min(yData)-buf, max(yData)+buf])
    plt.axis(ax)
    plt.plot(xData,yData,plotType)
    plt.show()

if __name__ == '__main__':
    import matplotlib.pyplot as plt
    import dragonfrac
    import numpy as np
    import argparse
    # We'll request input from user
    parser = argparse.ArgumentParser(description='Draw dragon fractal')
    parser.add_argument('num', metavar='N', type=int, help='Number of iteration')
    args = parser.parse_args()
    command = dragonfrac.dragoncurv(args.num)
    startPt = [1.,1.]
    startDir = math.radians(90)
    xPlot = []
    yPlot = []
    xPlot.append(startPt[0])
    yPlot.append(startPt[1])

    for x in command:
        if x=='F':
            startPt, startDir = goStraight(startPt, startDir)
        elif x=='R':
            startPt, startDir = goRight(startPt, startDir)
        elif x=='L':
            startPt, startDir = goLeft(startPt, startDir)

        xPlot.append(startPt[0])
        yPlot.append(startPt[1])

    x1 = np.array(xPlot)
    y1 = np.array(yPlot)
    prettyPlot(x1,y1)
