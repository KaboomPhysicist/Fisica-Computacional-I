from tkinter import font
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

path = 'raw_data/transicion_Lvar.csv'
file = pd.read_csv(path)

df = pd.DataFrame(file)

T = np.linspace(1,4, 50)

plt.figure(figsize=(16,9))

font = {'family': 'serif',
        'size': 20}

matplotlib.rc('font', **font)

plt.title("Magnetización en función de la temperatura")
plt.xlabel("Temperatura T")
plt.ylabel("Magnetización M")

for i in df.columns.values[1:]:
    plt.plot(T, df[i], label=f"Lado de red L = {float(i):.2f}")

plt.grid()
plt.legend()
plt.savefig("imgs/transicion_Lvar.png")
plt.show()