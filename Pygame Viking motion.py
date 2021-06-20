import pygame
from math import *
import numpy as np 
import numpy.linalg as npl
import sys

#Simulation of the Viking attraction in amusement parks

def G(t,y):
   F[0]=-g*np.sin(y[1])+(F0/m)*np.cos(w*t)-(f/m)*y[0]
   F[1]=y[0]
   return inv_L.dot(F)
def RK4(t,y,delta):
    k1= G(t,y)
    k2=G(t+delta*0.5 , y+0.5*delta*k1)
    k3=G(t+delta*0.5 , y+0.5*delta*k2)
    k4=G(t+delta*0.1 , y+1*delta*k3)
    return 1/6 *k1 + 2/6 *k2 + 2/6 *k3 + 1/6 *k4 
def position(angle):
    x=l*sin(angle)+x_center
    y=l*cos(angle)+y_center
    return (x,y)
def render(pos_xy):
    screen.fill(white)
    pygame.draw.line(screen,'black',(x_center,y_center),(pos_xy[0],pos_xy[1]),2)
    pygame.draw.circle(screen,red,(pos_xy[0],pos_xy[1]),15)
    
    

#variables
g=9.8
F0=500
f=50 #low friction coefficient
m=1000 #1000 kilograms
ll=20 #20 meters
w=0.7  #in our case, the resonance pulsation is equal to the driving pulsation
delta=0.03
t=0

#initial conditions
y=np.array([0.0,0.0])
L=np.array([[ll,0.0],[0.0,1.0]])
F=np.array([0.0,0.0])
inv_L=npl.inv(L)
width=600
height=400
clock=pygame.time.Clock()
l=150

x_center=width*0.5
y_center=height*0.3
screen=pygame.display.set_mode((width,height))
red=pygame.Color('red')
white=pygame.Color('white')
screen.fill(white)

pygame.display.update()
count=0
while True:  #1.51mins ride
    count=count+1
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
    #update
    xy=position(y[1])
    render(xy)

    t=t+delta
    y=y+delta*RK4(t,y,delta)

    render(xy)
    clock.tick(100)
    pygame.display.update()
   