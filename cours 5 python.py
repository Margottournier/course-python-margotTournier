# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 19:53:42 2023

@author: Msi
"""

#Cours 5 boucle for

#range(n_initial,n_final-1,nb_de_pas)
#ex
n=int(input("Enter the value of n :"))
for i in range (n):
    q_1=i**2#we calculate the square of the value
    print (q_1)#we write its value

#ex1
n=int(input("Enter the value of n :"))
for i in range (1,n+1):
    q_1=i**2#we calculate the square of the value
    print (q_1)#we write its value

#ex2
n=int(input("Enter the value of n :"))
for i in range (1,n+1,2):
    q_1=i**2#we calculate the square of the value
    print (q_1)#we write its value
#{accumulator}
#ex
sum=0
for i in range (6):
    sum=sum+i
    print(f"The value of sum is in each iteration: {sum} ")
print("The sum is valid {} ".format(sum))

#ex3
prod=1 #si je met 0 la somme tot sera egal à 0
for i in range (1,6):
    prod=prod*i
    print("The partial sum is {}".format(prod))
print("The total sum is valid {}".format(prod))

#ex4
for i in range(4):
    for j in range (3):
        print("i = {}, j {}".format(i,j))

#ex somme 
n=int(input("Enter a value:"))
sum=0
for i in range(1,n+1):
    sum=sum+i
    print ("sum is {}".format(sum))
print("The sum is {}".format(sum))

#ex 
n=int(input("Enter a value:"))
sum=0
for j in range (1, n+1):
    q=(j+1)/(j**2)
    sum=sum+q
    print(sum)
print ("The value of the sum is {: .2f}".format(sum)) #.2f donne les 2 premieère decimale après la virgule
#print (f"The value of the sum is {sum: .3f}") 

#ex factorial of a positive integer 
n=int(input("Enter a value:"))
fact=1
for i in range(1,n+1):
    fact=fact*i
    print(fact)
print(f"The fact is {fact}")

#ex ou l'on écrit les pairs de 11 a 99
for i in range(1,10):
    for j in range (1,10):
        print("{}{}".format(i,j))
        
#ex ou l'on evite les pais 11 22 33 ...
for i in range(1,10):
    for j in range (1,10):
        if i!=j:
            print("{}{}".format(i,j))
#ex pyramide
a=int(input("Enter the nb of triangular nb you want:"))
for i in range (0,a+1):
    t=i*(i+1)/2
    print(t)

#ex variation with 3 digits
for i in range (1,10):
    for j in range (1,10):
        for k in range (1,10):
            print("{}{}{}".format(i,j,k), end=" ")

#ex faire la somme des 3 nombres dans un chiffre soit egal a 22
for i in range (1,10):
    for j in range (1,10):
        for k in range (1,10):
                if i+j+k ==22:
                    print("{}{}{}".format(i,j,k), end=" ")
#ex  le meme mais ou c la somme des 3 chiffres soit egale au cube du nb
for i in range (0,10):
    for j in range (0,10):
        for k in range (0,10):
                if (i**3+j**3+k**3) == (i*100+j*10+k):
                    print("{}{}{}".format(i,j,k), end=" ")

#ex divisors of a positive integer
n=int(input("Enter an integer:"))
i=1
for i in range(1,n+1):
    if(n%i==0):
        print(i,end=" ")
        i=i+1

#ex pour trouver si un nombre est un nb premier
nb=int(input("Enter an integer value: "))
val=True
for i in range(2,nb):
    if nb%i==0 :
        val=False
   

if val==True:
    print(f"The value {nb} is a prime nb ")
else:
    print(f"The value {nb} is not a prime nb ")

#exercice de fibonnaci
n=int(input("Enter an integer value: "))
u1=0
u2=1
var=0
for i in range (0,n):
    var=u1+u2
    u1=u2
    u2=var
print(u2)