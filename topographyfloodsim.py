#!/usr/bin/env python

import sys
import argparse
import time

# Default dimensions if no 2D grid length / width specified
DEFAULT_LENGTH, DEFAULT_WIDTH, DEFAULT_HEIGHT = 8, 8, 10 
# Descriptive key of 3D grid contents
CONTENT_AIR, CONTENT_BOARD, CONTENT_WATER = 0, 1, 2

parser = argparse.ArgumentParser(description='Just an argparse test.')
parser.add_argument('-l','--length', metavar='grid length', type=int, nargs='?', default=DEFAULT_LENGTH,
                    help='length of topography grid')
parser.add_argument('-w','--width', metavar='grid width', type=int, nargs='?', default=DEFAULT_WIDTH, 
                    help='width of topography grid')
parser.add_argument('-g','--grid', dest='area', action='store_true',
                    help='2D python array, e.g.: [[0,1,0],[1,1,1],[0,2,0]]')
                    
args = parser.parse_args() 
if args.area:
    calc_area = args.length * args.width
    print(f"The area of the grid is {calc_area}.")
    
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
    def __init__(self, length, width, height, grid):
        self.length = length
        self.width = width
        self.height = height
        self.grid = grid        
        
def prepare_grid(chessboard = None):
    """
    prepare_grid accepts a standard Python 2d array input, and normalizes it 
    for extrusion by the MakeCartesianGrid class. It assumes an "x" length 
    based on the length of the first array, then truncates or fills the rest
    of the "y" arrays. It also computes the maximum elevation of the grid's values

    Parameters
    ----------
    chessboard : int, optional
        A 2d python array, square or rectangular

    """
    if chessboard is None: 
        print("Randomizing a 2D grid")
        # To be added
        chessboard = [[0,1,1],[0,3,1],[3,2,2]]
        
    print(chessboard)

    return chessboard
    