# Cross Validation Classification
import numpy as np
from sklearn import datasets
from sklearn.linear_model import LogisticRegression
from sklearn import cross_validation
# load the iris datasets
dataset = datasets.load_iris()
# prepare cross validation folds
num_folds = 10
num_instances = len(dataset.data)
kfold = cross_validation.KFold(n=num_instances, n_folds=num_folds)
# prepare a Logistic Regression model
model = LogisticRegression()
# evaluate the model k-fold cross validation
results = cross_validation.cross_val_score(model, dataset.data, dataset.target, cv=kfold)
# display the mean classification accuracy on each fold
print(results)
# display the mean and stdev of the classification accuracy
print(results.mean())
print(results.std())