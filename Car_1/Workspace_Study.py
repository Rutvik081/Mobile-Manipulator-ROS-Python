#!/usr/bin/env python3

import sympy as s
import numpy as np
from sympy.codegen.ast import Print
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d


# Cross Product of two vectors
def cross(n1,n2):
    return [n1[1]*n2[2]-n1[2]*n2[1],n1[2]*n2[0]-n1[0]*n2[2],n1[0]*n2[1]-n1[1]*n2[0]]

# Calculates transformation matrices
def Transformation(q,d,al,a):
    T = []
    for i in range(len(q)):
        Ti = s.Matrix([[s.cos(q[i]),-s.sin(q[i])*s.cos(al[i]),s.sin(q[i])*s.sin(al[i]),a[i]*s.cos(q[i])],
                        [s.sin(q[i]),s.cos(q[i])*s.cos(al[i]),-s.cos(q[i])*s.sin(al[i]),a[i]*s.sin(q[i])],
                        [0,s.sin(al[i]),s.cos(al[i]),d[i]],
                        [0,0,0,1]])
        T.append(Ti)
    return T

d1 = 0.2
d2 = 0.41
d3 = 0.25
d4 = 0.355
d5 = 0.25 
d = [d1,0,0,d3+d4,0]

al = [-s.pi/2,0,s.pi/2,-s.pi/2,0]
a = [0,d2,0,0,d5]
q_old = [0.0,-s.pi/2,s.pi/2,0.0,-s.pi/2]

fig = plt.figure()
ax = plt.axes(projection="3d")
X = []
Y = []
Z = []
for i in np.linspace(-2.8973,2.8973,50):
    for j in np.linspace(-1.7628,1.7628,50):
        q_old[0] = i
        q_old[1] = j - s.pi/2
        T = Transformation(q_old,d,al,a)
        T_end = T[0]*T[1]*T[2]*T[3]*T[4]
        P = s.Matrix([[T_end.col(-1)[0]], [T_end.col(-1)[1]], [T_end.col(-1)[2]]])
        X.append(P[0])
        Y.append(P[1])
        Z.append(P[2])
ax.plot3D(X, Y, Z, 'blue')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.show()
