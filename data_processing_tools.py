#import libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('Data.csv')
X = dataset.iloc[:,:-1]
Y = dataset.iloc[:,-1]

#print naive data
print(X) 

print('#######') 
#missing data modification
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
imputer.fit(X.iloc[:, 1:3])  # iloc kullanımı ve [:, 1:3] indeksleme
X.iloc[:, 1:3] = imputer.transform(X.iloc[:, 1:3])  # iloc kullanımı ve [:, 1:3] indeksleme

#print converted data
print(X) 