import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style='whitegrid')

t = np.linspace(0, 2*np.pi, 200)
x = 16 * np.sin(t)**3
y = 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)

plt.plot(x, y, 'r-')
plt.text(0, 0, 'bootcamp', fontsize=36, ha='center')
plt.margins(0.02)
plt.xlabel('x', fontsize=14)
plt.ylabel('y', fontsize=14)
plt.draw()
plt.show()
