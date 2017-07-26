#! /usr/bin/env python
from utils import *

def cross(a,b):
  return [x+y for x in a for y in b]
  

def grid_lines(grid):
      """Convert grid string into {<box>: <value>} dict with '123456789' value for empties.

    Args:
        grid: Sudoku grid in string form, 81 characters long
    Returns:
        Sudoku grid in dictionary form:
        - keys: Box labels, e.g. 'A1'
        - values: Value in corresponding box, e.g. '8', or '123456789' if it is empty.
    """
    Lgrid = list(grid)
    Lgrid = [a if a != '.' else '123456789' for a in Lgrid]
    
  return dict(zip(cross(rows,cols),Lgrid))
  
def __init__ == __main__:
  rows = 'ABCDEFGHI'
  cols = '123456789'
  boxes = cross(rows,cols)  
