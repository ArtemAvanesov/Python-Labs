import numpy as np
import matplotlib.pyplot as plt

# Входные данные для обучения
x = np.array([
    [1, 1],
    [1, 0],
    [0, 1],
    [0, 0]
]).reshape(4, 2)

# Выходные данные для обучения
y = np.array([0.1, 0.9, 0.9, 0.1]).reshape(4, 1)

# Параметры сети
n = 0.3
a = 10

# Начальные веса после входного слоя
w1 = np.array([
    [-0.5, 0.2], 
    [0.4, -0.3], 
    [-0.6, 0.8]
]).reshape(3, 2)

# Начальные веса перед выходным слоем
w2 = np.array([-0.4, 0.6, -0.4]).reshape(3, 1)

def df(neti):
    return (a * np.exp(-neti * a)) / ((np.exp(-neti * a) + 1) ** 2)

def fsi(neti):
    return 1 / (1 + np.exp(-a * neti))

# Обучение сети
j = 0
while(j < 13000):
    i = 0
    while(i < 4):
        x1 = x[i][0] 
        x2 = x[i][1] 
        yT = y[i]
        net1 = x1 * w1[0][0] + x2 * w1[1][0] + 1 * w1[2][0]
        net2 = x1 * w1[0][1] + x2 * w1[1][1] + 1 * w1[2][1]
        y1 = fsi(net1)
        y2 = fsi(net2)
        net3 = y1 * w2[0] + y2 * w2[1] + 1 * w2[2]
        y3 = fsi(net3)
        qy = (yT - y3) * df(net3)
        q1 = df(net1) * qy * w2[0]
        q2 = df(net2) * qy * w2[1]
        w2_r = n * qy * np.array([y1, y2, 1]).reshape(3, 1)
        w2 = w2 + w2_r
        w1_r = np.array([
            [n * q1 * x1, n * q2 * x[i][0]],
            [n * q1 * x2, n * q2 * x[i][1]],
            [n * q1 * 1, n * q2 * 1]
        ]).reshape(3, 2)
        w1 = w1 + w1_r
        i += 1
    j += 1

d = 0

# Входные данные
x_r = np.array([
    [0.8, 1.1],
    [1.2, -0.1],
    [0.1, 0.9],
    [0.3, -0.3]
]).reshape(4, 2)

# Рассчет ответа сетью с рассчитаными ранее весами
while(d < 4):
    x11 = x_r[d][0] 
    x22 = x_r[d][1] 

    net11 = x11 * w1[0][0] + x22 * w1[1][0] + 1 * w1[2][0]
    net22 = x11 * w1[0][1] + x22 * w1[1][1] + 1 * w1[2][1]

    y11 = fsi(net11)
    y22 = fsi(net22)

    net33 = y11 * w2[0] + y22 * w2[1] + 1 * w2[2]
    yR = fsi(net33)
    
    # Обработка ответа сети
    if yR>0.5:
        yR=1
    else:
        yR=0
    print("answer: ", yR)
    d += 1