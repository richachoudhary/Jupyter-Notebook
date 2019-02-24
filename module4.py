# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 02:51:05 2019

@author: RICHA
"""

#All third party packages require to be imported first in Python. 'np' is used to simplify and avoid repeating 'numpy' all time. You can choose any other name.
import numpy as np

#A simple NumPy array can be defined by providing a single list of numbers as an argument.
np_list = np.array([1, 2, 3])
print("1 dimensional array = ", np_list)

#A Numpy matrix can be defined by providing sequences of sequences.
matrix_2d = np.array ([[1, 2, 3], [4, 5, 6]])
print("2 dimensional array = ", matrix_2d)

matrix_3d = np.ones((2, 1, 4))
print("3 dimensional array = ", matrix_3d)



a = np.array([[1, 2, 3], [4, 5, 6]])

# the dimensions of the array.
print('shape = ', a.shape)

# the number of axes (dimensions) of the array.
print('dimension = ', a.ndim)

# an object describing the type of the elements in the array.
print('data type = ', a.dtype.name)

# the size in bytes of each element of the array.
print('size in bytes = ', a.itemsize)

# the total number of elements of the array.
print('total no. of elements = ', a.size)

print('type = ', type(a))


#Range function in Numpy
print('Range 0 to 9 with step 1 difference = ', np.arange(0, 10))

#Range function in Numpy with step difference
print('Range 0 to 10 with step 2 difference = ', np.arange(0, 11, 2))


#Range function in Numpy
print('Elements from 0 to 10 with 50 samples = ', np.linspace(0, 10, 50))


print('array of zeros = ', np.zeros((5, 5))) #Create array of zeros

print('array of ones = ', np.ones((2, 3, 4), dtype=np.int16)) #Create array of ones & data type can be specified

print('empty array = ', np.empty((2, 3))) #Create array with very small values

print('Identity matrix = ', np.eye(4)) #Create identity matrix

print('Single integer number = ', np.random.randint(24, 110))

print('Multiple integer number = ', np.random.randint(24, 110, 10))

print('Array of random numbers = ', np.random.rand(10))

print('Matrix of random numbers = ', np.random.rand(5, 5)) 

#Define an array of shape (1, 25)
arr = np.arange(1, 25)
print('Array with dimension (1, 25) = ', arr)

#Change the dimensions from (1, 25) to (25, 1).
mod_array = arr.reshape(24, 1)
print('Array with dimension (25, 1) = ', mod_array)

ary= np.arange(3,10)

#Print elements from position 1 to 6
print('elements from position 1 to 6 = ', ary[:5])

#Print elements from position 2 to 6
print('elements from position 2 to 6 = ', ary[1:5])

#Print the last element
print('the last element = ', ary[-1])

#Print all elements in reverse order
print('all elements in reverse order = ', ary[::-1])


arr = np.arange(0, 10)

#Add
print('arr + arr = ', arr + arr)

#Subtract
print('arr - arr = ', arr - arr)

#Multiply
print('arr x arr = ', arr * arr)

#Divide
print('arr / arr = ', arr / arr)

import numpy as np
arr = np.arange(0, 10)

#Square root of arr
print('Square root of arr = ', np.sqrt(arr))

#Exponent of arr
print('\nExponent of arr = ', np.exp(arr))

#Sine of arr
print('\nSine of arr = ', np.sin(arr))

#Log of arr
print('\nLog of arr = ', np.log(arr))

#Create an array with random numbers of dimension (3, 4)
a = np.floor(10*np.random.random((3,4)))
print('a = ', a)

#We will use 'T' method for transpose.
print('Transpose of a = ', a.T)

























