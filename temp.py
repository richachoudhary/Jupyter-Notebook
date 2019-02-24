s# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy 
import matplotlib.pyplot as plt 
#print (numpy.__version__)
#print (matplotlib.__version__)
import pandas
import sklearn
#print (pandas.__version__)
import seaborn
#print (seaborn.__version__)
#print (sklearn.__version__)
from pandas.plotting import scatter_matrix
from sklearn import  model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
#from sklearn.tree import DecisionTreeClassifier
#from sklearn.neighbors import KNeighborsClassifier
#from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
#from sklearn.naive_bayes import GaussianNB
#from sklearn.svm import SVC
# Load dataset
url = r"C:\Users\RICHA\Desktop\iris.csv"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = pandas.read_csv(url, names=names)
print(dataset.shape)
#print (dataset.head(20))
#print (dataset.describe()) 
#mean,mode statistics 
#print (dataset.groupby('class').size())

#data visualization 
#univariate plot 
#box and whiskers plots
#dataset.plot(kind='box', subplots= True , layout= (2,2), sharex= False, sharey= False)
#plt.show()

dataset.hist()
plt.show()
dataset.plot(kind='density', subplots= True , layout= (2,2), sharex= False, sharey= False)
