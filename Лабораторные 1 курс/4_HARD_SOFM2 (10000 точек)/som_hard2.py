import numpy as np
import random
import matplotlib.pyplot as plt

points=[]
def read():
    i=0
    for i in range(10000):
        points.append([np.random.uniform(-1,1),np.random.uniform(-1,1)])

def d2(rj,ri):
    return (rj[0] - ri[0]) ** 2 + (rj[1] - ri[1]) ** 2

def sigma(n):
    sigma0=0.1
    tau1=1000/np.log(sigma0)
    return sigma0*np.exp(-n/tau1)

def hji(n,rj,ri):
    return np.exp(-d2(rj,ri)/(2*sigma(n)**2))

def eta(n):
    eta0=0.1
    tau2=1000
    return eta0*np.exp(-n/tau2)

class NN:
    def __init__(self, inputs):
        random.seed(1)
        self.inputs=inputs
        self.l=len(self.inputs)
        self.size=len(inputs[0])
        self.out=100
        self.w=np.random.uniform(-1,1,[self.l,self.out])


    def find(self,points,it):
        for k in range(it):
            for j in range(self.size):
                d = np.zeros(self.out)
                for i in range(self.out):
                    d[i]=(self.w[0][i]-points[0][j])**2+(self.w[1][i]-points[1][j])**2
                minimum=min(d)
                index = list(d).index(minimum)
                for i in range(self.out):
                    if i!=index:
                        self.w.T[index]+=eta(k)*hji(k,self.w.T[i],self.w.T[index])*(points.T[j]-self.w.T[index])
             


read()
points=np.transpose(points)

n=NN(points)
plt.scatter(points[0],points[1])
plt.scatter(n.w[0],n.w[1])
plt.figure(1)
plt.title("Before")

n.find(points,100)

plt.figure(2)
plt.scatter(points[0],points[1],c='g')
plt.scatter(n.w[0],n.w[1],c='r')
plt.title("After")

plt.figure(3)
plt.scatter(n.w[0],n.w[1])
plt.title("After clear")

plt.show()