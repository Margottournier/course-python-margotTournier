# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 13:00:17 2023

@author: Msi
"""

import matplotlib.pyplot as plt

import numpy as np

#%matplotlib inline

x=np.linspace(-2,2,101)
y=x**2
print(x)

plt.plot(x,y)#vectors x,y
plt.title("graph of x**2 vs x")
plt.show()

