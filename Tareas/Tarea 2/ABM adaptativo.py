import numpy as np
import matplotlib.pyplot as plt

def rk4(f, inicio, tiempo, h):
    """
    Soluciona una ecuación diferencial de una variable por el método de Runge-Kutta de 
    cuarto orden.
    f: función de la derivada
    inicio: array, tupla o lista con las condiciones iniciales. El primer elemento corresponde
    al tiempo inicial.
    tiempo: float, tiempo final
    h: paso
    """
    
    T = np.arange(inicio[0], tiempo, h)
    Y = np.zeros(len(T))
    Y[0] = inicio[1]
    
    # Aplica Runge-Kutta de orden 4
    for i in range(len(T)-1):
        # Define los coeficientes
        k1 = f(Y[i])
        k2 = f(Y[i] + h*k1/2)
        k3 = f(Y[i] + h*k2/2)
        k4 = f(Y[i] + h*k3)
        # Calcula el resultado final
        Y[i+1] = Y[i] + h*(k1 + 2*k2 + 2*k3 + k4)/6
    
    return T, Y

def abm_ada(f, inicio, tiempo, h0):
    """
    Soluciona una ecuación diferencial de una variable por un método predictor-corrector
    basado en una predicción por Adams-Bashforth y una corrección por Adams-Moulton. 
    El paso es adaptativo.
    f: función de la derivada
    inicio: array, tupla o lista con las condiciones iniciales. El primer elemento corresponde
    al tiempo inicial.
    tiempo: float, tiempo final
    h: paso
    """
    
    T = np.zeros(4)
    Y = np.zeros(len(T))
    Y[0] = inicio[1]
    
    Tol = 1e-5
    hmax = 1
    hmin = 1e-5
    
    #Determinamos los siguientes 3 pasos haciendo uso de RK4
    h = h0
    
    i = 0
    iterations = 0
    
    while T[i]<tiempo:
        
        T[i:i+4],Y[i:i+4] = rk4(f, [T[i],Y[i]], 4*h, h)
        
        w4p = Y[i]+h/24*(55*f(Y[i])-59*f(Y[i-1])+37*f(Y[i-2])-9*f(Y[i-3]))
        w4c = Y[i]+h/24*(9*f(w4p)+19*f(Y[i])-5*f(Y[i-1])+f(Y[i-2]))
        
        eps = 19/(270*h)*abs(w4p-w4c)
        
        
        if eps<Tol:
            print(h)
            Y = np.append(Y, w4c)
            T = np.append(T, T[i]+h)
            i += 1

        
        q = (Tol/(2*eps))**(1/4)
        
        if (q <= 0.1): h = 0.1*h   # (error grande) 0.1 es el mínimo valor impuesto para q
        elif (q >= 5): h = 5.*h    # 5 es el máximo valor impuesto para q
        else:          h = q*h  
        
        
        if h > hmax:
            h = hmax
        elif h < hmin:
            print(h,"hmin excedido")
            break
        
        iterations+=1
        #if iterations>200000:
        #    break
        
    return T, Y

k = 0.0009906
f = lambda x: k*x*(1000-x)

def analitica(t):
    return 1000/(1+999*np.exp(-1000*k*t))

def main():
    tada, yada = abm_ada(f, [0,1], 13, 1)
    yt = analitica(tada)

    plt.figure(figsize=(16,9), dpi=200)
    plt.title("Número de estudiantes infectados en función del tiempo")
    plt.xlabel("Tiempo (días)")
    plt.ylabel("Número de infectados")
    plt.grid()

    plt.plot(tada, yt, label="Analítica")
    plt.plot(tada, yada, '.', label = "Adaptativo")

    plt.legend()

if __name__=="__main__":
    main()