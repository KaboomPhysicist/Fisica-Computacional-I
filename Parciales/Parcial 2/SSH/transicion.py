import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd

from tqdm import tqdm
from functions import evolucion

def transition(S, L, h):
    N_sep = 50
    T = np.linspace(1, 4, N_sep)
    
    M = np.zeros(N_sep)
    
    for i,j in enumerate(T):
        s, m, x = evolucion(S, L, j, h)
        M[i] = abs(m)
    
        
    plt.title("Magnetización en función de la temperatura")
    plt.xlabel("Temperatura T")
    plt.ylabel("Magnetización M")
    plt.plot(T, M, label = f'Campo externo H = {h:.2f} L = {L: .2f}')
    
    plt.legend()
    plt.grid()

    return M
    
if __name__ == '__main__':
    L = 128
    S = [1 for k in range(L*L)]

    H = [0, 0.1, 0.5, 1, 2]

    dict_tr = {}
    
    for i in tqdm(H):
        plt.figure(1, figsize=(16,9))
        M = transition(S, L, i)

        dict_tr[i] = M

    df_tr = pd.DataFrame(dict_tr)
    df_tr.to_csv('raw_data/transicion.csv')
    
    font = {'family' : 'Times New Roman',
        'size'   : 20}

     
  
    matplotlib.rc('font', **font)    

    plt.grid()
    plt.savefig('imgs/transition.png')
