#numpy array function 
'''
search array -> searching an array for a certain value and return the indexes that get a match 

use -> np.where(array == value) function
'''
import numpy as np

x = np.array([7,8,9,10,7,9,11,10])

res = np.where(x == 9)
even = np.where((x % 2) == 0)
print(res)
print(even)

'''
Search sorted array : it perform binary search in the array and returns the index where the specified value would be inserted to maintain the search order 

Function -> np.searchsorted(array, value) # giev the position where it can fit from left to right
'''
x = np.array([7,8,9,10,11,14])

res2 = np.searchsorted(x, [12,13,15])
print(res2)

'''
Sort Array : to make anumber or character appear in an order asc or desc
Function -> np.sort(array)
'''

var = np.array([7,8,4,9,11,10])
res3 = np.sort(var)
print(res3)

d = np.array([[7,8,4,9,11,10],[78,12,35,4,5,10]])
print(np.sort(d))

'''
filter : getting some element out of an existing array and creating a new array out of them
'''

var = np.array([7,8,4,9])
f = [True,False,False,True]
r = var[f]
print(r)
