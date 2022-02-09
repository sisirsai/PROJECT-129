import pandas as pd
import numpy as np

df = pd.read_csv('Scraper.csv')

df1 = df.dropna()

df1['Mass'] = df1['Mass'].astype(float)
df1['Radius'] = df1['Radius'].astype(float)

df1['Mass'] = df1['Mass']*0.102763
df1['Radius'] = df1['Radius']*0.000954588

df1.to_csv('dataset1.csv')

import csv

dataset1 = []
dataset2 = []

with open('dataset1.csv' , 'r') as f:
    csv_reader = csv.reader(f)
    for row in csv_reader:
        dataset1.append(row)

with open('dataset2.csv' , 'r') as f:
    csv_reader = csv.reader(f)
    for row in csv_reader:
        dataset2.append(row)

headers1 = dataset1[0]
data1 = dataset1[1:]

headers2 = dataset2[0]
data2 = dataset2[1:]

headers = headers1 + headers2
data = []

for index,datarow in enumerate(data1):
    data.append(data1[index] + data2[index])

with open('overAll.csv' , 'a+') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(headers)
    csv_writer.writerows(data)