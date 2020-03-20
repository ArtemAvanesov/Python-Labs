import matplotlib.pyplot as plot
import numpy as np
import math

# Переменные в которые будут помещены входные данные
input_y = []
input_x = []

# Чтение значений x
with open("Лабораторные 1 курс/2_RBF/input_x.txt") as file:
    input_x1 = [row.strip() for row in file]
    input_x.append(list(float(element) for element in input_x1)) 
    input_x = input_x[0]

# Чтение значений y
with open('Лабораторные 1 курс/2_RBF/input_y.txt') as file:
    input_y1 = [row.strip() for row in file]
    input_y.append(list(float(element) for element in input_y1)) 
    input_y = input_y[0]

# Пустой массив в который будет помещен ответ сети (21 точка)
output_y = [0]*len(input_y)

# Норма обучения (коэффициент, от которого зависит величина изменения веса)
proportionality_constant = 0.1
# Константа, от ее значения зависит ширина колокола кривой
sigma = 0.7

# Начальные веса сети
w = [0.5]*9
nets = [0]*9
# Число базисных функций выбирается произвольным образов, были выбраны девять
# функций с центрами в точках: [-0.8, -0.6, -0.4, -0.2, 0, 0.2, 0.4, 0.6, 0.8]
c = [-0.8, -0.6, -0.4, -0.2, 0, 0.2, 0.4, 0.6, 0.8]

# Аппроксимация с помощью взвешенных сумм функции Гауса (параметр с задает центр функции; может быть другая функция)
def net(sigma, c, x): 
    return math.exp((-0.5*sigma) * ((c-x)**2))

# Вычисление ошибки (разности фактического значения и значения рассчитанного сетью)
def error(index):
    return input_y[index] - output_y[index]

def calculate_nets(x):
    global nets
    for i in range(len(c)):
        nets[i] = net(sigma, c[i], x)

# Вычисление весов с учетом ошибки (разности фактического значения и значения рассчитанного сетью)
def correct_weights(index):
    global w
    for i in range(len(w)):
        w[i] += proportionality_constant * error(index) * nets[i]

# Умножение матриц весов и nets
def sum_of_multiply(weights, values):
    return np.array(values).dot(np.array(weights))

# Обучение сети
def learning(iterations):
    global output_y
    for _ in range(iterations):
        for i in range(len(input_x)):
            calculate_nets(input_x[i])
            output_y[i] = sum_of_multiply(w, nets)
            correct_weights(i)
        if _ == iterations - 1:
            for i in range(len(input_x)):
                calculate_nets(input_x[i])
                output_y[i] = sum_of_multiply(w, nets)

# Запуск обучения сети на 10000 иттераций
learning(10000)

# Запись ответа в файл
f=open("Лабораторные 1 курс/2_RBF/output.txt",'w')
for item in output_y:
    f.write("%s\n" % item)
f.close()

# Расчет значения y с использованием обученной сети
def value_y_with_user_data(input_x):
    answer_y_array = []
    for element in input_x:
        calculate_nets(element)
        answer_y = sum_of_multiply(w, nets)
        answer_y_array.append(float(answer_y))
        print("User data: x = {}, answer RBF: y = {}".format(element, answer_y))
    return answer_y_array

# Точки в которых необходимо спрогнозировать y
user_x_data = [1.1, 1.2, 1.3, 1.4]

# Вызов функции расчета значений y по заданным x с использованием обученной сети
answer_y_array = value_y_with_user_data(user_x_data)

# График с фактическими данными
plot.scatter(input_x, input_y)

# График с расчитанными сетью значениями плюс прогноз
input_x_plus_prognoz = input_x
output_y_plus_prognoz = output_y
for element in user_x_data:
    input_x_plus_prognoz.append(float(element))
for element in answer_y_array:
    output_y_plus_prognoz.append(float(element))
plot.plot(input_x_plus_prognoz, output_y_plus_prognoz)
plot.show()