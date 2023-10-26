# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

message='good morning'
print(len(message)) #taille du mot

print(message[8])#donne la lettre à la nieme place

print (message[0:4])#pour ecrire une partie du mot (faut faire n+1 au dernier sinon il manquera la derniere lettre)

print(message[8:11])

print (message[-1])#donne la derniere lettre du mot

print (message[2:-1])#donne le mot du start jusqu'a l'avant dernier mot

print(message.upper())#donne le mot en maj

print(message.lower())#donnele mot en minuscule

print(message.count('g'))#donne le nb de fois ou la lettre apparait

print(message.find('o'))#trouve la position du premier 'o'

new_message= message.replace('morning','Afternoon')
print(new_message)

print(dir(str))#montre totes les possibilités que tu peux faire avce des strings

#les loops
num=input("Enter an integer")
num=int(num)
if num <5:
    print("It's less than five")
else:
    print("It's greater than or equal to five")
    
#ex
num=int(input("Enter the number:"))
if num%2==0:
    print("The number {} is an even number ".format(num))
else:
    #print("The number {} is an odd number".format(num))
    print(f"The number {num} is an odd number")
    
#ex pour verifier la note d'un eleve
marks=float(input('Enter a grade(out of 10):'))  
if marks<40:
    print('The student has failed and got an F')
elif marks>40 and marks<=50:
    print('The student has passed marginaly and got an E grade')
elif marks>=50 and marks <=75:
    print("The student has passed with C grade")
elif marks >=75 and marks <=90:
    print("The student has done well and has scored B grade")
else:
    print("The student has done excellent and passed with Distinction, A grade")
                     
#ex pour calculer IMC
weight=float(input('Enter your weight:'))
height=float(input('Enter your height'))   
BMI=weight/(height**2)
if BMI<18.5:
    print("Your BMI is {} and you are in underweight".format(BMI))
elif BMI>=18.5 and BMI<25:
    print("Your BMI is {} and you are in normal weigth".format(BMI))
elif BMI>=25 and BMI<30:
    print("Your BMI is {} and you are in overweight".format(BMI))
else:
    print("Your BMI is {} and you are in obesity".format(BMI))
    
#exercice
n1= int(input("Enter a natural number:"))
n2= int(input("Enter an other natural number:"))
n=n1/n2
r=n1%n2
if r==0:
    print("The number {} is divisible by {} and the quotient is {}".format(n1,n2,n))
else:
    print("The number {} is not divisible by {} but the remainder is {} ".format(n1,n2,r))


#exercice chercher le minimum 
n1= int(input("Enter a natural number:"))
n2= int(input("Enter an other natural number:"))
if n1>n2:
    print("The number {} is bigger than {}".format(n1,n2))
elif n1<n2:
    print("The number {} is bigger than {}".format(n2,n1))
else:
    print("The number {} is equal to {}".format(n1,n2))
 
#exercice
a= int(input("Enter your unit:"))
if(a<100):
    print("You will have no charge ")
elif a>=100 and a<200:
    p=5*(a-100)
    print("You have {}unit so your bill will be Rs{}".format(a,p))
else:
    p=10*(a-200)+100*5
    print("You have {}unit so your bill will be Rs{}".format(a,p))