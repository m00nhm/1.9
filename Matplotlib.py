import matplotlib.pyplot as plt

# Relación entre elementos y electronegatividad
elementos = ['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne']
electronegatividad = [2.1, 0, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 0]

plt.figure(figsize=(12, 6))
plt.subplot(1, 3, 1)
plt.bar(elementos, electronegatividad, color='teal')
plt.title('Electronegatividad de Elementos')
plt.xlabel('Elemento')
plt.ylabel('Electronegatividad')

# Relación de elementos y su masa molar
masa_molar = [1.008, 4.0026, 6.94, 9.0122, 10.81, 12.011, 14.007, 15.999, 18.998, 20.180]

plt.subplot(1, 3, 2)
plt.plot(elementos, masa_molar, marker='o', color='orange')
plt.title('Masa Molar de Elementos')
plt.xlabel('Elemento')
plt.ylabel('Masa Molar (g/mol)')

# Relación de viscosidad y temperatura de un Aceite de motor
temperatura = [0, 20, 40, 60, 80, 100, 120, 140, 160, 180]
viscosidad = [150, 140, 120, 100, 80, 60, 50, 40, 35, 30]  # cSt a distintas temperaturas

plt.subplot(1, 3, 3)
plt.plot(temperatura, viscosidad, marker='x', linestyle='--', color='red')
plt.title('Viscosidad vs Temperatura')
plt.xlabel('Temperatura (°C)')
plt.ylabel('Viscosidad (cSt)')
plt.grid()

# Mostrar todas las gráficas
plt.tight_layout()
plt.show()
