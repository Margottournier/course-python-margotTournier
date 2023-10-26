# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 09:21:19 2023

@author: Msi
"""
#cours 8:Dictionnary

Dict={"Dict1":{1:'Geeks'},
      'Dict2':{"Name":'For'}}

print(Dict['Dict1'])
print(Dict['Dict1'][1]) #ecrire l'élément du 1er dico dans le dico principal
print(Dict['Dict2']['Name'])#ecrire l'élément du 2e dico

country_capitals={
"United states" : "Washington D.C",
"Italy":"Rome",
"England":"London"
}

del country_capitals["United states"]
print (country_capitals)

keys=('Ten','Twenty','Thirty')
values=(10,20,30)
res_dict=dict(zip(keys,values)) #permet d'écrir qu'un seul tuple au lie des tous les 3 , la fonction formkey
print(res_dict)

dict1={'Ten':10, 'Twenty': 20, 'Thirty':30}
dict2={'Thirty':30, 'Forty': 40, 'Fifty':50}
dict1.update(dict2)
print(dict1)

employees=['Kelly','Emma']
default={"designation":'Developer',"Salary":8000}
res=dict.fromkeys(employees,default)
print(res)








