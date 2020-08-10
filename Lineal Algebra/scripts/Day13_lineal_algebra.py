import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x, y = np.linspace(-8,8,100), np.linspace(-8,8,100)
X, Y = np.meshgrid(x,y)
Z1 = 11 - 4*X + 2*Y
Z2 = (16 - 2*X + 4*Y) / 2
Z3 = (17 - X + 2*Y) / 4

ax.plot_surface(X,Y,Z1, alpha=0.5, rstride=100, cstride=100)
ax.plot_surface(X,Y,Z2, alpha=0.5, rstride=100, cstride=100)


ax.plot((1,1),(-8,8),(-9,23), lw=2, c='b')
ax.plot_surface(X,Y,Z3, alpha=0.5, facecolors='g', rstride=100, cstride=100)
ax.plot((1,),(-2,),(3,), lw=2, c='k', marker='o')

plt.show()

 
x = np.linspace(-6, 6, 100) 
y1 = (5 - 2*x) / 2
y2 = (3 - 3*x) / 2

  
fig = plt.figure(figsize = (10, 5)) 
# Create the plot 
plt.plot(x, y1, label=r'$2x + 4y = 5$') 
plt.plot(x, y2, label=r'$3x + 2y = 3$')
plt.plot(-2,4.5,'ko') 


plt.grid(True) 
plt.xlim([-6, 6]) 
plt.ylim([-2, 6]) 
plt.xlabel('X')
plt.ylabel('Y')
# Show the plot 
plt.legend()
plt.show() 