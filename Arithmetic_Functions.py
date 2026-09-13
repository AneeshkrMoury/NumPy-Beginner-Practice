#Arithmetic Functions 
'''
np.min(x)
np.max(x)
np.argmin(x)
np.sqrt(x)
np.sin(x)
np.cos(x)
np.cumsum(x)
'''

import numpy as np

obj = np.array([1,2,3,4,5])
print(f"Min: {np.min(obj)}, Position : {np.argmin(obj)}")
print(f"Max: {np.max(obj)}, Position : {np.argmax(obj)}")



var = np.array([[4,6,15],[7,11,9]])
in 2 d array we have 2 axis 0 & 1; 0-> COLOUM, 1 FOR ROW
print(f"Minimum: {np.min(var, 0)}")

print(f"Sqrt: {np.sqrt(var)}")

var2 = np.array([1,2,3])
print(f"Sqrt: {np.sin(var2)}")
print(f"Sqrt: {np.cos(var2)}")


#cumultive sum
'''
array => [1,2,3], cumsum = [1,3,6]
'''
print(f"Sqrt: {np.cumsum(var2)}")
print(f"Sqrt: {np.cumprod(var2)}")
