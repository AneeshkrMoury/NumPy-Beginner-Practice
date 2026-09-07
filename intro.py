#numpy => consumes less memory, faster then list , easy to use , for wide mathmatial operat , built function , sorting, basic algebra , ml

import numpy as np

a = np.array([1,2,3,4])
# print(a)
# print(type(a))

y = [1,2,3,4]
# print(y)
# print(type(y))


#creating array using numpy

#-> we use np.array() its basic function for 
a = np.array([1,2,3])
# print(a)

# coverting a list in to array 
b = np.array(y)
# print(type(b))

# l = []
# for i in range(1,5):
#     value = int(input("Enter number:"))
#     l.append(value)

# print(np.array(l))

'''
types of array 
1D -> [1,2,3,4]
2D -> [[1,2,3,4]]
3D -> [[[1,2,3,4]]]
Higher Dimensional Array 
we can use "np.ndim() or array_name.ndim" function to check dimenssion of an array 
'''
# 1D array
x = np.array([1,2,3,4])
# print(x.ndim)
# print(np.ndim(x))


#2D array # number of colum should be same in each row 
a2 = np.array([[1,2,3,4],[5,6,7,8]])
print(a2)
print(a2.ndim)

#3D  array
a3 = np.array([[[1,2,3,4],[5,6,7,8],[4,8,7,9]]])
print(a3)
print(a3.ndim)


#N Dimenssion array
an = np.array([1,2,3,4], ndmin=10) # we can use ndim to tell how many dimenssion array should be 
# print(an)
# print(an.ndim)