import numpy as np
from scipy import sparse
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

# Задание: создать разреженную матрицу M, dim(M)=10×6, где M2,4 = M6,4 = M2,5 = M6,6 = 1
# с использованием обоих форматов. Вывести на печать, сравнить.
def skipy():
    eye = np.zeros((10,6)) 
    eye[1][3], eye[5][3], eye[1][4], eye[5][5] = 1,1,1,1 
    print(eye)
    sparse_matrix = sparse.csr_matrix(eye)                                                                                         # единичная - по диагонали 1, ост.0
    print("\nРазреженная матрица SciPy в формате CSR:\n{}".format(sparse_matrix))

    data = np.zeros(4)
    row_indices = [1,5,1,5]
    col_indices = [3,3,4,5]
    eye_coo = sparse.coo_matrix((data, (row_indices, col_indices)))
    print("\nФормат COO:\n{}".format(eye_coo))

skipy()

#Задание1: вывести на печать первые 5 примеров (samples) массива data
def iris():
    iris_dataset = load_iris()
    print("Первые 5 примеров: \n{}".format(iris_dataset['data'][:5]))

iris()

#Задание2: просмотреть oстальные ключи
def irisKey():
    iris_dataset = load_iris()
    print("Тип массива target_names: {}".format(type(iris_dataset['target_names'])))
    print("Форма массива target_names: {}".format(iris_dataset['target_names'].shape))
    print("Классы:\n{}".format(iris_dataset['target_names']))

    print("Тип массива feature_names: {}".format(type(iris_dataset['feature_names'])))
    print("Признаки:\n{}".format(iris_dataset['feature_names']))

    print("Тип массива DESCR: {}".format(type(iris_dataset['DESCR'])))
    print("Описание:\n{}".format(iris_dataset['DESCR']))

    print("Тип массива data: {}".format(type(iris_dataset['data'])))
    print("Форма массива data: {}".format(iris_dataset['data'].shape))
    print("Примеры:\n{}".format(iris_dataset['data']))

    print("Тип массива target: {}".format(type(iris_dataset['target'])))
    print("Форма массива target: {}".format(iris_dataset['target'].shape))
    print("Ключ класса:\n{}".format(iris_dataset['target']))

irisKey()
