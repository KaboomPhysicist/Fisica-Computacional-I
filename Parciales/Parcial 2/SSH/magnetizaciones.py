import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from tqdm import tqdm

from functions import evolucion

hn = 200
H = np.linspace(-6, 6, hn)
T = [1, 2, 2.5, 3, 5]

L = 128
init = [np.random.choice([1, -1]) for k in range(L*L)]

dict_magnetization = {}

plt.figure(figsize=(16,9))

font = {'family' : 'Times New Roman',
        'size'   : 20}

matplotlib.rc('font', **font)


plt.title("Magnetización en función del campo externo")
plt.xlabel("Campo Externo H")
plt.ylabel("Magnetización M")

for i in T:
    S = init
    M = np.zeros(hn)
    c = 0
    for j, k in tqdm(enumerate(H)):
        s, m, x = evolucion(S, L, i, k)
        M[j] = m
    
    dict_magnetization[i] = M
        
    plt.plot(H, M, linestyle='--', marker='.',label = f"T = {i:.1f}")
    
df = pd.DataFrame(dict_magnetization)
df.to_csv('raw_data/magnetizaciones.csv')

    
plt.grid()
plt.legend()
plt.savefig('imgs/magnetizaciones.png')
