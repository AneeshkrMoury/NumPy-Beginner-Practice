#Broadcasting in Array

import numpy as np


#When we see Broadcasting 
var1 =np.array([1,2,3,4])
var2 =np.array([1,2,3])
print(var1 + var2) # thorw an error could not be broadcast due to different size of arraly element 
'''
(1,4) (1, 3) from right side there should be atleast one 1 but there are 4, 3 thus it throw broad cast error
'''

'''
[1,2,3] # 1 * 3
[ 1
  2
  2 ] # 3 * 1
#dimension should be same
#should have 1 in one atleast from right (1 * 3) (3 * 1)
#new array will be that max of both (3 * 3)
'''
var3 =np.array([1, 2, 3])
print(np.shape(var3))
print(var3)
print()
var4 = np.array([[1],[2],[3]])
print(np.shape(var4))
print(var4)
print()
print(var3 + var4)



x = np.array([[1],[5]])
print(x.shape)
x1 = np.array([[1,2,3],[1,2,3]])
print(x1.shape)
print(x + x1)
