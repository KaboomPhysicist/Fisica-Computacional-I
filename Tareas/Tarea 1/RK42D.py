import numpy as np
import matplotlib.pyplot as plt

def RK42D(f, u0, tiempo, h):
    """
    f: función de segundo orden a integrar
    u0: tupla, array o lista. u0[0] Tiempo inicial, u0[1:] Condiciones iniciales
    tiempo: tiempo final
    h: paso de integración
    """

    T = np.arange(u0[0], tiempo, h)
    # Declara un array con 2 columnas, una para cada orden de derivación
    U = np.zeros((len(T),2))

    # Primera fila con condiciones iniciales
    U[0] = u0[1:]

    # Aplica RK4 con caracter vectorial
    for i in range(len(T)-1):
        k1 = f(T[i],U[i])
        k2 = f(T[i], U[i] + h*k1/2)
        k3 = f(T[i], U[i] + h*k2/2)
        k4 = f(T[i], U[i] + h*k3)
        U[i+1] = U[i] + h*(k1 + 2*k2 + 2*k3 + k4)/6
    
    return T, U


if __name__ == '__main__':
    gamma = 0.15
    a = -1
    b = 1
    omega = 1.2

    F = 0.15

    Fuerzas = [0.15, 0.20, 0.37, 0.50, 0.65]

    def f(t, u):
        f1 = u[1]
        f2 = -2*gamma*f1 - a*u[0] - b*u[0]**3 + F*np.cos(omega*t)

        return np.array([f1, f2])


    for i in Fuerzas:
        F = i
        T, U = RK42D(f, np.array([1, 0]), 40*np.pi/omega, 0.1)
        plt.plot(U[:,0], U[:,1], label = '$F = {}$'.format(F))

    plt.legend()
    plt.show()
