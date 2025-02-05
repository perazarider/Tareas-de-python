import numpy as np
import matplotlib.pyplot as plt

# Inicialización de variables
epsilon = 1.0  # Valor inicial de epsilon
iteracion = 0  # Contador de iteraciones
historial_epsilon = []  # Lista para almacenar los valores de epsilon
historial_iteracion = []  # Lista para almacenar las iteraciones

# Bucle para encontrar la precisión de máquina
while 1.0 + epsilon != 1.0:
    epsilon /= 2  # Se divide epsilon entre 2 en cada iteración
    iteracion += 1  # Se incrementa el contador de iteraciones
    historial_epsilon.append(epsilon)  # Se almacena el valor de epsilon
    historial_iteracion.append(iteracion)  # Se almacena la iteración

# Se multiplica por 2 para obtener la precisión de máquina real
epsilon *= 2
print(f"Precisión de máquina: {epsilon}")

# Graficar la evolución de epsilon
plt.figure(figsize=(8, 5))
plt.plot(historial_iteracion, historial_epsilon, marker='o', linestyle='-')
plt.xlabel("Iteraciones")
plt.ylabel("Valor de epsilon")
plt.title("Convergencia de Epsilon a la Precisión de Máquina")
plt.yscale("log")  # Escala logarítmica para mejor visualización
plt.grid(True)
plt.show()
