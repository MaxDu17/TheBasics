import matplotlib.pyplot as plt
import numpy as np

def f(x, y):
    return np.sin(np.sqrt(x ** 2 + y ** 2))

x = np.linspace(-6, 6, 30)
y = np.linspace(-6, 6, 30)

X, Y = np.meshgrid(x, y)
Z = f(X, Y)

fig = plt.figure()
ax = plt.axes(projection='3d')

#### A VAREITY OF DIFFERENT STYLE OF PLOTS
# ax.plot_wireframe(X, Y, Z, color='black')
# ax.contour3D(X, Y, Z, stride = 50, cmap='binary')
ax.plot_surface(X, Y, Z, rstride=1, cstride=1,
                cmap='viridis', edgecolor='none')
# ax.scatter(X, Y, Z, c=Z, cmap='viridis', linewidth=0.5)
#this one requires X, Y, and Z to be 1d arrays
# ax.plot_trisurf(X, Y, Z,
#                 cmap='viridis', edgecolor='none')

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

plt.show()