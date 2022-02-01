#!/usr/bin/env Python

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
    Parameters
    ----------
    grid : 2D arr/list of lists
        the 2D grid represented as a 2D Python array 
    height : int
        the height of the 3D grid
    manual_run : bool, optional, default False
        flag to indicate whether to automatically run the extrusion 
    
    Attributes
    ----------
    grid : the 2D grid represented as a 2D Python array 
    length : int
        the length from the 2D grid input
    width : int
        the width from the 2D grid input
    cubes : list of list of list of TopoCube objects
        a 3D cube matrix of TopoCube instances used to track contents of the 3D 
        space

    Methods
    -------
    extrude()
        Produces a 3D array by extruding the heights of each grid square.
    """      
    
    def __init__(self, grid, height, manual_run = False):
        self.length = len(grid[0])
        self.width = len(grid)
        self.height = height
        self.grid = grid
        self.cube_grid = \
            [[[CONTENT_AIR for z in range(self.height)] \
            for y in range(self.width)] \
            for x in range(self.length)] 
        self.cubes = \
            [[[CONTENT_AIR for z in range(self.height)] \
            for y in range(self.width)] \
            for x in range(self.length)] 
        if not manual_run:
            self.extrude()
        
    def extrude(self, grid=None):
        """
        extrude() creates a 3D array representing a 3D Cartesian grid of cubes, 
        starting with the 2D topo_grid array and extruding each square into a 
        z-axis per the value (height) of each array element. The
        topographical 'cubes' will have a value of 1 (board material), and all
        other cubes will have a value of 0 (air material)
        
        Parameters
        ----------
        grid : 2D arr/list of lists, optional
            A Python 2D array (list of lists) which can be passed to override
            the grid_array already defined within the class init.
    
        Returns
        -------
        cube_grid : 3D arr/list of list of lists
            A fullly extruded 3d Python array, with int values of either 0 (air)
            or 1 (board)
        """
        
        if grid is None:
            grid = self.grid

        # Build the 3D grid in order of y, x, and then z axes
        for y in range(self.width):
            for x in range(self.length):
                for z in range(self.height):
                    self.cubes[x][y][z] = TopoCube(coords=(x,y,z))
                
                    if grid[y][x]-1>=z:
                        self.cube_grid[x][y][z]=CONTENT_BOARD
                        self.cubes[x][y][z].content = CONTENT_BOARD
                        
        return self.cube_grid

class TopoCube:
    """
    TopoCube allows for a collection of Cube objects that compose a 3D
    cartesian grid. TopoCube objects are created in the MakeCartesianGrid
    class, and are created en masse on 3D grid initialization. For example,
    an 8x8x8 grid will instantiate 512 objects. 
    
    For this reason, this is a "lite" class using the __slots__ method
    which keeps each cube object lightweight and speeds up data retrieval.
    
    ...
    Attributes
    ----------
    coords : list
        (x, y, z) coordinates of the cube 
    content : int, default 0
        The material currently occupying the cube via 3 global variables:
        0: air, 1: board, 2: water
    drains_out : bool, default False
        flag to indicate if this cube drains to any lower height 
    """
    
    __slots__ = ('coords', 'content', 'drains_out', 'resolved')
    
    def __init__(self, coords: list, content = 0, drains_out = False, 
        resolved = False):
        self.coords = coords
        self.content = int(content)
        self.drains_out = drains_out
        self.resolved = resolved


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
    topo_grid : 2D arr/list of lists, optional
        A 2d Python array, square or rectangular
    length : int, optional, defaults to DEFAULT_LENGTH
        Desired length of a randomized 2D grid
    width : int, optional, defaults to DEFAULT_WIDTH
        Desired width of a randomized 2D grid, 
    max_height : int, optional, defaults to DEFAULT_MAX_HEIGHT
       Maximum values (height) of a randomized 2D grid

    Returns
    -------
    (topo_grid, board_max_height) : tuple (2D arr/list of lists, int)
        1. The final 2D array, or in other words a groomed grid 
        for use with MakeCartesianGrid, and
        2. The maximum value detected in the 2D grid, also called
        maximum height.
    """
    
    if topo_grid is None: 
        # randomizing a 2D grid
        board_length = length or DEFAULT_LENGTH
        board_width = width or DEFAULT_WIDTH
        board_max_height = max_height or DEFAULT_MAX_HEIGHT
        print(f"Randomizing a 2D grid of {board_length}x{board_width} with " + 
            f"values 0-{board_max_height}")

        #Randomize values in 2D array up to maximum height calculated above
        topo_grid = [[random.randint(0,board_max_height) 
            for i in range(board_length)] for j in range(board_width)]
        print("Your random 2D grid is:")
        print(print_grid(topo_grid))

    else: 
        # base board length on the first row's length
        board_length = len(topo_grid[0])
        board_width = len(topo_grid)
        board_max_height = max(map(max, topo_grid))
        
        # Fill incomplete rows with zeros for uniform row length
        for y in range(board_width):
            row = topo_grid[y]
            if len(row) < board_length:
                row.extend([0 for i in range((board_length-len(row)))])  
            # trim longer rows to first row's length
            topo_grid[y] = row[0:board_length]

    return topo_grid, board_max_height
    
def print_grid(topo_grid):
    """
    Prints a right-aligned table of integers representing the heights
    of each square in the 2D array passed. This grid printer allows
    for integers of up to 2 digits. The 2D array must be square or
    rectangular, as there is currently no error handling for 
    extraneous array elements. 

    Parameters
    ----------
    topo_grid : 2D arr/list of lists
        A 2d Python array of integers, square or rectangular
    """    
    for i in range(len(topo_grid)):
        print("|", end="")
        for j in range(len(topo_grid[0])):
            print(str(topo_grid[i][j]).rjust(2), end="|")
        print("")

def print_grid3d(cube_grid, include_coords = False):
    """
    Prints a pipe-separated table of integers representing a 3D grid as follows:
    0: air, 1: board, 2: water
    The 3D array must be a perfect cuboid / orthotope, as there is no error
    handling for extraneous array elements. 

    Parameters
    ----------
    topo_grid : 2D arr/list of lists
        A 2d Python array of integers, square or rectangular
    include_coords : bool, optional, default False
        Add 3D coordinates to each position in addition to the material
    
    """        
    length = len(cube_grid) 
    width = len(cube_grid[0])
    height = len(cube_grid[0][0])
    
    len_digits = len(str(length))-1
    wid_digits = len(str(width))-1
    ht_digits = len(str(height))-1
    
    print(f"Length {length}, Width {width}, Height {height}")
    for y in range(width):
        for x in range(length):
            print("", end="|")
            for z in range(height):
                if include_coords:
                    print("-".join([str(x).rjust(len_digits),
                        str(y).rjust(wid_digits),
                        str(z).rjust(ht_digits)]), end=":")
                print(cube_grid[x][y][z], end='|')
            print("", end=" ")
        print("")    
        
def print_cube_grid(cube_grid, include_coords = False):
    length = len(cube_grid) 
    width = len(cube_grid[0])
    height = len(cube_grid[0][0])
    
    len_digits = len(str(length))-1
    wid_digits = len(str(width))-1
    ht_digits = len(str(height))-1
    
    print(f"Length {length}, Width {width}, Height {height}")
    for y in range(width):
        for x in range(length):
            print("", end="|")
            for z in range(height):
                if include_coords:
                    print("-".join([str(x).rjust(len_digits),
                        str(y).rjust(wid_digits),
                        str(z).rjust(ht_digits)]), end=":")
                print(f"{cube_grid[x][y][z].content}", end='|')
            print("", end=" ")
        print("")

    
def simulate_flood(cube_matrix):
    
    ' first define flood level '
    flood_level = 0    
    
    length = len(cube_matrix)
    width = len(cube_matrix[0])
    height = len(cube_matrix[0][0])    
    
    'loop through each of x & y'
    for y in range(width):
        for x in range(length):
            print(f"1. Coords are {x},{y}")    

            'check if x,y is board or has water, then just ignore'
            # Must be air to bother with recursive function 
            if cube_matrix[x][y][flood_level].content == CONTENT_BOARD:
                print(f"1a. {x},{y} is a board, ignore.")
                print(f"1b. Also, {x},{y} drains? {cube_matrix[x][y][0].drains_out}")

            # If we already detected that the square drains, ignore
            elif cube_matrix[x][y][flood_level].drains_out:
                print(f"1c. Indeed, {x},{y} drains. Ignoring")
            # Check if it's the edge of the board. Ignore
            elif (0 in (x,y) or x == length-1 or y == width-1):
                print(f"1d. Edge of board, so ignore.")
                cube_matrix[x][y][flood_level].drains_out = True
            
            # Primary loop and recursion to check for air
            elif cube_matrix[x][y][flood_level].content == CONTENT_AIR:    
                print(f"2. Spreading out from {x},{y}")
            
                touched = [[False for i in range(width)] for j in range(length)]
                
                # Main recursive pathfinding loop. returns True if water drains, or False if it pools
                def crawl(x=x, y=y, drains_out=False, level=1):
                    paths = [(x,y-1), (x+1,y), (x,y+1), (x-1,y)]  # only 4 paths, diagonal walls are watertight. 
                    # Split into 4 crawls, clockwise starting at 12 o'clock (NESW)
                    tick = 0
                    for path in paths:
                        tick +=1
                        print(tick)
                        px, py = path[0], path[1]
                        
                        print(f"3. Pathfinding {px},{py} from {x},{y}, l={level}")
                        
                        if not ((0 <= px <= length-1) and (0 <= py <= width-1)):
                            print("Coords {px},{py} are out of bounds")
                            continue # Because we can't determine flooding or drainage yet
                        # Check for water or board and ignore 
                        elif cube_matrix[px][py][flood_level].content == (CONTENT_BOARD):
                            print(f"3a. Board at {px},{py}, ignoring.")
                            continue
                        elif cube_matrix[px][py][flood_level].content == (CONTENT_WATER):
                            print(f"3a. Water at {px},{py}, so flooding ")
                            cube_matrix[x][y][flood_level].content = CONTENT_WATER
                            continue
                        #Edge of board detection, if so we drain and mark it for drainage 
                        elif (0 in (px,py) or px == length-1 or py == width-1):
                            cube_matrix[x][y][flood_level].drains_out = True
                            cube_matrix[px][py][flood_level].drains_out = True
                            drains_out = True    
                            continue
                            
                        
                        # Otherwise we are inside the board with an air sqaure to resolve and recurse
                        else:
                            print(f"4. Found air at {px},{py}, starting recursion, l={level}")
                            if not touched[px][py] and level < 5:
                                touched[px][py] = True
                                drains_out = crawl(px, py, level+1)
                                print(f"4a. Did {px},{py} drain? {drains_out}, l={level}")
                                if drains_out: # Drains out
                                    print(f"4b. Yes {px},{py} drained, l={level}")
                                    cube_matrix[x][y][flood_level].drains_out = True 
                                    cube_matrix[px][py][flood_level].drains_out = True    
                                    return True
                    print(f"5. Testing for water at {x},{y}, l={level}")
                    if not cube_matrix[x][y][flood_level].drains_out: # Resolve as water
                        print(f"5a. Resolving water at {x},{y}! l={level}")
                        time.sleep(1)
                        cube_matrix[x][y][flood_level].content = CONTENT_WATER
                        return False
                crawl() 
    return cube_matrix
    
    '''
                    'if it is air, then ...'
                        'if it is at edge of board, you should detect drain. Drain out.
                        'if it is inside board, 
                            'then mark that we already touched this square'
                            'then recursively loop the pathfinder
                                '->recursion follows the same rules until it hits a drain. then drain and break'
                                '->if did not drain then congrats, the square is a water!'
             
                    
      '''          


def simulate_flood_old(cube_matrix):
    
    ''' now take a 2d slice at the flood level, and start flooding one square
    at a time '''
    
    length = len(cube_matrix)
    width = len(cube_matrix[0])
    height = len(cube_matrix[0][0])
    
    for flood_level in range(height):
        print(f"Flooding level {flood_level}")
        time.sleep(1)
        for y in range(width):
            for x in range(length):
                print(f"coords are {x},{y}")
                touched = [[False for i in range(width)] for j in range(length)]
                
                def crawl(cx=x, cy=y, drains_out = False):
                    # stary by touching current seed square
                    touched[cx][cy] = True
                    # Must be air to bother with recursive function 
                    if cube_matrix[cx][cy][flood_level].drains_out:
                        time.sleep(1)
                        print(f"Nice, we detected that {cx},{cy} drains out")
                    
                    content_below = CONTENT_BOARD
                    if flood_level > 0: 
                        content_below = cube_matrix[cx][cy][flood_level-1]
                    
                    if content_below == CONTENT_AIR: 
                        drains_out = True
                        cube_matrix[cx][cy][flood_level].drains_out = True
                        return True
                    
                    if cube_matrix[cx][cy][flood_level].content == CONTENT_AIR and not cube_matrix[cx][cy][flood_level].drains_out:
                        print(f"spreading out from {cx},{cy}")
                        paths = [(cx,cy-1), (cx+1,cy), (cx,cy+1), (cx-1,cy)]  # only 4 paths, diagonal walls are watertight. 
                        for path in paths:
                            px, py = path[0], path[1]
                            
                            content_below = CONTENT_BOARD
                            if flood_level > 0: 
                                content_below = cube_matrix[px][py][flood_level-1]
                            
                            if content_below == CONTENT_AIR: 
                                cube_matrix[px][py][flood_level].drains_out = True
                                return True
                                
                            if (0 <= px <= length-1) and (0 <= py <= width-1): 
                                if cube_matrix[px][py][flood_level].drains_out:
                                    print(f"Already detected that {px},{py} drains, so closing recursion and draining back to air")
                                    time.sleep(1)
                                    return True
                                
                                print(f"Crawling around at {px}, {py} / content {cube_matrix[px][py][flood_level].content}")
                                if cube_matrix[px][py][flood_level].content != CONTENT_BOARD and not touched[px][py] : 
                                    print("Found unresolved air")
                                    
                                    drains_out = crawl(px, py) 
                                    print(f"Does {px},{py} drain ? {drains_out}")
                                    if drains_out:
                                        cube_matrix[cx][cy][flood_level].drains_out = True 
                                        cube_matrix[px][py][flood_level].drains_out = True 
                                        return True
                                    
                                else: 
                                    print(f"No recursion for {px},{py} since content {cube_matrix[px][py][flood_level].content} and touched is {touched[px][py]}")                                
    
                            elif cube_matrix[cx][cy][flood_level].content == CONTENT_AIR: # drains off board at level
                                print(f"Draining out, {cx},{cy} doesnt hold wasser")
                                drains_out = True
                                cube_matrix[cx][cy][flood_level].drains_out = True
                                return True
                        
                        print(f"{cx},{cy} Drains out... {cube_matrix[cx][cy][0].drains_out} ")
                        if not cube_matrix[cx][cy][flood_level].drains_out:
                            print(f"Yay, making water")
                            #time.sleep(1)
                            cube_matrix[cx][cy][flood_level].content = CONTENT_WATER
                            cube_matrix[cx][cy][flood_level].resolved = True
                            return False                                
                    else:
                        return False    
             
                crawl()
    return cube_matrix
       
def simulate_flood_old2(cube_matrix):
    
    ' first define flood level '
    flood_level = 0
    
    ''' now take a 2d slice at the flood level + 1, and start flooding one square
    at a time '''
    
    length = len(cube_matrix)
    width = len(cube_matrix[0])
    
    for y in range(width):
        for x in range(length):
            print(f"coords are {x},{y}")
            
            def crawl(cx=x, cy=y):
                # stary by touching current seed square
                touched = [[False for i in range(width)] for j in range(length)]
                #touched[cx][cy] = True
                
                # Must be air to bother with recursive function 
                if cube_matrix[cx][cy][0].drains_out:
                    print(f"Nice, we detected that {cx},{cy} drains out")
                    print(f"Also, 1,1 drains? {cube_matrix[cx][cy][0].drains_out}")
                    time.sleep(1)
                    return True
                if cube_matrix[cx][cy][0].content == CONTENT_AIR:
                    print(f"spreading out from {cx},{cy}")
                    paths = [(cx-1,cy), (cx,cy-1), (cx+1,cy), (cx,cy+1)]  # only 4 paths, diagonal walls are watertight. 
                    
                    for path in paths:
                        
                        px, py = path[0], path[1]
                                                
                        if (0 <= px <= length-1) and (0 <= py <= width-1): 
                            touched[px][py] = True
                            if cube_matrix[px][py][0].drains_out:
                                cube_matrix[px][py][0].content = CONTENT_AIR
                                cube_matrix[cx][cy][0].content = CONTENT_AIR
                                cube_matrix[cx][cy][0].drains_out = True
                                print(f"Already detected that {px},{py} drains, so {cx},{cy} also drains. closing recursion & draining")
                                #time.sleep(1)
                                
                                return True
                            
                            print(f"Crawling around at {px}, {py} / content {cube_matrix[px][py][0].content}")
                            if cube_matrix[px][py][0].content != CONTENT_BOARD and not cube_matrix[px][py][0].drains_out and not touched[px][py] : 
                                
                                print("Found unresolved air")
                                
                                drains_out = crawl(px, py) 
                                                              
                                print(f"Does {px},{py} drain ? {drains_out}")
                                if drains_out:
                                    cube_matrix[cx][cy][0].drains_out = True 
                                    cube_matrix[px][py][0].drains_out = True 
                                    return True
      
                            else: 
                                
                                print(f"No recursion for {px},{py} since content {cube_matrix[px][py][0].content} and touched is {touched[px][py]}") 
                              

                        elif cube_matrix[cx][cy][0].content == CONTENT_AIR: # edge of board, so drains off board at level
                            print(f"Draining out at edge of board, {cx},{cy} doesnt hold wasser")
                            cube_matrix[cx][cy][0].drains_out = True
                            
                            return True
                    
                    print(f"{cx},{cy} Drains out... {cube_matrix[cx][cy][0].drains_out} ")
                    if not cube_matrix[cx][cy][0].drains_out:
                        print(f"Yay, making water")
                        #time.sleep(1)
                        cube_matrix[cx][cy][0].content = CONTENT_WATER
                        cube_matrix[cx][cy][0].resolved = True
                        return False                                
                else:
                    return False    
         
            crawl()
            
        print(cube_matrix[1][1][0].drains_out)
    return cube_matrix
       
if __name__ == '__main__':
    (topo_grid, board_max_height) = prepare_grid(length=args.grid_length, 
        width=args.grid_width, max_height=args.max_height)   
    print_grid(topo_grid)
    print(board_max_height)