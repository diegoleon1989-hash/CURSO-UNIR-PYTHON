def main():
# Este programa permite ingresar calificaciones de materias, calcular el promedio, determinar el estado del estudiante y encontrar las materias con las calificaciones más altas y más bajas.
    # Llama a la función para ingresar calificaciones y materias
    materias, calificaciones = ingresar_calificaciones()
    print("Materias:", materias)
    print("Calificaciones:", calificaciones)
    # Calcula el promedio de las calificaciones
    promedio = calcular_promedio(calificaciones)
    print("Promedio de calificaciones:", promedio)
    # Define el umbral para aprobar o reprobar
    umbral = 5.0
    materias_aprobadas, materias_reprobadas = determinar_estado(materias, calificaciones, umbral)
    print("Estado del estudiante:\n", "Aprobadas:", materias_aprobadas, "Reprobadas:", materias_reprobadas)
    #
    materia_max, calificacion_max, materia_min, calificacion_min = encontrar_extremos(materias, calificaciones)
    print(f"Las materias con la calificación más alta son {materia_max} con una calificación de {calificacion_max}.")
    print(f"Las materias con la calificación más baja son {materia_min} con una calificación de {calificacion_min}.")

# función para ingresar calificaciones y materias
def ingresar_calificaciones():
    materias = []
    calificaciones = []
    while True:
        materia = input("Ingrese el nombre de la materia: ")
        calificacion = float(input(f"Ingrese la calificación para {materia}: "))
        while not (0 <= calificacion <= 10):
            print("La calificación debe estar entre 0 y 10. Intente nuevamente.")
            calificacion = float(input(f"Ingrese la calificación para {materia}: "))
        ingresar = input("¿Desea ingresar otra materia? (si/no): ")
        while ingresar.lower() not in ['si', 'no']:
            print("Respuesta inválida. Por favor, responda 'si' o 'no'.")
            ingresar = input("¿Desea ingresar otra materia? (si/no): ")
        materias.append(materia)
        calificaciones.append(calificacion)
        if ingresar.lower() != 'si':
            break
    
    return materias, calificaciones
# función para calcular el promedio de calificaciones
def calcular_promedio(calificaciones):
    if len(calificaciones) == 0:
        return 0
    return sum(calificaciones) / len(calificaciones)

# función para determinar el estado del estudiante
materias_reprobadas = []
materias_aprobadas = []
def determinar_estado(materias,calificaciones, umbral):
    materias_calificaciones = list(zip(materias, calificaciones))
    
    if len(calificaciones) == 0:
        return "No hay calificaciones para evaluar."
    for materia, calificacion in materias_calificaciones:
        if calificacion < umbral:
            materias_reprobadas.append(materia)
        else:
            materias_aprobadas.append(materia)
    if len(materias_aprobadas) == 0:
        print("El estudiante ha reprobado todas las materias.")
    elif len(materias_reprobadas) == 0:
        print("El estudiante ha aprobado todas las materias.")
    return materias_aprobadas, materias_reprobadas
# función para encontrar las materias con las calificaciones más altas y más bajas
def encontrar_extremos(materias, calificaciones):
    if len(calificaciones) == 0:
        return "No hay calificaciones para evaluar."
    max_calificacion = max(calificaciones)
    max_calficaciones = [calificacion for calificacion in calificaciones if calificacion == max_calificacion]
    min_calificacion = min(calificaciones)
    min_calficaciones = [calificacion for calificacion in calificaciones if calificacion == min_calificacion]
    materias_max = [materias[i] for i, calificacion in enumerate(calificaciones) if calificacion == max_calificacion]
    materias_min = [materias[i] for i, calificacion in enumerate(calificaciones) if calificacion == min_calificacion]
    
    return materias_max, max_calificacion, materias_min, min_calificacion
# se ejecuta la función principal si el archivo se ejecuta directamente
if __name__ == "__main__":
    main()
