# Linear Discriminant Analysis
from sklearn import datasets
from sklearn import metrics
from sklearn.lda import LDA
# load the iris datasets
dataset = datasets.load_iris()
# fit a LDA model to the data
model = LDA()
model.fit(dataset.data, dataset.target)
print(model)
# make predictions
expected = dataset.target
predicted = model.predict(dataset.data)
# summarize the fit of the model
print(metrics.classification_report(expected, predicted))
print(metrics.confusion_matrix(expected, predicted))