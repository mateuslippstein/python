import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


dataset = pd.read_csv('/home/mlippstein/Projects/ml/python/machine_learning/part_one/data_preprocessing/Data.csv')
x = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

print(x)
print(y)