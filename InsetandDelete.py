#Insert and Delete in numpy array 

import numpy as np 

x = np.array([1,2,3,4,5])

print(x)
print(type(x))

'''
Inserting data in array : use insert function to enter add new value in a array 

np.insert(array, position , value)
'''
v = np.insert(x , 2, 4)
print(v)

'''
we can insert a value at multiple position by passing position in tuple 
'''
a = np.insert(x, (2,4,5), 9)
print(a)


'''
It does not accepect float value consider itneger value 
'''
b = np.insert(x, (2,4,5), 9.5)
print(b)


# 2D we can inset along axis 1-> y -> 1 , x -> 0 ; we can insert multiple value by passing in list 
var = np.array([[5,6,7],[1,2,3]])
print(var)
print()
var1 = np.insert(var, 2, 6, axis = 0)
print(var1)
print()
var2 = np.insert(var, 2, [22,23], axis = 1)
print(var2)


'''
Same as list we have append function in numpy array it add value at the end of array 
'''

obj = np.append(x, 6.5)
print(obj)
obj1 = np.append(var, [[61, 45 , 23]], axis=0)
print(obj1)

'''
Delete to remova a sertain value from array 
function-> np.delete(array, index_number)
'''
obj = np.delete(x, 2)
print(x)
print(obj)

obj2 = np.delete(var,1, axis=0)
print(var)
print()
print(obj2)
