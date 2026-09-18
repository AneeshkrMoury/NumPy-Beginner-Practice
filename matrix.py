#Matrix in numpy array

'''
Matrix 
 __   __
| 1 2 3 |                  [ [ 1 2 3 ]
| 4 5 6 | --> can be this    [ 4 5 6 ]
| 7 8 9 |                    [ 7 8 9 ] ]
|__   __| 

aaray and matrix are very similer both are defind as row and coloum 
matrix are readed as (no of row * no of coloumn), basic differenc in numpy array and matric can be shown in muliplication of matrix 

in product of array -> data multiply one by one 
in matrxi -> we do dot product 
'''

#creating matric np.matrix()

import numpy as np

var = np.matrix([[1,2,3],[1,2,3]])
print(var)
print(type(var))
print()


var1 = np.array([[1,2,3],[1,2,3]])
print(var1)
print(type(var1))
print()

#addition in both matrix and array is same and subtration is same as well
#product is different in both array and matrix as matrix use dot product 
var1 = np.array([[1,2,3],[1,2,3]])
print(var)
print()
print(var1)
print()
print(var + var1)
print()

var = np.matrix([[1,2],[1,2]])
var1 = np.array([[1,2],[1,2]])
print(var)
print()
print(var1)
print()
print(var * var1)
print()

'''
1 2  *  1 2  ->  1*1 + 2*3  2*1 + 4*2  ->  7  10
3 4     3 4      3*1 + 4*3  3*2 + 4*4      15 22

this multiplication is called as dot product  we use dot function to perform this product 
'''

print(var.dot(var1))

'''
Function in matrix 
'''

'''
Transpose: np.transpose(array), array.T 'sortcut'

1 2  A^T = 1 3 5    --> covert row into coloumn and column into row
3 4        2 4 6        3*2 -> 2*3
5 6
'''
mt = np.matrix([[1,2,3],[4,5,6]])
print(mt)
print()
print(np.transpose(mt))


'''
swapaxes: similar to transpose convert row into coloumn and coloumn into row ; np.swapaxes(array , axis1, axis2)
'''
print()
print(np.swapaxes(mt, 0,1))

'''
inverse: represt as A power -1 
Function => np.linalg.inv(matrix)

1 2  -> A^-1  ->  1 / (1*4 - 3*2)  ->  4  -2
3 4                                    3   1

                  1 / -2               4  -2
                                      -3   1
 
'''

var3 = np.matrix([[1,2],[3,4]])
print(var3)
print()
print(np.linalg.inv(var3))


'''
power : like making power of matrix a => a^2
function-> np.linalg.Matrix_power(matrix, n) #n represetn value of power any value 
n  > 0
n  = 0
n  < 0

n = 0 :  we get identity matrix dignoal element will be 1 and other will be 0

n > 0 : power applied and multiplication performed 

n < 0 : inverse * power
'''
var4 = np.matrix([[1,2],[3,4]])
print(var4)
print()
print(np.linalg.matrix_power(var4 , 2))
print()
print(np.linalg.matrix_power(var4 , 0))
print()
print(np.linalg.matrix_power(var4 , -2))
print()


'''
determinate
3*3 matrix

a b c  
d e f  -> | A | -> a  [ei - hf] - b [di - gf] + c [dh - eg]
g h i

np.linalg.det()
'''

var6 = np.matrix([[1,2],[3,4]])
print(var6)
print()
print(np.linalg.det(var6))


var6 = np.matrix([[1,2,3],[3,4,3],[1,2,3]])
print(var6)
print()
print(np.linalg.det(var6))
