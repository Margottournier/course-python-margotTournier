# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 09:33:33 2023

@author: Msi
"""

#cours 10: numpy
import numpy as np

a=np.array([1,2,3], dtype='int32')
print(a) 

b=np.array([[9.0,8.0,7.0],[6.0,5.0,4.0]])
print(b)

a.ndim #get dimension

b.shape #getshape

a.dtype #get type

a.itemsize #get size

a.nbytes #get total sizes 

a.size #get number of elements

c=np.array([[9.0,'c',7.0],[6.0,5.0,4.0]])
print(b)
c.shape
c.dtype

d=np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
print(d)

d[0,5] #get a specific elements
#le premier represente la permiere liste et le deuxieme la position

d[0,:] #get a specific row 

d[:,2] #get a specific column

d[-1,:] #derniere ligne

d[0,1:-1:2] #premier row, 2e element in a row,3e stop index, 4e stop size 

d[1,5]=20
d[:,2]=[1,2]
print(d)

np.zeros((2,3)) #cree une matrice de 0 dé 2 list et 3 elements

b=np.array([[[1,2],[3,4]],[[5,6],[7,8]]]) #matrices en 2 dimension
print(b) 

np.full((2,2),99) #le premier c'est la taille , le deuxieme c le nb qui se mets partout

np.full_like(a,4)

np.random.rand(4,2)

np.random.randint(-4,8, size=(3,3)) # le premier on specifie le min et le max et le deuxieme c'est la taille

np.identity(5) #matrice identite

#repeat array
arr= np.array([[1,2,3]])
r1=np.repeat(arr,3,axis=0)
print(r1)

arr=np.array([[1,0,1]])
r1=np.repeat(arr,3,axis=0)
print(r1)
r1[1,1]=2
print(r1)

output=np.ones((5,5))
print(output)
z=np.zeros((3,3))
z[1,1]=9
print(z)
output[1:-1,1:-1]=z
print(output)

a=np.array([1,2,3])
b=a
#b=a.copy()
b[0]=100
print(b)
print(a)

a+b
a/b
a*b
a-b

import math

np.cos(a)

#multiplier matrices
a=np.ones((2,3))
print(a)

b=np.full((3,2),2)
print(b)

np.matmul(a,b)

#autre exemple
d=np.random.randint(-4,2,size=(2,3))
print(d)
e=np.random.randint(-5,5,size=(3,2))
print(e)
print(np.matmul(d,e))
print(np.matmul(e,d))

#fait le determinant de 2 matrices
f=np.random.randint(-10,10,size=(4,4))
print(f)
g=np.random.randint(-4,10,size=(3,3))
print(g)
print(np.linalg.det(f))
print(np.linalg.det(g))

stats=np.array([[1,2,3],[4,5,6]])
stats
np.min(stats)
np.min(stats, axis=0) #axis 0 = ligne
np.min(stats,axis=1) # axis 1 =colonne
np.max(stats)

print(np.sum(stats))#la somme de toute la matrice
print(np.sum(stats), axis=0)#somme par ligne

arr=np.array([[1,2,3]])
r=np.repeat(arr,3,axis=-2)
print(r)

#axis -2->Row
#-1 -> Columne
#0-> Row 
#1 -> Column

#exemple

angles=[0,math.pi/4,math.pi/2,3*math.pi/4,math.pi]#list of angles in radians]
angles=np.array(angles)#the list is transformed into a numpy array
sin_angle=np.sin(angles)#the sine of all angles is calculated with a single instruction
print("Angles:{}".format(angles))
print("Sinus:{}".format(sin_angle))

#ex2
import numpy
npoints=21
values=np.linspace(-2.0,2.0,npoints)
print(values)

#ex3
#vect=np.arange(0,9,3) donne une matrice de 3 valeurs entre 0 et 9 
vect=np.arange(9)
print(vect)

npoints=21
values=np.linspace(10,20,npoints)
values[6]=1
print(values)














