#! /usr/bin/env python
from utils import *

def cross(a,b):
  return [x+y for x in a for y in b]
  

def grid_lines(grid):
  return dict(zip(cross(rows,cols),grid))
  
def __init__ == __main__:
  rows = 'ABCDEFGHI'
  cols = '123456789'
  boxes = cross(rows,cols)  