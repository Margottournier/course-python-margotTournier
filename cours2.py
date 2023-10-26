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

print(message.find('o'))

#cours4 while

#ex1
num=int(input("Enter an integer value:"))

while num>0:
    res=num//3
    print('The integer division of {} by 3 gives: {}'.format(num,res))
    num=int(input("Enter an integer value:"))

print("We're done")

#ex2

num=int(input("Enter an integer value:"))
ndiv=1

while ndiv<num:
    res=num//ndiv
    print("The integer division of {} by {} gives: {}".format(num,ndiv,res))
    ndiv=ndiv+1 #ou ndiv+=1

print("We're done")
print("Total number of division: {}".format(ndiv))


#ex3
num=int(input("Enter an integer value:"))
ndiv=0

while ndiv<num:
    res=num//3
    print("The integer division of {} by 3 gives: {}".format(num,res))
    ndiv=ndiv+1 #ou ndiv+=1
    print("Number of division so far: {}".format(ndiv))
    num=int(input("Enter an integer value:"))

print("We're done")
print("Total number of division: {}".format(ndiv))

#ex4
num=1
ndiv=0

while num>0 and num<211:
    if num%3==0:
        print(f"The number is {num}")
        ndiv=ndiv+1
    num=num+1
    
print("We're done")
print("Total number of division: {}".format(ndiv))

#EX5 sum of 10 first matural number
num=0
i=0
while num<=10:
     i=i+num
     num=num+1
print(i)

#ex6  moyenne de 10 nb donnee

i=0
sum=0
while i<10:
    num=int(input("Enter an integer value:"))
    sum=sum+num
    i=i+1

average=sum//10
print(average)


#ex7 faire la pyramide en etoile
i=1
while i<=4:
    print("*"*i)
    i=i+1
# avec boucle for     
x=int(input("nb of line: "))
nb=0
for i in range (x):
    nb+=1
    print(nb*"*")
    
    
#ex avce des factoriels
num=int(input("Enter an integer value:"))
f=num
r=1
while f!=0:
    r=r*f
    f=f-1
print("Factorial of",num,"is:",r)

#EX pour reecrire le nom d'utilisateur en nom avec lettre espace en s'arretant au 1er nb
name='Jesaa29Roy'
size=len(name)
i=0 #iterate loop till the last characters
while i <size:
    #break loop if current charcater is number
    if name[i].isdecimal():
        break;
    #print current character
    print(name[i],end=' ')
    i=i+1
print("\nThe execution has stopped")

# ex meme chose mais juste ca skip les num
name='Jesaa29Roy'
size = len(name)
i=-1
#iterate loop till the last character
while i<size-1:
    i=i+1
    #skip while loop body if current character is not alphabet 
    if not name[i].isalpha():#or isdecimal() pour avoir juste les nombres
        continue
    #print current character
    print(name[i],end=' ')
    
#boucle for
#for i in range (3):
    #print("value of i : {}".format(i))
    
#ex boucle for
n=int(input("Enter the value of n: "))
for i in range (n):
    q_i=i**2 #we calculate the square of the value i 
    print(q_i)# we write its value



