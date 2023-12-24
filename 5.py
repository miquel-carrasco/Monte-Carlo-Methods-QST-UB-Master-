import numpy as np
import matplotlib.pyplot as plt
import random
import math
import os
from tqdm import tqdm


os.chdir(r'C:\Users\miqc1\OneDrive\Escritorio\Màster\Monte Carlo\5\data')

def Energy_Coulomb(r):
    E=0
    for i,s in enumerate(r):
        E+=np.linalg.norm(s)**2
        for j,t in enumerate(r):
            if i!=j:
                rij=np.linalg.norm(s-t)
                E+=1/2/rij
    return E

Np=26
T0=5
R=1


Ntimes=10000
dt=0.01

file_name=f'{Np}_{Ntimes}_{dt}.txt'

r=np.random.rand(Np,2)*R
r_prima=r.copy()
n_accept=0
T=T0
with open(file_name,'w') as f:
    E_0=Energy_Coulomb(r)
    f.write(f'{0}'+'\t'+f'{E_0}'+'\n')
    for m in tqdm(range(Ntimes)):
        T=T*0.995
        for n in range(Np):
            u=np.random.rand(2)
            r_prima[n]=r[n]+dt*(2*u-[1,1])
        E_prima=Energy_Coulomb(r_prima)
        E_0=Energy_Coulomb(r)
        deltaE=E_prima-E_0
        if deltaE<=0:
            r[:,:]=r_prima[:,:]
            n_accept+=1
            f.write(f'{m+1}'+'\t'+f'{E_prima}'+'\n')
        else:
            p=np.exp(-deltaE/T)
            u=random.uniform(0,1)
            if u<p:
                r[:,:]=r_prima[:,:]
                n_accept+=1
                f.write(f'{m+1}'+'\t'+f'{E_prima}'+'\n')
            else:
                f.write(f'{m+1}'+'\t'+f'{E_0}'+'\n')
    f.write('\n')
    for n in range(Np):
        f.write(f'{r[n,0]}'+'\t'+f'{r[n,1]}'+'\n')
    f.write('\n'+f'{T0}'+'\t'+f'{T}'+'\t'+f'{n_accept/Ntimes}')
print(n_accept/Ntimes)
print(T)


