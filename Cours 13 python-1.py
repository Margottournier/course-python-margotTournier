# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 09:36:06 2023

@author: Msi
"""
name='names'
variable=open(name,options)

name=open("names.txt",'r')

variable=open("names.txt")
for i in variable:
    i=i.strip() #for delete the space between two variables
    print("Hello {}".format(i))
print(variable.mode)

variable=open("names.txt")
for i in variable:
    if "margot" in i:#condition for finding a name in a file
        i=i.strip() #for delete the space between two variables
        print("Hello {}".format(i))
        
f=open("test file",mode="r")

fnames=open('names.txt','r')
for name in fnames:
    print(name)

#this doesn't work
fnames=open("names.txt",'w')#if we put w this will not work and their will be an error 
for name in fnames:
    print(name)

#reading files ( context manager):
with open("test.txt","r") as f:
    pass

with open("test.txt",'r') as f:
    #small files
    f_content=f.read()
    #f_content=f.readlines() #for multiple lines for one line it's (.readline)
    print(f_content)


#writing files:
    #we have to put w and not r 
with open("test.txt","w") as f: 
    f.write("Test")


#writing starts:
with open("test4.txt","w") as f:
    f.write("Test")
    f.seek(0)#come back to index0
    f.write("Test")
    f.seek("R")


with open("test2.txt","w") as f:
    val1='10'
    val2="nhzag"
    f.write(val1+val2)
    f.seek(0)
    f.write("Test")
    f.seek(6)
    f.write("z")

#copying files:
with open("test.txt","r") as rf:
    with open("test_copy.txt","w") as wf:
        for line in rf:
            wf.write(line)

#copying your image
with open("python.jpg","rb") as rf:
    with open("python_copy.jpg","wb") as wf: #wb is for byte
        for line in rf:
            wf.write(line)





