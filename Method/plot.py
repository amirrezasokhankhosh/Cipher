import matplotlib.pyplot as plt
import numpy as np

smd_w = [0.01620906, 0.01869368, 0.03558314,
         0.03558314, 0.02070571, 0.02555159]
smd_raw = [0.1682156, 0.7501993, 0.1386352,
           0.1386352, 0.7674266, 0.1865729]

labels = ["Households", "Generated E", "Consumed E", "Max Consumed E", "Area", "People"]

plt.style.use('seaborn-whitegrid')

plt.plot(smd_w, range(0, 6, 1), marker='o', label="Weighted Data")
plt.plot(smd_raw, range(0, 6, 1), marker='o', label="Raw Data")

plt.xticks(np.arange(0,0.8, 0.05))
plt.yticks(range(0, 6, 1), labels)

plt.xlabel("Features")
plt.ylabel("SMD")

plt.legend()

plt.show()

