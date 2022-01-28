#!/usr/bin/env python

import sys
import argparse
import time
import random

# Default dimensions if no 2D grid length / width specified
DEFAULT_LENGTH, DEFAULT_WIDTH, DEFAULT_MAX_HEIGHT = 8, 8, 10 
# Descriptive key of 3D grid contents
CONTENT_AIR, CONTENT_BOARD, CONTENT_WATER = 0, 1, 2

'''
The argument parser is used if the user wishes to generate random grids
without passing a user-defined grid through the program.
The user may specify any of the following: length, width, and/or maximum 
height of the "topography" to be generated.
'''
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
    MakeCartesianGrid accepts input of heights for a 2-dimensional grid of
    squares, then produces a 3D array (cartesian grid) representing that 
    topography. 
    
    The 3D array's height is simply the height of the square with the highest
    elevation. The 3D array will store contents as follows: 0: air, 1: board,
    and 2: water.

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
    of the "y" arrays. It also computes the maximum elevation of the grid's
    values.
    
    Alternatively, instead of passing a 2D array as topo_grid, you may create a 
    random 2D grid of height values by supplying length, width, and maximum
    height desired. 

    Parameters
    ----------
    topo_grid : int, optional
        A 2d python array, square or rectangular
    length : int, optional, defaults to DEFAULT_LENGTH
        Desired length of a randomized 2D grid
    width : int, optional, defaults to DEFAULT_WIDTH
        Desired width of a randomized 2D grid, 
    max_height : int, optional, defaults to DEFAULT_MAX_HEIGHT
       Maximum values (height) of a randomized 2D grid

    Returns
    -------
    (topo_grid, board_max_height) : tuple (array/list of lists, int)
        1. The final 2D array, or in other words a groomed grid 
        for use with MakeCartesianGrid, and
        2. The maximum value detected in the 2D grid, also called
        maximum height.
    """
    
    if topo_grid is None: 
        # Randomizing a 2D grid
        print("Randomizing a 2D grid")
        board_length = length or DEFAULT_LENGTH
        board_width = width or DEFAULT_WIDTH
        board_max_height = max_height or DEFAULT_MAX_HEIGHT

        topo_grid = [[random.randint(0,board_max_height) 
            for i in range(board_length)] for j in range(board_width)]

    else: 
        # trim rows to first row
        board_length = len(topo_grid[0])
        board_width = len(topo_grid)
        board_max_height = max(map(max, topo_grid))
        
        # Fill incomplete rows with zeros for uniform row length
        for y in range(board_width):
            row = topo_grid[y]
            if len(row) < board_length:
                row.extend([0 for i in range((board_length-len(row)))])  
            topo_grid[y] = row[0:board_length]

    return topo_grid, board_max_height
    
def print_grid(topo_grid):
    """
    Prints a right-aligned table of integers representing the heights
    of each square in the 2D array passed. This grid printer allows
    for integers of up to 3 digits. The 2D array must be square or
    rectangular, as there is currently no error handling for 
    extraneous array elements. 


    Parameters
    ----------
    topo_grid : int
        A 2d python array of integers, square or rectangular
    """    
    for i in range(len(topo_grid)):
        for j in range(len(topo_grid[0])):
            print(str(topo_grid[i][j]).rjust(3), end="|")
        print("") 

if __name__ == '__main__':
    (topo_grid, board_max_height) = prepare_grid(length=args.grid_length, 
        width=args.grid_width, max_height=args.max_height)   
    print_grid(topo_grid)
    print(board_max_height)