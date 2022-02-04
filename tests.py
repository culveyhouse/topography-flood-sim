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

class Test3(unittest.TestCase):
        
    def test_average(self):
        pass
        
        
unittest.main()  # Calling from the command