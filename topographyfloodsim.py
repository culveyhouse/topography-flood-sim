#!/usr/bin/env python

import sys
import argparse

DEFAULT_X = 8
DEFAULT_Y = 8

parser = argparse.ArgumentParser(description='Just an argparse test.')
parser.add_argument('length', metavar='grid length', type=int, nargs='?', default=DEFAULT_X,
                    help='length of topography grid')
parser.add_argument('width', metavar='grid width', type=int, nargs='?', default=DEFAULT_Y, 
                    help='width of topography grid')
parser.add_argument('--area', dest='area', action='store_true',
                    help='sum the integers')
                    
args = parser.parse_args() 
if args.area:
    calc_area = args.length * args.width
    print(f"The area of the grid is {calc_area}.")
    