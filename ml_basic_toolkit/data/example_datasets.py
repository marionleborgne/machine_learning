# Load and display details of the packaged datasets
from sklearn.datasets import load_boston
from sklearn.datasets import load_iris
from sklearn.datasets import load_diabetes
from sklearn.datasets import load_digits
from sklearn.datasets import load_linnerud
# Boston house prices dataset (13x506, reals, regression)
boston = load_boston()
print(boston.data.shape)
# Iris flower dataset (4x150, reals, multi-label classification)
iris = load_iris()
print(iris.data.shape)
# Diabetes dataset (10x442, reals, regression)
diabetes = load_diabetes()
print(diabetes.data.shape)
# Hand-written digit dataset (64x1797, multi-label classification)
digits = load_digits()
print(digits.data.shape)
# Linnerud psychological and exercise dataset (3x20,3x20 multivariate regression)
linnerud = load_linnerud()
print(linnerud.data.shape)