import pandas as pd
import json
import os


df = pd.read_csv("C:/Users/Vladimyr/Desktop/NYPD.csv", sep=',')
print(df.head())
print(df.tail(5).iloc[:, 5])
