import random
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


X1 = []
X2 = []
Y1 = []
Y2 = []
Z1 = []
Z2 = []

steps = []
V = []
frac_error = []

def monte_carlo(a1, a2, b1, b2, c1, c2, ellipsoid, N,analyt_val):
    j = 0
    vol_box = (a2 - a1) * (b2 - b1) * (c2 - c1)
    vol_ellipsoid = 0
    sum_fx = 0
    point_inside = 0
    for i in range(N):
        x = random.uniform(a1, a2)
        y = random.uniform(b1, b2)
        z = random.uniform(c1, c2)

        if (ellipsoid(x, y, z) <= 1):
            X1.append(x)
            Y1.append(y)
            Z1.append(z)
            point_inside = point_inside +1

        else:
            X2.append(x)
            Y2.append(y)
            Z2.append(z)
        if (i % 100) == 0 and i != 0: #for plotting on every 100 steps
            vol_ellipsoid = (vol_box/float(i)) *point_inside
            steps.append(i)
            V.append(vol_ellipsoid)
            frac_err = abs(vol_ellipsoid - analyt_val) / analyt_val
            frac_error.append(frac_err)
    vol_ellipsoid = (vol_box/float(N)) * point_inside

    return vol_ellipsoid,frac_error

def ellipsoid(x,y,z):
    return ((x**2)/(1**2))+((y**2)/(1.5**2))+((z**2)/(2**2))

N = 30000
analyt_val = 12.56637
volume ,frac_error = monte_carlo(-1,1,-1.5,1.5,-2,2,ellipsoid,N,analyt_val)

print("Volume = ", volume)
print("Actual volume = 12.56637")

plt.figure()
plt.plot(steps, V)
plt.axhline(12.56637, color='r')
plt.title("Comparison between Analytical value and ellipsoid")
plt.xlabel("Steps")
plt.ylabel("Volume of ellipsoid")



plt.figure()
plt.plot(steps,frac_error)
plt.title("Plot for Steps vs Fractional error")
plt.xlabel("Steps")
plt.ylabel("Fractional Error")



fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(X1, Y1, Z1)
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()



"""
/home/tamoghna/anaconda3/envs/Pycharm_py/bin/python /home/tamoghna/PycharmProjects/pythonProject/q2.py
Volume =  12.576
Actual volume = 12.56637

"""