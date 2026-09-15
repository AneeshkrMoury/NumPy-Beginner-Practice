# iteration in numpy array
'''
x = [9,8,7,6,5,4]
now i have to itrate this array means getting each element indvidually one by one we use loop for that 

for i in x:
   print(i) -> output will be 

9
8
7
6
5
4
'''
import numpy as np

#1D array iteration 
x = np.array([4,5,6,1,2,3])
print(x)
for i in x :
    print(i)


#2D array

x1 = np.array([[4,5,6,1,2,3],[8,7,9,6,5,4]])
print(x1)
for j in x1:
    print(j) # give both row 

# output : 
[4,5,6,1,2,3]
[8,7,9,6,5,4]

#to get element we will be require to use another loop that will access the row element 

for j in x1:
    for k in j:
        print(k)


#3D
x3 = np.array([[[4,5,6,1,2,3],[8,7,9,6,5,4]]])
print(x3)

for i in x3:
    for j in i:
        for k in j:
            print(k)


'''
Function for looping:

nditer() is a function that we can use inplace of using for loop multiple times 
'''
x3 = np.array([[[4,5,6,1,2,3],[8,7,9,6,5,4]]])
print(x3)
for i in np.nditer(x3):
    print(i)

for i in np.nditer(x3, flags=['buffered'],op_dtypes="S"): #changing output type 
    print(i)


'''
Function to do iteration with indexting:

np.ndenumerate(array)
return  data and index 
'''
for i,d in np.ndenumerate(x3): #changing output type 
    print(i,d)

'''
Output
(0, 0, 0) 4
(0, 0, 1) 5
(0, 0, 2) 6
(0, 0, 3) 1
(0, 0, 4) 2
(0, 0, 5) 3
(0, 1, 0) 8
(0, 1, 1) 7
(0, 1, 2) 9
(0, 1, 3) 6
(0, 1, 4) 5
(0, 1, 5) 4
'''
