# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 19:54:50 2023

@author: Msi
"""

#cours6: Les lists complex

a=[1,2,"5","Name"] #comment écrire une list

a.append("Margot") or a.add("Margot") #rajouter un élément dans la liste
a.remove("Name") #retire un élémengt de la liste
a[index]="ce que l'on veut changer" #permet de changer qqchose dans la liste 

print(a[index])#affiche un seul element de la liste

#les tuples sont immutable
a_tuple=("joe","margot","2021-01") #on ne peut pas ajouter , changer ou retirer


#les sets
a_set={"Margot","joe","arthur"}

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


#exo1: faire la somme d'une série en utilisant une liste
n= int(input("Enter a value:"))
the_list=[]
for i in range (1,n+1):
    the_list.append(1/i)
    print(the_list)
Sn=sum(the_list)
print(f"The sum is {Sn}")

#ex
nat7= list(range(7))
print(nat7)
print(type(nat7))

#ex écrire un elist fin cree une list
print("This programm will create a list from real numeric data ")
nval=int(input("Enter nb of values:"))
llnum=[]
for i in range (nval):
    value=float(input("Enter a numeric value:"))
    llnum.append(value)
print(llnum)

#ex sépare la phrase la ou ya un a 
line="Temperature is 298.15 K before combustion"
words=line.split('a')
print(words)

#ex sur mettre une temp dans une liste en sépare
ligne=input("Enter, in a single line and SEPARATED BY SPACES, the desired temp")
smooth_text=ligne.split()
print("List is now {}".format(smooth_text))
temp=[]
for element in smooth_text:
    value=float(element)
    temp.append(value)
    
print("The final list is {}".format(temp))

#ex
a=[1,3,5,7,11]
b=[13,17]
c=a+b
print ("First instruction print: {}".format (c))
b[0] = -1
d = []
for e in a:
  d.append (e+1)
print ("Second instruction print: {}". format (d))
d.append(b[0] + 1)
d.append(b[-1] + 1)
print ("Third instruction print: {}". format (d))
print ("Fourth instruction print: {}".format (d[-2:])) 
print ("Fifth instruction print: {}".format(d[:-1])) 
print ("Sixth instruction print: {}".format(d[1:4]))

#ex sur list des carrées des nb naturels
n=int(input("enter a value :"))
list_margot=[]
for i in range (1,n+1):
    list_margot.append(i**2)
print(list_margot)


#ex sur la liste des notes d'un exam
liste_name=[]
list_grade=[]
mean=0
number_of_student=int(input("Enter a number of student:"))
for i in range (1,number_of_student+1):
    name=input("Enter a name:")
    liste_name.append(name)
    grade=int(input("Enter the grade:"))
    list_grade.append(grade)
    mean=mean+grade
    print(name)
    print(grade)

print(liste_name)
print(list_grade)
average=mean/number_of_student
print("The average of the grade is {}".format(average))









