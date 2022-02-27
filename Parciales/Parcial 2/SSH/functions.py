import random, math
import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm

J = 1

def energy(S, N, h, nbr):
        E = 0.0
        for k in range(N):
            # La energía corresponde a la interacción del espín con cada uno de sus vecinos próximos
            E = -J * S[k] * sum(S[nn] for nn in nbr[k]) - S[k]*h
        return 0.5 * E

def evolucion(S, L, T, h):
    # Función que calcula la energía total del sistema

    N = L*L
    # Da los vecinos próximos de cada espín i
    nbr = {i: ((i//L) * L + (i + 1) % L, (i + L) % N,
               (i//L) * L + (i - 1) % L, (i - L) % N) \
                                      for i in range(N)}
    
    # Temperatura
    beta = 1.0 / T
    # S = [1 for k in range(N)]
    
    S_ini = np.copy(S)
    # S_mat_ini = np.reshape(S, (L,L))

    # Número de pasos
    nsteps = N * 100
    Energy = energy(S, N, h, nbr)

    E = np.zeros(nsteps)

    for step in range(nsteps):
        k = np.random.randint(0, N-1)
        delta_E = J * 2.0 * S[k] * sum(S[nn] for nn in nbr[k]) + 2 * S[k] * h
        if np.random.uniform(0.0, 1.0) < np.exp(-beta * delta_E):
            S[k] *= -1
            Energy += delta_E
        E[step] = Energy

    # S_mat_end = np.reshape(S, (L,L))
    S_end = np.copy(S)

    M = np.sum(S_end)/N
    X = beta * (sum(S_end**2)/N - M**2)
    
    
    return S_end, M, X
