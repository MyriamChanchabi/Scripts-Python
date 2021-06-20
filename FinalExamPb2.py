
#Problem 2

import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
def Gauss(x,*p):
    A, mu, sigma=p
    return A*np.exp(-(x-mu)**2/(2.*sigma**2))

#Gaussian fitting
#School A
score=np.linspace(1,50,50)
numberA=np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,4,10,13,11,17,14,15,5,2,2,1,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
m=np.sum(score*numberA)/sum(numberA)
sig=np.sqrt(sum(numberA * (score - m) ** 2) / sum(numberA))
start1=(17,m,sig)
popt,pcov=curve_fit(Gauss,score,numberA,p0=start1,absolute_sigma=True)
MeanA=popt[1]
sigmaA=popt[2]
print("The average score(mean) for school A is=",MeanA)
print("The sigma for school A is=",sigmaA)
print("\n")
A=Gauss(score,*popt)
plt.plot(score,A,'r--',label="Gaussian fit for school A")
plt.plot(score,numberA,'c',label="Data Points for School A")

#School B
numberB=np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,1,2,2,9,8,12,14, 11, 17, 6, 6, 2, 4, 2, 1, 1, 0, 0, 0, 0, 0, 0])
m=np.sum(score*numberB)/sum(numberB)
sig=np.sqrt(sum(numberB * (score - m) ** 2) / sum(numberB))
start2=(17,m,sig)
poptt,pcovv=curve_fit(Gauss,score,numberB,p0=start2,absolute_sigma=True)
MeanB=poptt[1]
sigmaB=poptt[2]
print("The average score(mean) for school B is=",MeanB)
print("The sigma for school B is=",sigmaB)
print("\n")
B=Gauss(score,*poptt)
plt.plot(score,B,'m--',label="Gaussian fit for school B")
plt.plot(score,numberB,'g',label="Data Points for School B")
plt.legend()
plt.xlabel("Scores")
plt.ylabel("Number of students")
plt.grid(True)
plt.show()