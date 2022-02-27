import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

from tqdm import tqdm
from functions import evolucion

hnn = 100

H_normal = np.linspace(-4, 4, hnn)

# Array con campo desde -6 hasta 6 y de vuelta
H_histeresis = np.concatenate((H_normal, H_normal[::-1]))

L = 64
S = [np.random.choice([1, -1]) for k in range(L*L)]

M_Histeresis = np.zeros(2*hnn)

for i, j in tqdm(enumerate(H_histeresis)):
    # Escojemos temperatura = 2
    s, m, x = evolucion(S, L, 2, j)
    M_Histeresis[i] = m

dict_histeresis = {'Campo' : H_histeresis, "Magnetización" : M_Histeresis}
df_histeresis = pd.DataFrame(dict_histeresis)
df_histeresis.to_csv('raw_data/histeresis.csv')

plt.figure(figsize = (16,9))

font = {'size'   : 20}

matplotlib.rc('font', **font)

plt.title("Ciclo de histéresis")
plt.xlabel("Campo magnético externo H")
plt.ylabel("Magnetización M")


plt.plot(H_histeresis[:hnn], M_Histeresis[:hnn], linestyle='--', marker='.',label = "H creciente T = 2.0" )
plt.plot(H_histeresis[hnn:], M_Histeresis[hnn:], linestyle='--', marker='.',label = "H decreciente T = 2.0" )
plt.axvline(0, color = 'b')
plt.axhline(0, color = 'b')
plt.legend()
plt.grid()

plt.savefig('imgs/histeresis_short_range.png')
