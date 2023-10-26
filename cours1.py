# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import math as m
ang=float(input("Enter an angle in sexagesimal degrees: "))
ang_rad=ang*m.pi/180#convert the angle in radians
si=m.sin(ang_rad)#the sine is calculated
print("The sine of {} is {}".format(ang,si))

#ex2

num1=float(input("Enter a numeric value:"))
num2=float(input("Enter another numeric value:"))
sum=num1+num2
product=num1*num2
print("The sum of {} and {} is {}".format(num1,num2,sum))
print("The product of {} and {} is {}".format(num1,num2,product))

#ex convertir degree en Kelvin
T=float(input("Enter the temperature in Celsius: "))
Kel=T+273.15
print("The temperature {}Celsius is {}K".format(T,Kel))

#exercice volume et aire d'un carre
c=float(input("Enter the length of the edge of a cube:"))
area=6*c*c
volume=c*c*c
print("The area of the cube whom lenght is {} is {} cm^2".format(c,area))
print("The volume of the cube whom lenght is {} is {} cm^3".format(c,volume))

#exercice ou on demande le nombre de billets qu'une personne a et la somme que cela fait 
n10=int(input("Enter the number of 10 euro you have"))
n20=int(input("Enter the number of 20 euro you have"))
n50=int(input("Enter the number of 50 euro you have"))
sum=n10*10+n20*20+n50*50
print("If the user has {} tickets of 10 euros, {} of 20 euros and {} of 50 , in total he has {} euros".format(n10,n20,n50,sum))

#exercice ou on demande la longueuer et l'air d'un cercle
import math
rad=float(input("Enter the radius of the circle"))
L=2*math.pi*rad
A=math.pi*rad**2     #math.exp()
print("For a radius of {} cm the length of the circuference is {}cm and the value of the area is {} cm^2".format(rad,L,A))

# meme chose mais pour une sphere
import math
rad=float(input("Enter the radius of the sphere"))
V=4/3*math.pi*rad**3
A=4*math.pi*rad**2
print("For a radius of {} cm the length of the circuference is {}cm and the value of the area is {} cm^2".format(rad,V,A))


#exercice avec une formule de constante de réaction
import math
A=float(input("Enter the A value:"))
Ea=float(input("Enter the Ea value:"))
T=float(input("Enter the temperature in Kelvin:"))
T=T+273.15
R=8.314
k=A*math.exp(-Ea/(R*T))
print("the rate constant is {}".format(k))

#exercice sur la longueur des cotes d'un triangle
import math
a=float(input("Enter the first side of the traingle"))
b=float(input("Enter the second side of the triangle"))
ang=float(input("Enter the angle in degree"))
c=math.sqrt(a**2+b**2-(2*a*b*math.cos(math.radians(ang))))
print("Given a triangle of side {} and {}, and a angle of {}° between them , the third side is {}".format(a,b,ang,c))

