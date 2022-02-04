#!/usr/bin/env Python

import unittest
from topographyfloodsim import full_simulation  

class Test1(unittest.TestCase):

    def test_small_draining_grid(self):
        chessboard = [  
            [0,1,1,7],
            [3,0,1,2],
            [2,0,0,2],
            [4,0,3,1]
        ]
        total_flooding, max_water_level = full_simulation(chessboard)
        self.assertEqual(total_flooding, 0)
           
    def test_full_containment(self):
        chessboard = [  
            [0,8,8,7,7,4,4,4],
            [8,0,0,0,0,0,0,3],
            [8,0,0,0,0,0,0,3],
            [4,0,0,0,0,0,0,4],
            [4,0,0,0,0,0,0,3],
            [4,0,0,0,0,0,0,4],
            [4,0,0,0,0,0,0,3],
            [4,6,6,6,4,4,4,4],
        ]
        total_flooding, max_water_level = full_simulation(chessboard)
        self.assertEqual(total_flooding, 108)

    def test_draining_maze(self):
        chessboard = [  
            [0,8,8,7,7,4,4,4],
            [8,0,0,0,3,0,0,3],
            [8,1,3,0,3,3,3,3],
            [4,1,3,0,0,0,0,4],
            [4,1,3,2,2,2,0,3],
            [4,2,3,0,0,1,0,4],
            [4,2,3,0,0,0,0,3],
            [4,6,6,0,4,4,2,4],
        ]
        total_flooding, max_water_level = full_simulation(chessboard)
        self.assertEqual(total_flooding, 6)
        
    def test_tiered_waterfall(self):
        chessboard = [  
            [0,9,9,9,9,9,9,0],
            [9,5,8,7,7,6,5,9],
            [0,9,9,9,9,9,6,9],
            [0,3,3,3,9,9,4,9],
            [0,3,3,9,9,9,4,9],
            [2,1,1,1,3,2,4,9],
            [2,1,2,2,2,2,4,9],
            [2,2,2,0,4,4,4,4],
        ]
        total_flooding, max_water_level = full_simulation(chessboard)
        self.assertEqual(total_flooding, 8)    
    
unittest.main()  # Calling from the command