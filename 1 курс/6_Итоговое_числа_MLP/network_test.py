import numpy as np
W1 = np.load('Лабораторные 1 курс/6_Итоговое_числа_MLP/W1.npy')
W2 = np.load('Лабораторные 1 курс/6_Итоговое_числа_MLP/W2.npy')

def n(X,W):
    return np.dot(X,W)
def f(net):
    return 1/(1 + np.exp(-0.1*net))

def dy(net):
    return (0.1 * np.exp(-net * 0.1)) / ((np.exp(-net * 0.1) + 1) ** 2)

X_test = np.genfromtxt('Лабораторные 1 курс/6_Итоговое_числа_MLP/data_2_test_3_bits.csv', delimiter=';')
for i in range(10):
    input_1 = np.array([X_test[i]])
    net_1 = n(input_1,W1)
    y_1 = f(net_1)
    net_2 = n(y_1,W2)
    y_2 = f(net_2)

    for i in range(10):
        print(y_2[0][i])
    print('Answer: this is', np.argmax(y_2[0]))