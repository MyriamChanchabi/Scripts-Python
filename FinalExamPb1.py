
#Problem 1
# Plotting is written at the end of the code and answers and detailed in the PDF file

import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from math import gamma, inf
from scipy.integrate import quad

Days=np.linspace(0,24,25)
Infected=np.array([575,626,575,566,532,574,579,577,633,524,553,561,588,535,491,538,495,537,528,533,543,505,508,494,480])
error=np.sqrt(Infected)
def func(x,nu):
    norm=pow(2,nu/2)*gamma(nu/2)
    powe=np.power(x,nu/2 -1)
    expo=np.exp(-x/2)
    return (1/norm)*powe*expo

#Fitting
#Constant function fitting
def f(Days,a):
    return np.zeros(25)+a
a=500
A=f(Days,a)
start=20
popt,pcov=curve_fit(f,Days,Infected,sigma= error, p0 =start, absolute_sigma=True)
perr=np.sqrt(np.diag(pcov))
print("The constant model function is f=",popt)
print("The error on this parameter is=",perr)
model1=f(Days,*popt)
chisq=np.sum((Infected-model1)**2/error**2)
pval1=quad(func,chisq,+inf,args=24)
print("Best fit chi-square value for the constant model is=",chisq)
print("The p-value for the constant model is=",pval1[0])
print("\n")
#The constant model has a p-value of approximately 3x10^(-6), this means that if we repeat the experiment, chi square>68.7375... happens with 0.0003% chance
#This rarely happens in nature and therefore this model is rejected.

#Linear function fitting
def g(Days,b,c):
    return np.zeros(25)+ b*Days + c
b=0
c=500
B=g(Days,b,c)
start2=(1,1)
poptt,pcovv= curve_fit(g,Days, Infected, sigma=error, p0=start2, absolute_sigma=True)
perrr=np.sqrt(np.diag(pcovv))
print("The linear model function has parameters b and c respectively equal to",poptt[0],poptt[1])
print("The respective errors on each parameter are=",perrr[0], perrr[1])
model2=g(Days,poptt[0],poptt[1])
chisq2=np.sum((Infected-model2)**2/error**2)
pval2=quad(func,chisq2,+inf,args=23)
print("Best fit chi-square value for the linear model is=",chisq2)
print("The p-value for the linear model is=",pval2[0])
print("\n")
#The p-value for the linear model is 11%, which means that if we repeat the experiment, chi square>31.22129737249933 happens with 11% chance
#This can happen in nature, and this model is acceptable

#Quadratic function fitting
def h(Days,d,e,k):
    return np.zeros(25)+ d*Days*Days + e*Days+ k
d=0
e=0
k=400
C=h(Days,d,e,k)
start3=(1,1,1)
popttt,pcovvv= curve_fit(h,Days, Infected, sigma=error, p0=start3, absolute_sigma=True)
perrrr=np.sqrt(np.diag(pcovvv))
print("The quadratic model function has parameters d, e  and k respectively equal to",poptt[0],poptt[1],popttt[2])
print("The respective errors on each parameter are=",perrrr[0], perrrr[1],perrrr[2])
model3=h(Days,popttt[0],popttt[1],popttt[2])
chisq3=np.sum((Infected-model3)**2/error**2)
pval3=quad(func,chisq3,+inf,args=22)
print("Best fit chi-square value for the quadratic model is=",chisq3)
print("The p-value for the quadratic model is=",pval3[0])
#The p-value for the linear model is 9%, which means that if we repeat the experiment, chi square>31.22129737249933 happens with 9% chance
#This can happen in nature, and this model is acceptable

plt.plot(Days,Infected,'m',label="Data points")
plt.errorbar(Days,Infected,error,fmt='o')
plt.plot(Days,model1,'r',label="Constant function model")
plt.plot(Days,model2,'g',label="Linear function model")
plt.plot(Days,model3,'orange', label="Quadratic function model")
plt.legend()
plt.xlabel("Number of days")
plt.ylabel("Number of cases")
plt.title("Number of cases versus number of days")
plt.grid(True)
plt.show()
#Conclusion:
#Out of the 3 models, the constant model is rejected because it is not a good description for the data, the linear and the quadratic models are acceptable.
#The number of infected people from COMPS-21 virus can grow linearly or quadratically with time.