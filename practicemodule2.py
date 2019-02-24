# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 12:16:11 2019

@author: RICHA
"""

#Writing Files
my_file = open('newric.py', 'w') #Step 1
my_file.write('This is a test line\n') #Step 2
my_file.close() #Step 3
my_file = open('newric.py', 'a')
my_file.write('This is Second test line\n')
my_file.close()
my_file = open('newric.py', 'r')
my_file.read()

#Note: 'w' method overwrites the content of file.