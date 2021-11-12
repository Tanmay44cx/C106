import plotly.express
import csv
import numpy as np

temprature=[]
cold_drink_sales=[] 

with open("cold drink vs temprature.csv") as f:
    csvreader= csv.DictReader(f)
    for row in csvreader:
        temprature.append(float(row["Temperature"]))
        cold_drink_sales.append(float(row["Cold drink sales"]))

corelation=np.corrcoef(temprature,cold_drink_sales)
print(corelation[0,1])