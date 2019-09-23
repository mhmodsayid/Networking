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

def decompress(bitin, out):# the Adaptive Arithmatic coding algorethem 
	initfreqs = arithmeticcoding.FlatFrequencyTable(257)
	freqs = arithmeticcoding.SimpleFrequencyTable(initfreqs)
	dec = arithmeticcoding.ArithmeticDecoder(32, bitin)
	while True:
		# Decode and write one byte
		symbol = dec.read(freqs)
		if symbol == 256:  # EOF symbol
			break
		out.write((str(symbol,)) if python3 else chr(symbol))
		freqs.increment(symbol)


def main():
    power=2
    inflate=2
    done=0
    i=4#2894
    clastering= np.zeros(shape=(i),dtype=int)
    np.set_printoptions(precision=2)
    a = np.zeros(shape=(i,i))
    data = np.loadtxt("HW2NetTest.net",skiprows=2,dtype=int)
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
    while done<1:
        for j in range(power-1):
            c=c.dot(c)

        #multiply
        c=np.power(c,inflate)
        for k in range(i):
            c[:,k]=c[:,k]/np.sum(c[:,k])
        done+=1
    #print(a, end=' ')
    for j in range(3):
        np.place(clastering, c[j+1,:]>0.1, j+1)

    np.savetxt('First_matrix.txt', c, delimiter=',',fmt='%1.6f')
    np.savetxt('clustering.txt', clastering, delimiter=',',fmt='%1.0f')


   
   
  #  with open('Arithmatic_Coding.txt', 'w') as f2:
        # write the result of Arithmatic_Coding

if __name__ == '__main__':
    main()