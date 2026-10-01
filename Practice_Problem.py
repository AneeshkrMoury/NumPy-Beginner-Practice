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

'''
Level 4: Shape & Reshaping
Q16. Reshape
Create arr=np.arange(1,13) and reshape it into a 3 × 4 array.
'''
import numpy as np
arr = np.arange(1,13) # there is something we use to tell the dimenson of array something like ndhim let me look for it i not able to remember it right now sorry ohh we can simply use reshape function for this lets try it out 
a = arr.reshape(3,4)
print(a) # yep .reshape for changing the shape 
print(a.ndim) # ndhim use the find the dimension of array
print(a.shape) # to check the shape of an array
'''
Q17. Different Shapes
Take arr=np.arange(1,13) and reshape it into 2×6, 3×4, 4×3, and 6×2. Print the shape after each operation.
'''
arr=np.arange(1,13)
a1 = arr.reshape(2,6)
print(np.shape(a1))
a2 = arr.reshape(3,4)
print(np.shape(a2))
a3 = arr.reshape(4,3)
print(np.shape(a3))
a4 = arr.reshape(6,2)
print(np.shape(a4))


'''
Q18. Shape Detective
For arr=[[1,2,3],[4,5,6]], predict ndim, shape, and size before running the code. Then verify.

Ans -> ndim = 2,  shape = 2 * 3 (2row, 3column), size = 6
'''
arr=np.array([[1,2,3],[4,5,6]])
print(f"{arr.ndim}\n{arr.shape}\n{arr.size}")

'''
Q19. Flattening
Convert the 3 × 3 array 1 through 9 into a 1-D array using a NumPy method you have learned.
'''
#i do not remeber the exact method i usd during learning session for flattening but lets try if can do it 
arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(f"{arr}\n{arr.shape}")
flaten = arr.flatten("A") # i can recall something about learning about few things like this lets me check form my learning material 
print(flaten)
#F flatten with coloum vise vertically
#C defaul in sequence first row seoncd then third row 
#A IN CONTINEOUS FORM 


'''Q20. Reshape Challenge
Create numbers 1 through 24 and reshape them into 4×6, then 3×8.'''

arr = np.arange(1,25)
a = arr.reshape(4,6)
b = arr.reshape(3,8)
print(f"{a}\n\n{b}")


'''
Level 5: Insert, Delete & Manipulation
Q21. Insert an Element
Given arr=[10,20,30,40], insert 25 between 20 and 30. Expected: [10 20 25 30 40].
'''
import numpy as np
arr = np.array([10,20,30,40])
arr = np.insert(arr,2,25) # pass array naem , postion where to insert and value to insert
print(arr)


'''Q22. Delete an Element
Given arr=[10,20,30,40,50], delete 30 and then delete the last element.
'''
arr = np.array([10,20,30,40,50])
arr = np.delete(arr, 2) # pass the array and position of item to delete 
print(arr)

'''Q23. Insert into 2-D Array
Given [[1,2],[3,4]], insert another row [5,6] so the result is [[1,2],[3,4],[5,6]].
'''
arr = np.array([[1,2],[3,4]])
# arr = np.insert(arr,[2][0],(5,6)) # so not getting right way to insert in 2d arrya let me think other ways
arr1 = np.append(arr, [[5],[6]], axis=1) # axis 1 add value in y axis like vertically coloumn way 
arr2 = np.append(arr, [[5,6]], axis=0)  # axis 0 add value in x axis like horizontal rows way
print(arr1)
print(arr2)

'''
Q24. Delete a Row
Given [[1,2,3],[4,5,6],[7,8,9]], delete the middle row. Then make another version deleting the middle column
'''
aar = np.array([[1,2,3],[4,5,6],[7,8,9]])
arr = np.delete(aar, 1, axis=0) # ok here i passed row addres as 1 and with this also added axis to tell that remove the elemnet along the x axis in row 1 
# arr = np.delete(aar, 1) # if i give like this it remove the element at index 1 in row one and flatten the array
arr = np.delete(aar, 1, axis=1) # remove all element along y axis at postion 1 in each row
print(arr)

arr1 = np.delete(aar, 1, axis=0 )

aar3 = np.array([[1,2,3],[4,6],[7,8,9]]) # we need to mentain the shape we can not remove a element and keep the shape both at same time unless we replace it withsome think else thats why array was getting flattened i thind when i removed only one element 
print(aar3)


'''
Level 6: Axis + Functions
Q25. Column-wise vs Row-wise Minimum
For [[10,20,30],[5,25,15],[8,12,40]], find the minimum column-wise and row-wise. Before running it, predict what
axis=0 and axis=1 will produce.

axis 0 -> 10 , 5 , 8
axis 1-> 5 , 12, 15  # not sure lets check it  this is incorrect our in output we got reversse of what we gueesed 0 on 1 and 1 on 0
'''
import numpy as np

arr = np.array([[10,20,30],[5,25,15],[8,12,40]])
print(np.max(arr, axis=0))
print(np.max(arr, axis=1))  # oops its max we have to check min
print(np.min(arr, axis=0))
print(np.min(arr, axis=1)) 


'''
Q26. Cumulative Sum
For arr=[1,2,3,4,5], calculate the cumulative sum. Then try cumulative product.
'''
#cumlative sum is like adding all number togeather => 0+1= 1, 1+2 = 3 , 3+3= 6 , 6+4 = 10 , 10+5 = 15 we get these in an new array form 
arr = np.array([1,2,3,4,5])
# i do not remeber eexact function we use for this so ill gonna give it a guess i first tried sum but it did not work so used google
print(np.cumsum(arr))
print(np.cumprod(arr))
'''
Q27. Square Root
For arr=[1,4,9,16,25], find the square root of every element using NumPy.
'''
arr = np.array([1,4,9,16,25])
print(np.sqrt(arr))

'''
Q28. Trigonometric Functions
Create arr=[0, np.pi/2, np.pi]. Find sine and cosine, then inspect the results
'''
arr = np.array([0, np.pi/2, np.pi])
print(np.sin(arr))
print(np.cos(arr))
# i do not remember the exact function name we use to get cosine so let me google it oops my bad cosine is cos i am like 0 in math ingore this pls 
