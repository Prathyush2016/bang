import numpy as np
import time
import sys

####################################################################################
# Advantages of Numpy over list
####################################################################################
# Explaination of why numpy is less memory and easy to convinient

# S = 10000000
# L1=range(S)
# L2=range(S)
#
# A1= np.arange(S)
# A2= np.arange(S)
#
#
# start = time.time() #its a real time time caln
# result = [(x,y)for x,y in zip(L1,L2)]
# print((time.time()-start)*1000)
#
# start = time.time()
# result = A1+A2
# print((time.time()-start)*1000)
################################################################################
# Operation of numpy array
################################################################################
# 1 finding the dimantion and  size of the given array
# a = np.array([(1,2,3),(4,5,6),(1,88,4)])
# print(a.ndim)
# print(a.itemsize)
# print(a.dtype)
# print(a)
################################################################################
# 2 By using the numpy we can find the size of an array and also we can find the shape of the array
# print(a.size)                                                                  #total no of elements in the numpy array
# print(a.shape)                                                                 #shows the no of rows and the no  of coloums in the given array or you can call it as matrix
################################################################################
# 3 In numpy we can Reshape the array and slicing the array
# Reshape
# a = a.reshape(3,2)
# print(a)                                                                      #simple it changes the rows into colums and colums into rows
# slicing
# print(a[1,1])
# print(a[2,1])                                                                  #print(a[element,index])
# print(a[0:,1])
################################################################################
# 4 Linespace of the given numbers
# a = np.linspace(1,100,50)
# print(a)
################################################################################
# 5 Find the min ,max, and sum of the array
# a = np.array([1,2,3,4,55,6])
# print(a.min())
# print(a.max())
# print(a.sum())
################################################################################
# 6 Array axis
# There are two types of axis 0 and axis 1
# axis 0 is nothing but row of a matrix or array
# axis 1 is nothing but column of a matirx or array
# b = np.array([(1,2,3),(1,5,6)])
# print(b.sum(axis=1))
################################################################################
# 7 Finging the squrare and Standard deviatiion
# s = np.array([(5,6,5),(9,4,2)])
# print(np.sqrt(s))
# print(np.std(s))
################################################################################
# 8 Basic mathematical functions like add sub multi div
# a = np.array([(1,2,3),(4,5,6)])
# b = np.array([(1,2,3),(4,5,7)])
# print(a+b)
# print(a*b)
# print(a-b)
# print(a/b)
################################################################################
# NUMPY SPECIAL FUNCTIONS
################################################################################
# 1 sin function
# import matplotlib.pyplot as ppp
# x = np.arange(0,3*np.pi,0.1)
# y = np.sin(x)
# ppp.plot(x,y)
# ppp.show()
################################################################################
# 2 cos function
# import matplotlib.pyplot as ppp
# x = np.arange(0,3*np.pi,0.1)
# y = np.tan(x)                                                                   we can also use tan cos and sin
# ppp.plot(x,y)
# ppp.show()
################################################################################
# 3 exponiantial and logorithamic functions
# ar = np.array([(1,2,3),(4,5,6)])
# print(np.exp(ar))
# print(np.log10(ar))
# print(np.log(ar))
################################################################################
