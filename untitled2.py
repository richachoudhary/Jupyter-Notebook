# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 22:37:04 2019

@author: RICHA
"""

sq= []


#Return square of numbers in range o to 20 that are divisible by 3.
for x in range(20):
    if x%3 == 0:
     sq.append(x**2)
     
     
#print(sq)

capitals = {'United States': 'Washington, DC','France': 'Paris','Italy': 'Rome'}

capitalss = {capitals[key]: key for key in capitals }
#print(capitalss)

list= [x for x in 'words']
print (list)