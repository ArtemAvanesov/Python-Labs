import numpy as np
import random
import matplotlib.pyplot as plt

# Переменная для хранения количества точек в исходных данных
number_of_data = 0

# Чтение координат точек
def read():
    # Данные с явным разбиением на 3 кластера
    f=open("3_SOM/make_blobs.txt")
    # Данные посложнее
    #f=open("Лабораторные 1 курс/3_SOM/som.txt")
    one=f.read().split("\n")
    global number_of_data
    number_of_data = len(one)
    points_of_data=[]
    i=0
    while i<number_of_data:
        loc=one[i].split(";")
        points_of_data.append(np.ravel(np.array([float(x) for x in loc])))
        i+=1
    f.close()
    points_of_data=np.transpose(points_of_data)
    return points_of_data

# Поиск класстеров
def find_clusters(points_of_data,size_step_on_itteration,num_of_itterations,num_of_clasters):
    # Генерация случайных координат кластеров, от которых начнет двигаться алгоритм 
    random.seed(1)
    points_of_clasters=np.random.random((len(points_of_data),num_of_clasters))
    for i in range(num_of_itterations):
        j=0
        while j<number_of_data:
            i=0
            d = np.zeros(num_of_clasters)
            while i<num_of_clasters:
                d[i]=(points_of_clasters[0][i]-points_of_data[0][j])**2+(points_of_clasters[1][i]-points_of_data[1][j])**2
                i+=1
            minimum=min(d)
            index = list(d).index(minimum)
            points_of_clasters.T[index]+=size_step_on_itteration*(points_of_data.T[j]-points_of_clasters.T[index])
            j+=1
    return points_of_clasters

# Разбиение данных на кластеры
def segmentation_clusters(points_of_data, points_of_clasters):
    arr = []
    for i in range(len(np.transpose(points_of_clasters))): arr.append([[],[]])
    for i in range(0, number_of_data, 1):
        d = np.zeros(len(np.transpose(points_of_clasters)))
        for j in range(0, len(np.transpose(points_of_clasters)), 1):
            d[j]=(points_of_clasters[0][j]-points_of_data[0][i])**2+(points_of_clasters[1][j]-points_of_data[1][i])**2
        minimum=min(d)
        index = list(d).index(minimum)
        arr[index][0].append(points_of_data[0][i])
        arr[index][1].append(points_of_data[1][i])
    return arr

# Вызов метода чтения исходных данных
points_of_data = read()

# Вызов метода по поиску центров класстеров (предполагается 3 класстера)
points_of_clasters = find_clusters(points_of_data,0.01,500, 3)

# Вызов метода разбивающего данные на кластеры
arr = segmentation_clusters(points_of_data, points_of_clasters)

# Вывод координат центров класстеров
print("Координаты центров класстеров: \n{}".format(points_of_clasters))

# Построение графиков
#plt.scatter(points_of_data[0],points_of_data[1])
for i in range(len(arr)):
    plt.scatter(arr[i][0],arr[i][1])
for j in range(len(np.transpose(points_of_clasters))):
    plt.scatter(points_of_clasters[0][j],points_of_clasters[1][j], marker='*', color = 'black')
    plt.text(points_of_clasters[0][j],points_of_clasters[1][j], "  "+str(j+1))
plt.show()