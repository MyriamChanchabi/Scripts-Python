import numpy as np
import matplotlib.pyplot as plt

F=np.array([2,4,6,8,10,12,14,16,18,20,22])
L=np.array([15,32,49,64,79,98,112,126,149,175,190])
L=L/1000

min=9999

for a in range(500,1500,1):
    a= a/200000.
    
    for b in range(-50,150,1):
        b=b/30000.

        s=0
        for i in range(11):
            x=2*(i+1)
            ff=a*x*+b
            s=s+(L[i]-ff)*(L[i]-ff)
            print(s)

            if(s<min):
                min=s
                print(a,b,1./a,-b/a,s)
k=1./a
print("the spring constant k is=",k)
F105=k*0.105 - b/a
print("For L=105mm, the force is ",F105)

plt.plot(F,L,'m',label='Data')
plt.plot(F,a*F+b,label='Best least-square fitting')
plt.xlabel("Applied force(N)")
plt.ylabel("Extension of the spring(m)")
plt.title("Extension of the spring versus the applied force")
plt.legend()
plt.grid(True)
plt.show()
# Answer to question (c)
#Although the least-square method is a good approximation of the real data model, not all the points intersect with the best fitting
#straight line, therefore we should ignore some of the data points