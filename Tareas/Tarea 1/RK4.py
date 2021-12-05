import numpy as np
import matplotlib.pyplot as plt

def rk4(f, inicio, tiempo, h):
    T = np.arange(inicio[0], tiempo, h)
    Y = np.zeros(len(T))
    Y[0] = inicio[1]
    for i in range(len(T)-1):
        k1 = f(Y[i])
        k2 = f(Y[i] + h*k1/2)
        k3 = f(Y[i] + h*k2/2)
        k4 = f(Y[i] + h*k3)
        Y[i+1] = Y[i] + h*(k1 + 2*k2 + 2*k3 + k4)/6
    
    return T, Y

if __name__ == "__main__":
    l = np.log(2)/(8*24*60*60)
    f = lambda y: -l*y

    t,N = rk4(f, [0,10], 40*24*60*60, 4)
    plt.plot(t,N)
    plt.show()