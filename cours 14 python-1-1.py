# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 13:05:11 2023

@author: Msi
"""

import pandas as p

print(p.__version__)

#d=p.read_json? #pour regarder les files que l'on peut utiliser

df=p.read_csv("C:/Users/Msi/.spyder-py3/autosave/Educational_Attainment_20231027.csv")
df.head(5)#donne les 5 premieres lignes
df.head(2)
df.tail()#donne la fin du tableau
df.tail(10)
df.describe()#donne toutes les différenets variables
df.shape()#donne la taille du tableau excel
df.dtypes()#donne le type de chaques variables
df.drop("nom de la colonne", axis=1).describe(include="all")#pour supprimer une colonne(1) ou ligne(0)

df.columns=df.columns.str.replace(' ','')
df.columns=df.columns.str.replace("'","")

df.Geography.unique()
df.LessThanHighSchoolGraduate.value_counts()

#ex1
import pandas
schema_df=pandas.read_csv("C:/Users/Msi/.spyder-py3/autosave/survey_results_public - Copie.csv")
schema_df.shape
schema_df.head

schema_df.loc[1000:2000,'MainBranch':"Age"]

#ex2

import pandas
baby_names=pandas.read_csv("C:/Users/Msi/Downloads/US_Baby_Names_right (1).csv")
baby_names.head(10)
baby_names2=baby_names.drop("Unnamed: 0",axis=1).describe(include="all")
baby_names=baby_names2.drop('Id',axis=1).describe(include="all")

baby_names.head(2)

#or delete
#del baby_names['Unnamed: 0']






