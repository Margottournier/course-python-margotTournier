# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 09:14:11 2023

@author: Msi
"""

#cours11:
    
import numpy as np
vect=np.linspace(11,31,30) #valeurs entre 11 et 31 sur 30 valeurs
print(vect)

import numpy
x= numpy.zeros(5)
print(x) #cree un vecteur comprenant que des 0 

import numpy 
nel= int(input("Enter the number of element in the vector:"))
lvec=[]#we create an empty list 
#lvec=numpy.zeros(nel)#we create the vector with zeros as component
for i in range (nel):
    comp=input("Enter the value of component{}:".format(i))
    lvec.append(float(comp))#convert it to real and add it to lvec
vec=numpy.array(lvec)#we create an array from the list
print(vec)

import numpy #mettre un espace entre chaque nombre lorsqu'on ecrit les valeurs
lin=input("Enter the components of a vector in a line")
smooth=lin.split()#we separate the line considering the targets
vec=numpy.float_(smooth)#we look at the back of the numpy float
print("List: {}".format(smooth))
print("Vector: {}".format(vec))

#Cree matrice
import numpy
mat=numpy.zeros((4,3))

for i in range(4):
    for j in range(3):
        mat[i,j]=float(input("Enter the value of the element{},{}".format(i,j)))
print(mat)

#1er exo FAIRE AB ET AB^-1
import numpy
matA=numpy.zeros((2,2))
matB=numpy.zeros((2,2))

for i in range(2):
    for j in range(2):
        matA[i,j]=float(input("Enter the value of the element{},{}".format(i,j)))
        matB[i,j]=float(input("Enter the value of the element{},{}".format(i,j)))
#print(matA)
#print(matB)

ab=numpy.matmul(matA,matB)
ab_invert=numpy.linalg.inv(ab)
ba_invert=numpy.matmul(numpy.linalg.inv(matB),numpy.linalg.inv(matA))
print("AB:\n",ab)
print("AB¨-1:\n",ab_invert)
print("\n(B)-1(A)-1 :\n",ba_invert)

#ex2: AXB=C
a=np.array([[1,1],[1,2]])
b=np.array([[4,1],[3,1]])
c=np.array([[24,7],[31,9]])

a_invert=np.linalg.inv(a)
b_invert=np.linalg.inv(b)
X=np.matmul(np.matmul(a_invert,c),b_invert)
print(X)

#exercice pH vector from list of proton concentrations
list=[2.07*(10**-5),2.62*(10**-7),3.22*(10**-5),2.59*(10**-4),4.87*(10**-5),1.19*(10**-4),3.95*(10**-5)]
vect=np.array(list)
vect=-1*np.log10(vect)
print(vect)


#ex Convert Armstrongs to Nanometers
import numpy as np

amstrongs_values = np.linspace(1.0, 5.0, 21)

nanometers_values = amstrongs_values * 0.1

for i, value in enumerate(nanometers_values):
    print(f"Value {i+1}: {value:.2f} nm")
    
#exercice table of values
x0=float(input("x0:"))
s=float(input("s:"))
init=float(input("initial x: "))
fin=float(input("Final x: "))
num=int(input("Number of point :"))
vect=np.linspace(init,fin,num)
arr=np.zeros((num,2))
for i in range(num):
    arr[i,0]=vect[i]
    arr[i,1]=(1/np.sqrt(2*np.pi))*np.exp((-1/2)*((vect[i]-x0)**2/s**2))
print(f"the final answer\n{arr:}")

#exercice Sea temperature stats
temp_mar=[13.8,13.3,13.9,15.0,16.4,20.0,21.9,22.3,22.0,21.2,18.8,16.0]
months=['January','February','March','April','May','June','July','August',"September","October","November","December"]
arr=np.array(temp_mar)
average=sum(arr)/len(arr)
print("Average: {}".format(average))
for i in range(len(temp_mar)-1):
    if(temp_mar[i]>temp_mar[i+1]):
        min_temp=temp_mar[i+1]
        min_month=months[i+1]
print("Coldest month: {}, at {}°C".format(min_month,min_temp))
for i in range (len(temp_mar)-1):
    if(temp_mar[i]<temp_mar[i+1]):
        max_temp=temp_mar[i+1]
        max_month=months[i+1]
print("Warmest month: {}, at {}°C".format(max_month, max_temp))

    



        






    
