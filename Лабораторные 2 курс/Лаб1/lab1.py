import numpy as np
import csv

dataset_filename = "2M6/affinity_dataset.txt"
X = np.loadtxt(dataset_filename) 

#print(X[:5])

num = [0, 0, 0, 0, 0]

def count_item():
    for sample in X:
        for i in range(0,5):
            if sample[i] == 1:
                num[i] +=1
    print("Количество появлений событий: ", num)
    return num

def para_valid(item1, item2):
    n = 0
    for sample in X:
        if (sample[item1] == sample[item2]) & (sample[item1] == 1):
            n +=1
    return n
        
def probab():
    num = [0, 0, 0, 0, 0]
    p = 0
    first = 0
    second = 0
    num = count_item()
    f = open("2M6/affinity_dataset.csv", "w+")
    for i in range (0, 5):
        for j in range (0,5):
            if(i != j):
                p = para_valid(i,j)/num[i]
                if i == 0: first = 'A'
                elif i == 1: first = 'B'
                elif i == 2: first = 'C'
                elif i == 3: first = 'D'
                else: first = 'E'
                if j == 0: second = 'A'
                elif j == 1: second = 'B'
                elif j == 2: second = 'C'
                elif j == 3: second = 'D'
                else: second = 'E'
                print(first, " ", second, " ", p)
                row = str(first) + str(second) + ";" + str(p) + "\n"
                f.write(row)
        f.write('\n')
    f.close()

probab()


    





