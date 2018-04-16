import sys
import matplotlib.pyplot as plt
import numpy as np

nombre_imagen = sys.argv[1]
n_pixel_kernel = int(sys.argv[2])

std = 1.0
centro = n_pixel_kernel//2+1
kernel = np.zeros((n_pixel_kernel, n_pixel_kernel))

for i in range(n_pixel_kernel):
	for j in range(n_pixel_kernel):
		distancia = float((i+1-centro)**2 + (j+1-centro)**2)
		kernel[i, j] = np.exp(-distancia/(2*std**2))
kernel = kernel/sum(sum(kernel))

imagen = plt.imread(nombre_imagen)
filas, columnas, capas = len(imagen), len(imagen[0]), len(imagen[0][0])
for i in range(filas):
	for j in range(columnas):
		for k in range(capas):
			suma = 0
			for l in range(-(centro-1),centro):
				for m in range(-(centro-1),centro):
					if not (i+l<0 or i+l>filas-1 or j+m<0 or j+m>columnas-1):
						suma+=kernel[centro+l-1,centro+m-1]*imagen[i+l][j+m][k]	
			imagen[i][j][k] = suma
plt.imshow(imagen)
plt.savefig("suave.png")
