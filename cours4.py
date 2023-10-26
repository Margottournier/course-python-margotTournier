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
    
#cours 5 boucle for
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


#cours 6

int=[1,2,3,4]
print(int)
smooth=[3.14,7,-2+3j,'water',False,[1,2]]
long_smooth=len(smooth)
print(long_smooth)
print(smooth)
smooth[3][4]#donne dans le mot "water" la 5e lettre (4e index)
print (smooth[5][1])#va dans la 2e list a l'interieur et prend le 2e element
smooth[2:5]#ca ecrit du 2e element au 4e element sans prendre en compte le 5e
smooth[:4]#ca écrit tout jusqu'au 3e element 
smooth[1:]#ca écrit tt la liste except le 1er element

bg=[3.14,7,-2+3j,'water',False,[1,2],5,"Hello","Hi","1","e"]
bg[::2]#ca fait un pas de 2 en 2 , on ^rend que les éléments 1 sur 2
print(bg[-1])
print(bg[-2])
bg.pop(2)#retire l'élément à l'index 2
print(bg)






