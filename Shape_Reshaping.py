#Shape and Reshaping in NumPy Arrays
'''
[[1,2],  
 [1,2]] 
2D array we we can find its shape , and covert it into different shapes we goona learn about this in this 
'''

import numpy as np

#shape 
var = np.array([[1,2,3],[4,5,6]])

# how can we show its row and coloum
print(var)
print()
print(np.shape(var)); print(var.shape) #both are valid


var1 = np.array([1,2,3,4], ndmin=4) # we use ndmin to make multi dimension array
print(var1)
print(var1.shape)


#reshaping array.reshape(x , y) ; x-> rows , y-> coloumn for 2d array
var3 = np.array(([1,2,3,4,5,6]))
x = var3.reshape(3,2)
print(x)
print(x.ndim) # ndim to cehck number of dimension


# if want to convert in 3 dimesion 
'''
Visualizing reshape(2, 3, 2)
When we run var4.reshape(2, 3, 2), you are telling NumPy to arrange your elements into a 3D block built like this:
2 (Layers / Depth): How many separate 2D grids you want.
3 (Rows): How many horizontal rows are inside each grid.
2 (Columns): How many vertical columns are inside each

'''
var4 = np.array(([1,2,3,4,5,6,7,8,9,10,11,12]))
x1 = var4.reshape(2,3,2)
print(x1)
print(x1.ndim)


#going back to 1d from 2d we can use -1 to go back on 1d 

print()
one = x1.reshape(-1)
print(one)
print(one.ndim)
