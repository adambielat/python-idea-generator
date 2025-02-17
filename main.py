import csv;import pandas as pd;import random

dataframe = pd.read_csv('ideas.csv')
choice = random.randint(1,79)
printlast = dataframe.iloc[choice]
print(*printlast)
