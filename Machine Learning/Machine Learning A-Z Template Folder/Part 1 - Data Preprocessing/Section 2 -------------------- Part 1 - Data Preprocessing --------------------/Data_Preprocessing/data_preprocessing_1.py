# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#Importing libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Importing Data Sets
dataset = pd.read_csv('Data.csv')

#X contains all independent variables
X = dataset.iloc[:,:-1].values
#print (X) - Execute to verify values in X
#Y contains all dependent variables
Y = dataset.iloc[:,3]
#print (Y) - Execute to verify values in X
