#!/usr/bin/env python3

import sympy as s
import numpy as np
from sympy.codegen.ast import Print
import matplotlib.pyplot as plt

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

# Calculates Jacobian matrix
def Jacobian(T):
    T1 = [0,0,0,0,0,0]
    T1[0]= s.simplify(T[0])
    T1[1]= s.simplify(T[0] * T[1])
    T1[2]= s.simplify(T[0] * T[1] * T[2])
    T1[3]= s.simplify(T[0] * T[1] * T[2] * T[3])
    T1[4]= s.simplify(T[0] * T[1] * T[2] * T[3] * T[4])
    T1[5]= s.simplify(T[0] * T[1] * T[2] * T[3] * T[4] * T[5])
    
    Z = [0,0,0,0,0,0,0]
    Z[0] = s.Matrix([[0], [0], [1]])
    Z[1] = s.Matrix([[T1[0].col(-2)[0]], [T1[0].col(-2)[1]], [T1[0].col(-2)[2]]])
    Z[2] = s.Matrix([[T1[1].col(-2)[0]], [T1[1].col(-2)[1]], [T1[1].col(-2)[2]]])
    Z[3] = s.Matrix([[T1[2].col(-2)[0]], [T1[2].col(-2)[1]], [T1[2].col(-2)[2]]])
    Z[4] = s.Matrix([[T1[3].col(-2)[0]], [T1[3].col(-2)[1]], [T1[3].col(-2)[2]]])
    Z[5] = s.Matrix([[T1[4].col(-2)[0]], [T1[4].col(-2)[1]], [T1[4].col(-2)[2]]])
    Z[6] = s.Matrix([[T1[5].col(-2)[0]], [T1[5].col(-2)[1]], [T1[5].col(-2)[2]]])

    P = [0,0,0,0,0,0,0]
    P[0] = s.Matrix([[0], [0], [0]])
    P[1] = s.Matrix([[T1[0].col(-1)[0]], [T1[0].col(-1)[1]], [T1[0].col(-1)[2]]])
    P[2] = s.Matrix([[T1[1].col(-1)[0]], [T1[1].col(-1)[1]], [T1[1].col(-1)[2]]])
    P[3] = s.Matrix([[T1[2].col(-1)[0]], [T1[2].col(-1)[1]], [T1[2].col(-1)[2]]])
    P[4] = s.Matrix([[T1[3].col(-1)[0]], [T1[3].col(-1)[1]], [T1[3].col(-1)[2]]])
    P[5] = s.Matrix([[T1[4].col(-1)[0]], [T1[4].col(-1)[1]], [T1[4].col(-1)[2]]])
    P[6] = s.Matrix([[T1[5].col(-1)[0]], [T1[5].col(-1)[1]], [T1[5].col(-1)[2]]])
    
    J1 = cross(Z[0],P[6] - P[0])
    J2 = cross(Z[1],P[6] - P[1])
    J3 = cross(Z[2],P[6] - P[2])
    J4 = cross(Z[3],P[6] - P[3])
    J5 = cross(Z[4],P[6] - P[4])
    J6 = cross(Z[5],P[6] - P[5])

    J11 = [J1, J2, J3, J4, J5, J6]
    J12 = [Z[0], Z[1], Z[2], Z[3], Z[4], Z[5]]
    j1 = [0,0,0,0,0,0]
    j2 = [0,0,0,0,0,0]
    j3 = [0,0,0,0,0,0]
    j4 = [0,0,0,0,0,0]
    j5 = [0,0,0,0,0,0]
    j6 = [0,0,0,0,0,0]
    J = [j1,j2,j3,j4,j5,j6]
    for i in range(3):
        for j in range(6):
            J[i][j] = J11[j][i]
    for i in [3,4,5]:
        for j in range(3):
            for k in range(6):
                J[i][j] = J12[k][j]
    return s.Matrix(J)

# Calculates Jacobian Inverse
def Jacobian_inv(J):
    return J.pinv()

d1 = 0.2
d2 = 0.41
d3 = 0.25
d4 = 0.355
d5 = 0.25 
d = [d1,0,0,d3+d4,0,0]

al = [-s.pi/2,0,s.pi/2,-s.pi/2,0, 0]
a = [0,d2,0,0,d5, 0]

t = 5.0     #Total Time
n = 100.0     #No. of parts
xc = 0    #Center coordinates of the circle
yc = 0
r = 0.66 
q_old = [0.0,0.0,0.0,0.0,0.0,0.0]
x_old = xc + r
y_old = 0
for i in np.linspace(0,180,n):
    x_new = (xc+r*np.cos((np.pi/180)*(i)))
    y_new = (yc+r*np.sin((np.pi/180)*(i)))
    plt.scatter(y_new, x_new, s=10, c="red", alpha=0.5)
    
    pos_diff = s.Matrix([(x_new-x_old),(y_new-y_old),0.0,0.0,0.0,0.0])
    
    x_old = x_new       #Updating the position
    y_old = y_new
    
    J = Jacobian(Transformation(q_old,d,al,a))
    J_in = Jacobian_inv(J)

    q_dot = J_in*pos_diff
    q_new = [0,0,0,0,0,0]

    q_new[0] = q_old[0] + q_dot[0]
    q_old[0] = q_new[0]
        
    q_new[1] = q_old[1] + q_dot[1]
    q_old[1] = q_new[1]

    q_new[2] = q_old[2] + q_dot[2]
    q_old[2] = q_new[2]
        
    q_new[3] = q_old[3] + q_dot[3]          #Calculating new joint angles using Inverse Kinematics
    q_old[3] = q_new[3]
        
    q_new[4] = q_old[4] + q_dot[4]
    q_old[4] = q_new[4]

    q_new[5] = q_old[5] + q_dot[5]
    q_old[5] = q_new[5]

    T_new = Transformation(q_new,d,al,a)
    T = T_new[0]*T_new[1]*T_new[2]*T_new[3]*T_new[4]*T_new[5]
    new_pos = s.Matrix([[T.col(-1)[0]], [T.col(-1)[1]], [T.col(-1)[2]]])

    plt.scatter(new_pos[1], new_pos[0], s=10, c="blue", alpha=0.5)      #Circle drawn by robot
    # plt.pause(0.05)
plt.xlim(-0.7,0.7)
plt.ylim(-0.7,0.7)
plt.xlabel("y-axis (m)")
plt.ylabel("x-axis (m)")
plt.show()