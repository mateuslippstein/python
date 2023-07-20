import numpy as np
import pandas as pd

dataset = pd.read_csv('machine_learning/part_one/data_preprocessing/data/pima-indians-diabetes.csv')

# Identify missing data (assumes that missing data is represented as NaN)
missing_counts = dataset.isnull().sum()

# Print the number of missing entries in each column
print(missing_counts)

# Configure an instance of the SimpleImputer class
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values=np.nan, strategy='mean')

# Fit the imputer on the DataFrame
imputer.fit(dataset)

# Apply the transform to the DataFrame
df_imputed = imputer.transform(dataset)

#Print your updated matrix of features
print(df_imputed)