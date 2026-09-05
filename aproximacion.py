import math

print("--- Evaluación del Algoritmo ---")

# Parámetros del cálculo
x = 1.0
aproximacion = 0.0
iteraciones = 12

# Bucle interactivo para ver la convergencia
for i in range(iteraciones):
    termino = (x ** i) / math.factorial(i)
    aproximacion += termino
    print(f"Iteración {i}: Término sumado = {termino:.4f} | Acumulado = {aproximacion:.4f}")

# Comparación con el valor teórico de la librería
valor_real = math.exp(x)
error_absoluto = abs(valor_real - aproximacion)

print("\n--- Resultados Finales ---")
print(f"Aproximación numérica: {aproximacion:.6f}")
print(f"Valor real de la función: {valor_real:.6f}")
print(f"Error absoluto residual: {error_absoluto:.6f}")