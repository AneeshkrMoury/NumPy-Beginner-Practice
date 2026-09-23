# NumPy Beginner Practice Set
'''
Level 1: Warm-up
Q1. Array Creation
Create a NumPy array containing the numbers 10, 20, 30, 40, 50. Print: the array its type its number of dimensions its
shape its size
'''
import numpy as np
var = np.array([10, 20, 30, 40, 50])
print(var)
print(type(var))
print(np.ndim(var))
print(np.shape(var))
print(var.size)

'''
Q2. Different Data Types
Create [10, 20, 30, 40] as: an integer NumPy arraya float NumPy array Print their dtype.
'''
a = np.array([10, 20, 30, 40], dtype=int)
print(a)
print(type(a))
print(a.dtype)
b = np.array([10, 20, 30, 40], dtype=float)
print(b)
print(type(b))
print(b.dtype) # we use array.dtype to check element type in an array 

'''
Q3. arange() Practice
Create an array containing numbers from 1 to 20 using np.arange(). Then create: 5, 10, 15, 20, ..., 50.
'''
c=np.arange(1,20)
print(c)
print(np.arange(5,51,5)) # we use arange like for loop here np.arange(starting_value, stoping_value, steps )

'''
Q4. linspace() Practice
Generate exactly 10 equally spaced numbers between 0 and 1.
'''
d = np.linspace(0,1, 5) # so line space kind give us the desired number of value with same interval like here (0,1,5) 0 and 1 are range from we want value and 5 is the number of value we want 
print(d)

'''
Q5. Zeros and Ones
Create: a 1-D array of five zeros a 1-D array of five ones a 3 × 3 array of zeros a 2 × 4 array of ones
'''
x = np.zeros(5)
print()
print(x)
print(np.ones(5))
print()

print(np.zeros((3,3))) # we pass the row and colomn in touple formate 
print()
print(np.ones((2,4)))


'''
Level 2: Indexing & Slicing
Q6. Basic Indexing
Given
arr = np.array([10, 20, 30, 40, 50, 60])
Print the first element, last element, third element, and second-last element.
'''
import numpy as np
arr = np.array([10, 20, 30, 40, 50, 60])
print(arr[0])  #first element 
print(arr[-1]) # we can use it to start from last index easy when we never know what is the number of element 
print(arr[2])  # third element 
print(arr[-2]) # second last element 

'''
Q7. Slicing
Using the same array, extract the first 3 elements, last 3 elements, elements from index 1 to 4, and every second
element.
'''
#using the same arrya we have in 6th 
print(arr[0:3:1]) # 0 is first positon to start and 3 is the postion to stop and 1 is like step to take if every element if 2 every second element will be picked 
print(arr[-1:2:-1]) # ok so here first -1 is like we telling to start from -1 and  2 numper to tiem to walk or limit to stop so first 0 then 1 then 2 after this it stops 
print(arr[1:5:1]) # in positive indexing we have to give one more then till we looking to get
print(arr[::2]) # it tells that to print every second value and start and stop are default O and last point

'''
Q8. Reverse an Array
Reverse arr = np.array([1, 2, 3, 4, 5, 6, 7]) using slicing.
'''
arr1 = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr1[::-1]) # its super easy we just make steps to move in negative like -5 , -4, -3 so on

'''
Q9. 2-D Indexing
Given a 3 × 3 array containing 10,20,30 / 40,50,60 / 70,80,90, find 50, 90, 20, the entire second row, and the entire
third column.
'''
arr2 = np.array([[10,20,30],[40,50,60],[70,80,90]])
print(arr2)
print()
print(np.where(arr2 == 50)) # its like our sql command where we like saying give index where in arr2 == 50
print(np.where(arr2 == 90)) 
print(np.where(arr2 == 20)) 
print()
print(arr2[1,::]) # here 1 is row number and :: says to print all row 
print(arr2[(0,1,2),2::3]) # so here we have give all row (0,1,2)  and then telling to start at index 2 and steps will be 3 print every 3rd value  
'''
Q10. 2-D Slicing
From the same array, extract:
10 20
40 50
Then extract:
50 60
80 90.
'''
print(arr2[(0,1),0:2:]) # here we telling row and extract first 2 value 
print(arr2[(1,2),1::])  # here we are starting at first so we skip the 0 index value as we have to only print after that to get second 2d output 


'''
Level 3: Array Operations
Q11. Element-wise Arithmetic
Given a=[10,20,30,40] and b=[1,2,3,4], perform addition, subtraction, multiplication, and division without a Python
loop.
'''
import numpy as np 

a = np.array([10,20,30,40])
b = np.array([1,2,3,4])

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(np.multiply(a , b))

'''
Q12. Scalar Operations
Given arr=[5,10,15,20], create arrays representing every value +10, -5, ×2, and ÷5.
'''
c = np.array([5,10,15,20])
print(c + 10)
print(c - 5)
print(c * 2)
print(c / 5)

'''
Q13. Comparison Operations
Given arr=[10,25,5,40,15,30], evaluate arr > 20, arr < 15, and arr == 25. Let NumPy perform the comparisons.
'''
d = np.array([10,25,5,40,15,30])
print(np.greater(d, 20))
print(d > 20) # both can be used to evaluate 
print(d < 20)
print(d == 25)
'''
Q14. Basic Statistics
For marks=[78,65,89,92,55,73,81], find minimum, maximum, average, and sum.
'''
e = np.array([78,65,89,92,55,73,81])
print(np.min(e))
print(np.max(e))
print(np.average(e))
print(np.sum(e))

'''
Q15. Position of Min/Max
For arr=[45,12,78,23,91,34], find the minimum value, maximum value, index of minimum, and index of maximum.
Practice argmin()/argmax().
'''
f = np.array([45,12,78,23,91,34])
print(np.min(f))
print(np.max(f))
print(np.min_index(f)) #i can not remember the function name we used to get the index of minimum or even there is function do to direclty lets first make this up by ourself

min_v = np.min(f)
print(np.where(f == min_v)) #  i was using only one equals but we have to use == for in where for comparison 
max_v = np.max(f)
print(np.where(f == max_v))

print(np.argmin(f)) # ok so we can use arg to get index value of max and min its a build in function 
print(np.argmax(f))




