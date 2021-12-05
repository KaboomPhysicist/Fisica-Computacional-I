import numpy as np
import matplotlib.pyplot as plt
from Euler import euler
from Euler_improved import euler_improved
from RK4 import rk4

l = np.log(2)/(8*24*60*60)
f = lambda y: -l*y

f_teo = lambda t: 10*np.exp(-l*t)

t1,N1 = euler(f, [0,10], 40*24*60*60, 4)
t2,N2 = euler_improved(f, [0,10], 40*24*60*60, 4)
t3,N3 = rk4(f, [0,10], 40*24*60*60, 4)

plt.plot(t1,N1, label = 'Euler')
plt.plot(t2,N2, label = 'Euler Improved')
plt.plot(t3,N3, label = 'RK4')
plt.plot(t1,f_teo(t1), label = 'Curva analítica')
plt.legend()
plt.show()