# Mark 0 values as missing and impute with the mean
import numpy as np
import urllib
from sklearn.preprocessing import Imputer
# Load the Pima Indians Diabetes dataset
url = "http://goo.gl/j0Rvxq"
raw_data = urllib.urlopen(url)
dataset = np.loadtxt(raw_data, delimiter=",")
print(dataset.shape)
# separate the data and target attributes
X = dataset[:,0:7]
y = dataset[:,8]
# Mark all zero values as 0
X[X==0]=np.nan
# Impute all missing values with the mean of the attribute
imp = Imputer(missing_values='NaN', strategy='mean')
imputed_X = imp.fit_transform(X)