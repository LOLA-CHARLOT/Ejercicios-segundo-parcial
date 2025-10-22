import numpy as np
from scipy.stats import (
    uniform, erlang, expon, gamma, norm, weibull_min, bernoulli, binomial
)

def calcular_distribucion(nombre_distribucion, x, *parametros):
    """
    Calcula la función de densidad de probabilidad (PDF) o la función 
    de masa de probabilidad (PMF) para un valor x dado en la distribución.

    Args:
        nombre_distribucion (str): Nombre de la distribución (ej: 'normal', 'binomial').
        x (float o int): El punto en el que se evalúa la distribución.
        *parametros: Los parámetros necesarios para la distribución.

    Returns:
        float: El valor de la PDF o PMF en el punto x.
    """
    
    # Estandarización de nombres y selección de la clase de distribución
    distribuciones = {
        'uniforme': uniform,
        'erlang': erlang,
        'exponente': expon,
        'gamma': gamma,
        'normal': norm,
        'weibull': weibull_min, # weibull_min es la implementación estándar en SciPy
        'bernoulli': bernoulli,
        'binomial': binomial
    }

    if nombre_distribucion.lower() not in distribuciones:
        return f"Error: Distribución '{nombre_distribucion}' no reconocida."

    dist = distribuciones[nombre_distribucion.lower()]

    try:
        # Para distribuciones continuas (la mayoría), usamos 'pdf'
        # Para distribuciones discretas (Bernoulli, Binomial), usamos 'pmf'
        if nombre_distribucion.lower() in ['bernoulli', 'binomial']:
            # pmf: Probability Mass Function (Función de Masa de Probabilidad)
            # x debe ser un entero para distribuciones discretas
            valor = dist.pmf(x, *parametros)
        else:
            # pdf: Probability Density Function (Función de Densidad de Probabilidad)
            valor = dist.pdf(x, *parametros)
            
        return valor
        
    except TypeError as e:
        return f"Error de parámetros: {e}. Verifique el número y tipo de parámetros para {nombre_distribucion}."
    except Exception as e:
        return f"Ocurrió un error inesperado: {e}"

# ----------------------------------------------------------------------
## EJEMPLOS DE USO
# ----------------------------------------------------------------------

print("--- Ejemplos de Distribuciones Continuas (PDF) ---")

# 1. Normal (Media=0, Desviación Estándar=1)
# Parámetros: loc (media), scale (desviación estándar)
x_normal = 0.5
pdf_normal = calcular_distribucion('normal', x_normal, 0, 1)
print(f"Normal en x={x_normal}: {pdf_normal:.4f}")

# 2. Gamma (a=2, loc=0, scale=1)
# Parámetros: a (parámetro de forma), loc (origen), scale (escala)
x_gamma = 1.5
pdf_gamma = calcular_distribucion('gamma', x_gamma, 2, 0, 1)
print(f"Gamma en x={x_gamma}: {pdf_gamma:.4f}")

# 3. Weibull (c=2, loc=0, scale=1)
# Parámetros: c (parámetro de forma), loc (origen), scale (escala)
x_weibull = 1.0
pdf_weibull = calcular_distribucion('weibull', x_weibull, 2, 0, 1)
print(f"Weibull en x={x_weibull}: {pdf_weibull:.4f}")


print("\n--- Ejemplos de Distribuciones Discretas (PMF) ---")

# 4. Bernoulli (p=0.3)
# Parámetros: p (probabilidad de éxito)
x_bernoulli = 1 # 1 para éxito, 0 para fracaso
pmf_bernoulli = calcular_distribucion('bernoulli', x_bernoulli, 0.3)
print(f"Bernoulli (p=0.3) en x={x_bernoulli}: {pmf_bernoulli:.4f}")

# 5. Binomial (n=10, p=0.5)
# Parámetros: n (número de ensayos), p (probabilidad de éxito)
x_binomial = 7 # Probabilidad de obtener 7 éxitos en 10 ensayos
pmf_binomial = calcular_distribucion('binomial', x_binomial, 10, 0.5)
print(f"Binomial (n=10, p=0.5) en x={x_binomial}: {pmf_binomial:.4f}")
