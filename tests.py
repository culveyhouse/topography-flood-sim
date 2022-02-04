#!/usr/bin/env Python

import unittest
import topographyfloodsim

class Test1(unittest.TestCase):
    
    def average(self, nums):
        return sum(nums)/len(nums)
    
    def test_average(self):
        self.assertEqual(self.average([20, 30, 70]), 41.0)
        self.assertEqual(round(self.average([1, 5, 7]), 1), 4.3)
        with self.assertRaises(ZeroDivisionError):
            self.average([])
        with self.assertRaises(TypeError):
            self.average(20, 30, 70)

class Test2(unittest.TestCase):
    
    def average(self, nums):
        return sum(nums)/len(nums)
    
    def test_average(self):
        self.assertEqual(self.average([20, 30, 70]), 40.0)
        self.assertEqual(round(self.average([1, 5, 7]), 1), 4.3)
        with self.assertRaises(ZeroDivisionError):
            self.average([])
        with self.assertRaises(TypeError):
            self.average(20, 30, 70)

class Chessboards(unittest.TestCase):
        
    def full_containment(self):
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
        groomed_grid, max_height = topographyfloodsim.prepare_grid(topo_grid=chessboard)
        cargrid = topographyfloodsim.MakeCartesianGrid(groomed_grid, max_height)
        result = topographyfloodsim.simulate_flood(cargrid.cubes)
        total = topographyfloodsim.flood_statistics(result, request='total')
        self.assertEqual(total, 108)
        
        
unittest.main()  # Calling from the command