#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 16:57:18 2018

@author: changhengchen
"""

"""Array elements"""

import numpy as np

def test_run():
    a = np.random.rand(5,4)
    print("Array:\n", a)
    
    """(1) Acess array elements"""
    # Accessing element at position (3,2)
    element = a[3,2]
    print(element)
    
    # Elements in defined range
    print(a[0,1:2])
    
    # Top left corner
    print(a[0:2, 0:2])
    
    # Slicing
    # Note: Slice n:m:t specifies a range that starts at n, and stops before m, interval of t
    print(a[:,0:3:2]) # will select columns 0, 2 for every row
    print(a[-2:,2])   # will select row -2 till end of all columns with index 2
    
    
    """(2) Modify array elements"""
    # Assigning a value to a particular location
    a[0, 0] = 1
    print("\nModified (replaced one element):\n", a)
    
    # Assigning a value to an entire row
    a[0, :] = 2
    print("\nModified (replaced a row with a single value):\n", a)
    
    # Assigning a list to a column in an array
    a[:, 3] = [1, 2, 3, 4, 5]
    print("\nModified (replaced a column with a list):\n", a)
    
    
    """(3) Index an array with another array"""
    b = np.random.rand(5)
    print("Array:\n", b)
    
    # Accessing using list of indices
    indices = np.array([1,1,2,3])
    print(b[indices])
    
    
    """(4) Boolean arrays"""
    c = np.array([(20,25,10,23,26,32,10,5,0),(0,2,50,20,0,1,28,5,0)])
    print("Array:\n", c)
    
    # calculate the mean
    mean = c.mean()
    print("Array mean:", mean)
    
    # masking
    c[c<mean] = mean
    print(c)
    
    
    """(5) Arithmetic operations"""
    d = np.array([(1,2,3,4,5),(10,20,30,40,50)])
    print("\nOriginal array d:\n", d)
    
    # Multiply d by 2
    print("\nMultiply d by 2:\n", 2*d)
    
    # Divide d by 2
    print("\nDivide d by 2:\n", d/2)
    
    e = np.array([(100,200,300,400,500),(1,2,3,4,5)])
    print("\nOriginal array e:\n", e)
    
    # Add the two arrays
    print("\nAdd d+e:\n", d+e)
    
    # Multiply d and e element-wise
    print("\nMultiply d and e:\n", d*e)
    
    # Divide d by e element-wise
    print("\nDivide d by e:\n", d/e)
    
    

if __name__ == "__main__":
    test_run()