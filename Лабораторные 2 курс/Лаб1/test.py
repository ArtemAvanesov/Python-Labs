import numpy as np
import matplotlib.pyplot as plt
from scipy import sparse
from sklearn.datasets import load_iris
import pandas as pd
from sklearn.model_selection import train_test_split
from pandas import plotting
from sklearn.neighbors import KNeighborsClassifier    

x = np.array([[1,2,3], [4,5,6]])
print(format(x))

eye = np.eye (4)
print("массив NumPy:\n{}".format(eye))

data = np.ones(4)
row_indices = np.arange(4)
print("дичь - ", row_indices)
col_indices = np.arange(4)
eye_coo = sparse.coo_matrix((data, (row_indices, col_indices)))
print("формат COO:\n{}".format( eye_coo))

y =np.array([[0,0,0,0,0,0],
             [0,0,0,1,1,0],
             [0,0,0,0,0,0],
             [0,0,0,0,0,0],
             [0,0,0,0,0,0],
             [0,0,0,1,0,1],
             [0,0,0,0,0,0],
             [0,0,0,0,0,0],
             [0,0,0,0,0,0],
             [0,0,0,0,0,0]])
#print(y)

x = np.linspace(-10, 10, 100)
y = np.sin(x)
plt.plot(x, y, marker="x")
#plt.show()

data = {'Name': ["John", "Anna", "Peter", "Linda"], 'Location' : ["New York", "Paris", "Berlin", "London"], 'Age' : [24, 13, 53, 33]}
data_pandas = pd.DataFrame(data)
#display(data_pandas)
print(data_pandas)

iris_dataset = load_iris()
X = iris_dataset.data
y = iris_dataset.target
print("Ключи iris_dataset: \n{}".format(iris_dataset.keys()))
#print(iris_dataset.DESCR)
# print("Ключи iris_dataset: \n{}".format(iris_dataset.keys()))
# print("Ключи iris_dataset: {}".format(iris_dataset.DESCR))
print("Тип массива data: {}".format(type(iris_dataset['data'])))
print("Форма (shape) массива data: {}".format(iris_dataset['data'].shape))
print("Форма (shape) массива data: \n{}".format(iris_dataset['data'][:5]))

print("Тип массива target: {}".format(type(iris_dataset['target'])))
print("Форма массива target: {}".format(iris_dataset['target'].shape))
#print("Классы:\n{}".format(iris_dataset['target']))

print("Тип массива target_names: {}".format(type(iris_dataset['target_names'])))
print("Форма массива target_names: {}".format(iris_dataset['target_names'].shape))
#print("Классы:\n{}".format(iris_dataset['target_names']))

print("Тип массива data: {}".format(type(iris_dataset['data'])))
print("Форма массива data: {}".format(iris_dataset['data'].shape))
#print("Классы:\n{}".format(iris_dataset['data']))

X_train, X_test, y_train, y_test = train_test_split(iris_dataset['data'], iris_dataset['target'], random_state=0)
print("Форма массива X_train: {}".format(X_train.shape))
print("Форма массива X_test: {}".format(X_test.shape))
print("Форма массива y_train: {}".format(y_train.shape))
print("Форма массива y_test: {}".format(y_test.shape))

print('------------------------------------------')

#работает в юпитере
#%matplotlib inline
#iris_dataframe = pd.DataFrame(X_train, columns=iris_dataset.feature_names)
#grr = plotting.scatter_matrix(iris_dataframe, c=y_train, figsize=(15, 15), marker='o', hist_kwds={'bins': 20}, s=60, alpha=.8)
#knn = KNeighborsClassifier(n_neighbors=1)  
#knn.fit(X_train,y_train)
