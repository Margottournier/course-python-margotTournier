# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 15:33:37 2023

@author: Msi
"""
import matplotlib.pyplot as plt

import numpy as np

#ex1
x0=int(input("Enter the number of point:"))
x=np.linspace(-1,1,100)
s=float(input("Enter s :"))
plt.xlabel('x')
plt.ylabel('f(x)')
y=(1/np.sqrt(2*np.pi))*np.exp((-1/2)*((x-x0)**2)/s**2)
plt.plot(x,y)
plt.title('Gaussian function')
plt.show()
plt.savefig("Gaussian function")

#ex2
n=int(input("Enter the number of point:"))
x=np.linspace(0,3,n)
plt.xlabel("x")
plt.ylabel("f(x)")
y=np.exp(-x)
plt.plot(x,y,'b',label ='e-x') 
y2=np.sin(3*np.pi*x)*np.exp(-x)
plt.plot(x,y2,'r',label ='sin(3pix)e-x') 
plt.title('Functions')
plt.legend()
plt.show()

#ex3
n = int(input("How many?"))
for i in range (0,n):
    x = np.linspace(-1,1,100)
    s = float(input("s"))
    x0 = float(input("x0"))
    y = (1/np.sqrt(2*np.pi))*np.exp((-1/2)*((x-x0)*2)/(s**2))
    a = input("line : ")
    nom = input("name ? ")
    plt.plot(x,y,a,label = nom)

plt.title("Gaus")
plt.legend()
plt.show()