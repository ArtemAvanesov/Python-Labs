import numpy as np
import random
import matplotlib.pyplot as plt

points=[]

# Чтение данных с координатами точек
def read():
    f=open("Лабораторные 1 курс/4_HARD_SOFM1/som_hard.txt")
    one=f.read().split("\n")
    i=0
    while i<1000:
        loc=one[i].split(";")
        points.append(np.ravel(np.array([float(x) for x in loc])))
        i+=1
    f.close()

def d2(rj,ri):
    return (rj[0] - ri[0]) ** 2 + (rj[1] - ri[1]) ** 2

def sigma_func(n):
    sigma0=0.1
    tau1=1000/np.log(sigma0)
    return sigma0*np.exp(-n/tau1)

def hji_func(n,rj,ri):
    return np.exp(-d2(rj,ri)/(2*sigma_func(n)**2))

def eta_func(n):
    eta0=0.1
    tau2=1000
    return eta0*np.exp(-n/tau2)

class SOFM:
    def __init__(self, inputs):
        random.seed(1)
        self.inputs=inputs
        self.l=len(self.inputs)
        self.size=len(inputs[0])
        self.out=100
        self.w=np.random.uniform(-1,1,[self.l,self.out])


    def find(self,points,it):
        for k in range(it):
            j=0
            while j<self.size:
                i=0
                d = np.zeros(self.out)
                while i<self.out:
                    d[i]=(self.w[0][i]-points[0][j])**2+(self.w[1][i]-points[1][j])**2
                    i+=1
                minimum=min(d)
                index = list(d).index(minimum)
                i=0
              
                while i<self.out:
                    if i!=index:
                        self.w.T[index]+=eta_func(k)*hji_func(k,self.w.T[i],self.w.T[index])*(points.T[j]-self.w.T[index])
                    i+=1
                j+=1

# Вызов метода чтения исходных данных
read()

points=np.transpose(points)

n=SOFM(points)
plt.scatter(points[0],points[1])
plt.scatter(n.w[0],n.w[1])
plt.figure(1)
plt.title("Before")

n.find(points,100)

plt.figure(2)
plt.scatter(points[0],points[1])
plt.scatter(n.w[0],n.w[1])
plt.title("After")

plt.figure(3)
plt.scatter(n.w[0],n.w[1])
plt.title("After clear")

plt.show()