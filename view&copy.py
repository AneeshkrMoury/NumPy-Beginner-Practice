#Copy vs view function in NumPy array

import numpy as np

x = np.array([1,2,3,4])


co = x.copy()



print(f"x : {x}")
print(f"copy : {co}")



vi = x.view()

print(f"view : {vi}")

'''
Both are used to copy the data
BASIC DIFFERENCE IN BOTH 
COPY                                   VIEW
ouns the data                          does not own the data
a copy is a new array                  view the original array
change does not reflect in original    change will afect in original
'''
