import plotly.express
import csv
import numpy as np

coffe=[]
sleep=[] 

with open("cups of coffee vs hours of sleep.csv") as f:
    csvreader= csv.DictReader(f)
    for row in csvreader:
        coffe.append(float(row["Coffee in ml"]))
        sleep.append(float(row["sleep in hours"]))

corelation=np.corrcoef(coffe,sleep)
print(corelation[0,1])