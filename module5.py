# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 03:36:05 2019

@author: RICHA
"""

#All third party packages require to be imported first in Python. 'pd' is used to simplify and avoid repeating 'pandas' all time.
#You can choose other name as well.
import pandas as pd
import numpy as np

#Create series using python arrays
labels = ['a', 'b', 'c'] #Define labels
my_list = [10, 20, 30] #Define python array

series_variable = pd.Series(data=my_list, index = labels) #Define pandas.series

print(series_variable)

dict= {"richa": "aayush", "kanchan": "aashish"}

s_v= pd.Series(dict)
print(s_v)

#Define pandas.Series
ser_1 = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
print(ser_1)
ser_2 = pd.Series([4, 5, 6, 7], index=['a', 'c', 'e', 'f'])
print(ser_2)

#Add two series
ser_res = ser_1 + ser_2

#print results
print(ser_res) 

#Create pandas.DataFrame using Python dict object
d = {'col1': [1, 2], 'col2': [3, 4]} #Define a dict object

df = pd.DataFrame(data=d) #Define pandas.DataFrame object

print(df)

#Create pandas.DataFrame from numpy ndarray
from numpy.random import randn
np.random.seed(101)

df = pd.DataFrame(randn(5, 4), index = 'A B C D E'.split(), columns = 'W X Y Z'.split())

print(df)



































