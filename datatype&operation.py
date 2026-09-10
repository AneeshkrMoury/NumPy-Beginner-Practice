#data type in numpy array

var = np.array([1,2,3,4])
print(f"Data Type : {var.dtype}")

varq = np.array([1.4,2,3.5,4])
print(f"Data Type : {varq.dtype}")

var1 = np.array(["a","C"])
print(f"Data Type : {var1.dtype}")

var2 = np.array([1.4,"D",3.5,4])
print(f"Data Type : {var2.dtype}")

#changing data type can use both full form or sort 
x = np.array([1.4,2,3.5,4], dtype=np.bool)
print(f"Data Type : {x.dtype}")
print(x)


#arthmetic operation on numpy array 
# we can use direct like a + b. a-c ,a*b or we can use its function like np.add(), np.suntract() etc

# in 1d array
var = np.array([1,2,3,4])
varadd = var + 3 # add 3 on each element of array 
print(varadd)

var1 = np.array([5,6,7,8])

addvar = var1 + var # add caresponding element of each array 
print(addvar)


subvar = var1 - var # - caresponding element of each array 
print(subvar)

multivar = np.multiply(var , var1) # * caresponding element of each array 
print(multivar)

# smilarly we can do other operation


#2D

d1 = np.array([[1,2,3],[5,6,7]])
d2 = np.array([[5,6,7],[8,9,10]])

print(np.add(d1 , d2)) #similarly we can perform other operation
