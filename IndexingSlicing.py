#Indexing and Slicing 
'''
1D Array

[1 2 3 4]
 0 1 2 3 -> indexting positive
-4-3-2-1 -> negative 
'''

'''
2D array
                row
[ [ 1  2 ]    ->  0 
  [ 1  2 ] ]  ->  1
    |  |
col 0  1
'''

'''
3D Array
                 index if row of 2d block inside 3d 
[ [ [ 1  2 ]      0        first the block of 2d indexing in 3d
    [ 1  2 ] ]    1         -> 0
  [ [ 1  2 ]      0
    [ 1  2 ] ] ]  1         -> 1
      |  |
      0  1    column index 

'''

import numpy as np

#1D
x = np.array([4,5,6,7])
print(x[0]) # -> getting specific index of element op: 4
print(x[-4]) # op : 4


#2D
y = np.array([[1,2,3],[8,5,2]])
print(y)
print(y.ndim)
print()
print(y[1][2]) # first pass row number/address ; then enter number of coloumn in the row

#3D

y = np.array([[[1,2,3],[78,15,22]],[[7,6,9],[8,5,2]]])
print(y)
print()
print(y.ndim)
print(y[1][0][2])

'''
Slicing 

x [1,2,3,4,5] getting a prat of array is slicing like here we want from 2-4 part then its clicing 
i  0 1 2 3 4 

x[start:stop:step] 
'''

#1D
z = np.array([78,15,22,89,4,56,27])
print(z)
print(z[1:5:1])
print(z[1:])
print(z[::-1])
print(z[::2])


#2D
'''
2D array
                row
[ [ 1  2 ]    ->  0 
  [ 1  2 ] ]  ->  1
    0  1  -> coloumn number

x[row_number , starting_coloumn , ending_coumn , steps]
'''

var = np.array([[1,2,3,9,7,8,5,78],[8,5,2,45,52,66,24,87]])
print(var[1,2:6])
print(var[0,2:6])
