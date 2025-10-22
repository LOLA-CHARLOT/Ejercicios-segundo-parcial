Python 3.13.9 (tags/v3.13.9:8183fa5, Oct 14 2025, 14:09:13) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> import numpy as np
... 
... def siguiente_generacion(tablero_actual):
...     """
...     Calcula el estado de la siguiente generación en el Juego de la Vida de Conway.
... 
...     El estado del tablero debe ser una matriz numpy bidimensional de 0s y 1s.
...     """
...     filas, columnas = tablero_actual.shape
...     tablero_nuevo = np.zeros((filas, columnas), dtype=int)
... 
...     # Iterar sobre cada célula del tablero, excluyendo los bordes
...     # Para manejar bordes infinitos se podría usar un 'toroidal wrap' o padding,
...     # pero aquí simplificamos el cálculo al interior del área.
...     for i in range(1, filas - 1):
...         for j in range(1, columnas - 1):
...             
...             # 1. Contar vecinas vivas
...             # Se suman los 8 vecinos alrededor de la célula (i, j)
...             vecinos_vivos = np.sum(tablero_actual[i-1:i+2, j-1:j+2]) - tablero_actual[i, j]
...             
...             estado_actual = tablero_actual[i, j]
... 
...             # 2. Aplicar las reglas del Juego de la Vida
...             
...             if estado_actual == 1:
...                 # Regla de Supervivencia:
...                 # La célula viva (1) sobrevive si tiene 2 o 3 vecinos.
...                 if vecinos_vivos == 2 or vecinos_vivos == 3:
...                     tablero_nuevo[i, j] = 1
...                 # De lo contrario (soledad o sobrepoblación), muere y se queda en 0.
...             else:
...                 # Regla de Nacimiento:
...                 # La célula muerta (0) nace si tiene exactamente 3 vecinos vivos.
                if vecinos_vivos == 3:
                    tablero_nuevo[i, j] = 1
                # De lo contrario, permanece muerta en 0.
                
    return tablero_nuevo

def imprimir_tablero(tablero):
    """Imprime el tablero con una visualización simple (caracteres)."""
    for fila in tablero:
        print(''.join(['■' if cell == 1 else '□' for cell in fila]))

# ----------------------------------------------------------------------
# EJEMPLO DE USO: Simulación del patrón "Glider" (Planeador)
# ----------------------------------------------------------------------

# Definición del patrón inicial (Glider) en un tablero de 10x10
# Se debe adaptar el tamaño del tablero a los ejercicios proporcionados.
tablero_inicial = np.zeros((10, 10), dtype=int)
tablero_inicial[1, 2] = 1
tablero_inicial[2, 3] = 1
tablero_inicial[3, 1] = 1
tablero_inicial[3, 2] = 1
tablero_inicial[3, 3] = 1

print("--- Generación 0 (Inicial) ---")
imprimir_tablero(tablero_inicial)

# Simular varias generaciones
tablero_actual = tablero_inicial
for gen in range(1, 5):
    tablero_actual = siguiente_generacion(tablero_actual)
    print(f"\n--- Generación {gen} ---")
