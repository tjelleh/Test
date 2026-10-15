from ROOT import TH1F, TCanvas, gStyle

import matplotlib.pyplot as plt
import numpy as np

x = np.array([1, 2, 3, 4, 5])
y = np.array([10, 20, 15, 25, 30])

plt.plot(x, y, marker='o', linestyle='-', color='r')
plt.title('Exercise Histogram')
plt.xlabel('X-Achse')
plt.ylabel('Y-Achse')
plt.grid(True)
plt.legend(['Data Points'])
plt.show()

print("Hist was plotted successfully.")