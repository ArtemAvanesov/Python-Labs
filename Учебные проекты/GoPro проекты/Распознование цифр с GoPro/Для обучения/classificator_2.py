import numpy as np

X = np.genfromtxt('X_train.csv', delimiter=';', dtype=float)
Y = np.genfromtxt('data_train_Y.csv', delimiter=';', dtype=float)
W1 = np.zeros([35,15])
W2 = np.zeros([15,10])
teta = 0.3

for i in range(35):
    for j in range(15):
        W1[i][j] = float(np.random.uniform(-1,1))

for i in range(15):
    for j in range(10):
        W2[i][j] = float(np.random.uniform(-1,1))

def n(X,W):
    return np.dot(X,W)

def f(net):
    return 1/(1 + np.exp(-0.1*net))

def dy(net):
    return (0.1 * np.exp(-net * 0.1)) / ((np.exp(-net * 0.1) + 1) ** 2)

for t in range(1000):
    for g in range(1010):
        input = np.array([X[g]])
        net1 = n(input,W1)
        output = np.array([Y[g]])
        y1 = f(net1)
        net2 = n(y1,W2)
        y2 = f(net2)

        d_out = (output - y2) * dy(net2)

        delta_h = np.zeros(15)
        for i in range(15):
            for j in range(10):
                delta_h[i] += d_out[0][j] * W2[i][j] 
            delta_h[i] *= dy(net1[0][i])

        d_W1 = np.zeros([35, 15])
        for i in range(35):
            for j in range(15):
                d_W1[i][j] = delta_h[j] * input[0][i]
        d_W1 *= teta    
        W1 += d_W1

        d_W2 = np.zeros([15, 10])
        for i in range(15):   
            for j in range(10): 
                d_W2[i][j] = d_out[0][j] * y1[0][i]
        d_W2 *= teta   
        W2 += d_W2   

'''
X_test = np.genfromtxt('data_1_test_3_bits.csv', delimiter=';')
for i in range(10):
    input_1 = np.array([X_test[i]])
    net_1 = n(input_1,W1)
    y_1 = f(net_1)
    net_2 = n(y_1,W2)
    y_2 = f(net_2)
    for i in range(10):
        print(y_2[0][i])
    print('Number:')
    print(np.argmax(y_2[0]))
    print('--------------------------')'''
     
