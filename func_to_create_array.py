# how to created numpy array using random number and function used inthis 

'''Functions'''
#-> rand(): use to generate random value between 0 to 1  give different value as each run
#1D
ran_fun = np.random.rand(4)
print(ran_fun)

ran_fun1 = np.random.rand(4)
print(ran_fun1)

#2D
var = np.random.rand(2,5)
print(var)

#-> randn(): generate random vlaue close to 0 this may be positive or negative 
varn = np.random.randn(2,5)
print(varn)

#-> ranf(): it return a array of specific shape and fills it with random floats in the half open interval [0.0,1.0] this mean from 0 - 0.999999E but not 1
rf = np.random.ranf(4)
print(rf)

#-> randint(): give random number between given 2 numbers 
rndit = np.random.randint(10, 15, 5)
print(rndit)
