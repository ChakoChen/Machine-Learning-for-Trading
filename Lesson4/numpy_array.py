#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 15:37:07 2018

@author: changhengchen
"""

import numpy as np

def get_max_index(a):
    """Return the index of the maximum value in given 1D array."""
    return a.argmax()

def test_run():
    """Creating NumPy arrays"""
    # List to 1D array
    print(np.array([2, 3, 4]))
    
    # List of tuples to 2D array
    print(np.array([(2, 3, 4), (5, 6, 7)]))
    
    # Empty array, not actually empty, but random values
    print(np.empty(5))     #1D
    print(np.empty((5,4))) #2D
    
    # Array of 1s
    print( np.ones((5, 4), dtype=np.int_) )
    
    
    """Generate random numbers"""
    # Generate an array full of random numbers, uniformly sampled from [0.0, 1.0)
    print( np.random.random((5, 4)) ) # pass in a size tuple
    print( np.random.rand(5, 4) )     # same, function arguments (not a tuple)
    
    # Sample from a Gaussian (normal) distribution
    print(np.random.normal(size=(2, 3)))         # "standard normal" (mean = 0, s.d. = 1)
    print(np.random.normal(50, 10, size=(2, 3))) # change mean to 50 and s.d. to 10 


    # Random integers
    print(np.random.randint(10)) # a single integer in [0, 10)
    print(np.random.randint(0, 10)) # same as above, specifying [low, high) explicit
    print(np.random.randint(0, 10, size=5)) # 5 random integers as a 1D array
    print(np.random.randint(0, 10, size=(2, 3))) # 2x3 array of random integers
    

    """Array attributes."""
    a = np.random.random((5,4)) # 5x4 array of random numbers
    print(a)
    print(a.shape)
    print(a.shape[0])   # number of rows
    print(a.shape[1])   # number of columns
    print(len(a.shape)) # number of dimensions
    print(a.size)       # number of elements
    print(a.dtype)      # data type of the values
    
    """Operations on arrays"""
    np.random.seed(693) # seed the random number generator
    a = np.random.randint(0, 10, size=(5, 4)) # 5x4 random integers in [0, 10)
    print("Array:\n", a) # will generate same numbers for every run
    
    # Sum of all elements
    print("Sum of all elements:", a.sum())
    # Iterate over rows to compute sum of each column
    print("Sum of each column:\n", a.sum(axis=0))
    # Iterate over columns to compute sum of each row
    print("Sum of each row:\n", a.sum(axis=1))
    
    # Statistics: min, max, mean (across rows, cols, and overall)
    print("Minimum of each column:\n", a.min(axis=0))
    print("Maximum of each row:\n", a.max(axis=1))
    print("Mean of all elements:", a.mean()) # leave out axis
    
    b = np.array([9, 6, 2, 3, 12, 14, 7, 10], dtype=np.int32) # 32-bit integer array
    print("Maximum value of b:", b.max())
    print("Index of max:", get_max_index(b))
    
if __name__ == "__main__":
    test_run()