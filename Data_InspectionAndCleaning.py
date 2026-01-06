import pandas as pd
import numpy as np

## Objective
# To inspect the given data and clean it if required

data=pd.read_csv(r"C:\Users\HP\Desktop\Just_Chillin\VS_code\Python_Apoorva\DS\EDA_StudentData\StudentsPerformance.csv")

print(data.shape)
print(data.columns)

for i in data.columns:
    if data[i].dtype ==pd.Series(["Cat"]).dtype :
        print(f" {i} : {data[i].unique()}")

print(data.info())
print(data.describe())

## Conclusin
# No null values but some values repeated in different forms
# Like "High school" and "Some high school" are same information with different format
