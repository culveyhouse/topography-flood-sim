#!/usr/bin/env python

import sys
import argparse
import time
import random

# Default dimensions if no 2D grid length / width specified
DEFAULT_LENGTH, DEFAULT_WIDTH, DEFAULT_MAX_HEIGHT = 8, 8, 10 
# Descriptive key of 3D grid contents
CONTENT_AIR, CONTENT_BOARD, CONTENT_WATER = 0, 1, 2

parser = argparse.ArgumentParser(description='Just an argparse test.')
parser.add_argument('-l','--length', dest='grid_length', metavar='grid length',
                    type=int, default=None, help='length of random \
                    topography grid')
parser.add_argument('-w','--width', dest='grid_width', metavar='grid width', 
                    type=int, default=None, help='width of random topography \
                    grid')
parser.add_argument('--mh','--max-height', dest='max_height', 
                    metavar='maximum height', type=int, default=None, 
                    help='maximum height of random topography grid')
args = parser.parse_args() 
 

class MakeCartesianGrid:
    """
    MakeCartesianGrid accepts input of heights for a 2-dimensional grid of squares, then
    produces a 3D array (cartesian grid) representing that topography. 
    The 3D array's height is simply the height of the square with the highest elevation.
    The 3D array will store contents as follows: 0: air, 1: board, and 2: water.

    ...

    Attributes
    ----------
    grid_array : the 2D grid represented as a 2D array 
    length : int
        the length from the 2D grid input
    width : int
        the width from the 2D grid input
    height : int
        the height of the 3D grid

    Methods
    -------
    extrude(self.grid_array)
        Produces the 3D array by extruding the heights of each grid square.
    """      
    def __init__(self, grid, height):
        self.length = len(grid[0])
        self.width = len(grid)
        self.height = height
        self.grid = grid        
        
def prepare_grid(topo_grid = None, length = None, width = None, max_height = None):
    """
    prepare_grid accepts a standard Python 2d array input, and normalizes it 
    for extrusion by the MakeCartesianGrid class. It assumes an "x" length 
    based on the length of the first array, then truncates or fills the rest
    of the "y" arrays. It also computes the maximum elevation of the grid's values
    
    Alternatively, instead of passing a 2D array as topo_grid, you may create a 
    random 2D grid of height values by supplying length, width, and maximum height
    desired. 

    Parameters
    ----------
    topo_grid : int, optional
        A 2d python array, square or rectangular
    topo_grid : int, optional
        A 2d python array, square or rectangular
    """
    if topo_grid is None: 
        # Randomizing a 2D grid
        print("Randomizing a 2D grid")
        board_length = length or DEFAULT_LENGTH
        board_width = width or DEFAULT_WIDTH
        board_max_height = max_height or DEFAULT_MAX_HEIGHT

        topo_grid = [[random.randint(0,board_max_height) for i in range(board_length)] for j in range(board_width)]

    else: 
        # trim rows to first row
        board_length = len(topo_grid[0])
        board_width = len(topo_grid)
        board_max_height = max(map(max, topo_grid))
        
        for y in range(len(topo_grid)):
            if len(topo_grid[y]) < board_length:
                topo_grid[y].extend([0 for i in range((board_length-len(topo_grid[y])))])  
            topo_grid[y] = topo_grid[y][0:board_length]

    return topo_grid, board_max_height
    
def print_grid(topo_grid):
    for i in range(len(topo_grid)):
        for j in range(len(topo_grid[0])):
            #print(topo_grid[i][j], end='|')
            #print("{:<2}".format(topo_grid[i][j]), end="|")
            print(str(topo_grid[i][j]).rjust(3), end="|")
        print("") 

if __name__ == '__main__':
    topo_grid, board_max_height = prepare_grid(length=args.grid_length, width=args.grid_width, max_height=args.max_height)   
    print_grid(topo_grid)
    print(board_max_height)