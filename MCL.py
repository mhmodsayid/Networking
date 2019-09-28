import sys
import random
import string
import decimal
import numpy as np
from decimal import Decimal
from array import array
decimal.getcontext().prec=100
import os
import sys

def main():
    power=2
    inflate=2
    done=0
    i=2894#nodes number
    Clusters=94
    clastering= np.zeros(shape=(i),dtype=int)
    np.set_printoptions(precision=2)
    a = np.zeros(shape=(i,i))
    data = np.loadtxt("HW2Net.net",skiprows=2,dtype=int)
    #for x in np.nditer(data,flags=['multi_index']):
    #    print(x[0], end=' ')
   
    for j in range(data.shape[0]):
        a[data[j,1].astype(int)-1,data[j,0].astype(int)-1]=1
        a[data[j,0].astype(int)-1,data[j,1].astype(int)-1]=1
    for j in range(i):#Add self loops to each node
        a[j,j]=1
    #Normalize the matrix
    for j in range(i):
        sum=np.sum(a[:,j])
        a[:,j]=a[:,j]/sum
    c=(a)
    temp=np.zeros(shape=(i,i))
    while not np.array_equal(c,temp):
        temp=c
        for j in range(power-1):
            c=c.dot(c)
        #multiply
        c=np.power(c,inflate)
        for k in range(i):
            c[:,k]=c[:,k]/np.sum(c[:,k])
        c=np.round(c,4)
        done+=1
        print(done)
        
    #print(a, end=' ')
   
    for j in range(2893):
        print(j,np.count_nonzero(c[j+1,:]!=0))

    Cnumber=0
    for j in range(2893):
        if c[j,j]!=0:
            count=np.count_nonzero(c[j,:]!=0)
            if count>1:
                np.place(clastering, c[j,:]!=0, Cnumber)
                Cnumber+=1
            else:
                np.place(clastering, c[j,:]!=0,-1)
        else:
            clastering[j]=-2
        
        
    
            
     #   *Vertices 2894.
    
    #num.savetxt('clustering.clu', DAT, delimiter=" ", fmt="%s") 
    
    np.savetxt('First_matrix.txt', c, delimiter=',',fmt='%1.4f')
    np.savetxt('clustering.clu', clastering, delimiter=',',fmt='%1.0f')


   
   
  #  with open('Arithmatic_Coding.txt', 'w') as f2:
        # write the result of Arithmatic_Coding

if __name__ == '__main__':
    main()