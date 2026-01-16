import numpy as np
import matplotlib.pyplot as plt
np.random.seed(1234)
matriz = np.random.rand(100, 100)
matriz1 = matriz>.25
matriz1[0,0] = True

plt.imshow(matriz1, cmap='gray', interpolation='nearest')

# Remove axis ticks and labels for a cleaner look
plt.xticks([])
plt.yticks([])

# Add a title to the plot
plt.title("Laberinto Propuesto (100x100)")

# Show the plot
plt.show()

path = r'C:\Users\mateo\OneDrive\Desktop\MATEO\TRANSITORIO\Universidad_Academico\2025_2\MIS\Talleres\Data_T02_MIS.txt'
np.savetxt(path, matriz1, delimiter=',')
