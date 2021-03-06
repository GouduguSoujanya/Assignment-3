# -*- coding: utf-8 -*-
"""Untitled25.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11ty1iRQyJJTCvd1SS-K2iKDPHGDDjQL3
"""

from mpl_toolkits.mplot3d.axes3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
a = np.array([1, -2, 0])
b = np.array([2, 1, 1])
theta = np.arccos(np.dot(a,b)/(np.linalg.norm(a)*np.linalg.norm(b)))
print("Angle between the two line in degrees is:")
print(np.degrees(theta))
 
fig = plt.figure()
ax = plt.axes(projection='3d')
 
ax.set_xlim(-5,5)
ax.set_ylim(-5,5)
ax.set_zlim(-5,5)
 
ax.set_xlabel('x-axis')
ax.set_ylabel('y-axis')
ax.set_zlabel('z-axis')
 
# Line 1 equation
t = np.linspace(-2,10)
x=(t)+3
y = -2*t +5
z = -1
 
ax.plot3D(x,y,z,label = "L1",color='r')
 
# Line 2 equation
x1=2*t
y1 = t
z1 = t
ax.plot3D(x1,y1,z1,label = "L2",color='g')
plt.legend()
plt.savefig("lines.png")
plt.show()