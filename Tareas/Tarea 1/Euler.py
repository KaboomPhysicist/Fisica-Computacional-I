import numpy as np
import matplotlib.pyplot as plt


def euler(f, inicio, tiempo, h):
    
    """
    f: función de la derivada
    inicio: array, tupla o lista con las condiciones iniciales. El primer elemento corresponde
    al tiempo inicial.
    tiempo: float, tiempo final
    h: paso
    """

    T = np.arange(0, tiempo, h)
    X = np.zeros(len(T))
    Y = np.zeros(len(T))

    X[0] = inicio[0]
    Y[0] = inicio[1]

    for i in range(len(T)-1):
        Y[i+1] = Y[i] + h*f(Y[i])

    return T, Y

if __name__ == "__main__":
    l = np.log(2)/(8*24*60*60)
    f = lambda y: -l*y

    t,N = euler(f, [0,10], 40*24*60*60, 4)
    plt.plot(t,N)
    plt.show()


