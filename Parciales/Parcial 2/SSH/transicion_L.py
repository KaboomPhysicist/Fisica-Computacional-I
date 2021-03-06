import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd

from functions import evolucion
from transicion import transition

from tqdm import tqdm

if __name__ == "__main__":

    h = 0
    L = [8, 32, 64, 128]

    dict_L = {}
    
    for i in tqdm(L):

        S = [1 for k in range(i*i)]
        
        plt.figure(1, figsize=(16,9))
        M = transition(S, i, h)

        dict_L[i] = M

    df_L = pd.DataFrame(dict_L)

    df_L.to_csv('raw_data/transicion_Lvar.csv')

    font = {'size' : 20}

    matplotlib.rc('font', **font)

    plt.grid()
    plt.savefig('imgs/transicion_Lvar.png')
