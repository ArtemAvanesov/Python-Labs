import numpy as np

nums=np.array([[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,-1,-1,1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,-1,-1,1,-1,-1,1,1,1,1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,1,1,1,-1,-1,1,-1,-1,1,-1,-1,1,-1,-1,1,-1,-1,1,-1,-1,1,-1,-1,1,-1,-1,1,-1,-1,1,-1,-1,1,1,1,1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]])
result=nums[0]*np.reshape(nums[0], [63,1])+nums[1]*np.reshape(nums[1], [63,1])
i=0
f=open("Лабораторные 1 курс/5_Hopfield/kr5.txt")
one=f.read().split(";")
one=np.array([int(x) for x in one])
i=0
f.close()
while i<63:
    result[i][i]=0
    i+=1

k=1
l=0
end=0
x = np.arange(63)
np.random.shuffle(x)
while k:

    j=0
    while j<63:
        i=0
        sum=0
        sum=np.dot(one,result[x[j]])

        if end > 0:
            if(np.sign(sum)!=one[x[j]]):
                l=1
        else:
            one[x[j]]=np.sign(sum)
            if one[x[j]]==0:
                one[x[j]]=1

        j+=1

    if end!=0:
        break
    j=0
    while j<2:
        if (one==nums[j]).all():
            end=k
            if(j==0):
                print("Number is "+np.str(j))
            else:
                print("Number is "+np.str(j+1))

        j+=1
    k += 1


if l==1:
    print("Error!!")
else:
    print ("Neural network is well")