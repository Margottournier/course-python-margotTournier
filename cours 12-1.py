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

#ex
x=np.linspace(0,3*np.pi,500)
plt.plot(x,np.sin(x**2))
plt.title('A simple chirp')
plt.show()

#ex2
x=np.linspace(-2,2,101)
y=x**2
plt.xlabel("x")
plt.ylabel("f(x)") #donne ne nom des axes
plt.xlim(-1.5,1.5)
plt.ylim(-0.5,2.5)#donne les points max et  min que l'on veut voir
plt.plot(x,y)
plt.show()

#ex3
x=np.linspace(-2,2,101)
plt.xlabel("x")
plt.ylabel("f(x)")
y=x**2
plt.plot(x,y,'g',label ='x**2') #'g' met couleur green sur le graphe
y2=x**4
plt.plot(x,y2,'ro',label ='x**4') # 'r' couleur rouge 'o' large dot=
plt.legend()
plt.show()
# plt.savefig("fig1.png") save the figure in your labtop

#ex4 trigonometric function
n=int(input("Enter the number of point:"))
x=np.linspace(-1,1,n)
plt.xlabel('x')
plt.ylabel('f(x)')
y=np.cos(2*np.pi*x)
plt.plot(x,y)
plt.title('2pix')
plt.savefig("cos2pix.png")
plt.show()

#ex5 2 trigo function
n=int(input("Enter the number of point:"))
x=np.linspace(-1,1,n)
plt.xlabel('x')
plt.ylabel('f(x)')
y=np.cos(2*np.pi*x)
plt.plot(x,y,label='cos(2pix)')
y2=np.sin(2*np.pi*x)
plt.plot(x,y2,label='sin(2pix)')
plt.title('2pix and 2sinx')
plt.legend()
plt.show()
plt.savefig("trigonometric.png")


#ex6 importance of the number of points in the representation
n=input("Enter the number of point:")
x=np.linspace(0,4,n)
plt.xlabel('x')
plt.ylabel('f(x)')
y=np.sin(np.pi*x)*np.sin(20*np.pi*x)*np.exp(-x)
plt.plot(x,y)
plt.title('sin*sin*exp')
plt.show()   

#ex7 isotherme of an ideal gas mix avec ex8 meme exo juste demande 5 fois la Temperature
n =int(input("nb"))
Temp1=int(input("T"))
Vm=np.linspace(2,10,n)
y1=0.08206*Temp1/Vm
plt.plot(Vm,y1,'g',label="temp1")

Temp2=int(input("T"))
Vm=np.linspace(2,10,n)
y2=0.08206*Temp2/Vm
plt.plot(Vm,y2,'bo',label="temp2")

Temp3=int(input("T"))
Vm=np.linspace(2,10,n)
y3=0.08206*Temp3/Vm
plt.plot(Vm,y3,'r',label="temp3")

Temp4=int(input("T"))
Vm=np.linspace(2,10,n)
y4=0.08206*Temp4/Vm
plt.plot(Vm,y4,'y',label="temp4")

Temp5=int(input("T"))
Vm=np.linspace(2,10,n)
y5=0.08206*Temp5/Vm
plt.plot(Vm,y5,'o',label="temp5")

plt.title("Five different temperature")
plt.show()





