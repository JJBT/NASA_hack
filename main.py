import pandas as pd
from Constants import *
import json
import os


df = pd.read_csv("C:/Users/Vladimyr/Desktop/NYPD.csv", sep=',')
a = df.iloc[1:5, :]
print(a["ZIP CODE"])
a["ZIP CODE"].fillna(a[pd.notnull(a["ZIP CODE"])]["ZIP CODE"].mean(), inplace=True)
print(a["ZIP CODE"])
# print(a[pd.notnull(a["ZIP CODE"])])
# print(b)
