def ingresar_calificaciones():
    materias = []
    calificaciones = []
    
    while True:
        materia = input("Ingresa el nombre de la materia: ").strip()
        if not materia:
            print("El nombre de la materia no puede estar vacío.")
            continue
            
        while True:
            try:
                calificacion = float(input(f"Ingresa la calificación para {materia} (0 - 10): "))
                if 0.0 <= calificacion <= 10.0:
                    break
                else:
                    print("Error: La calificación debe estar entre 0 y 10.")
            except ValueError:
                print("Error: Debes ingresar un valor numérico.")
                
        materias.append(materia)
        calificaciones.append(calificacion)
        
        continuar = input("¿Deseas ingresar otra materia? (s/n): ").strip().lower()
        if continuar != 's':
            break
            
    return materias, calificaciones

def calcular_promedio(calificaciones):
    if not calificaciones:
        return 0.0
    return sum(calificaciones) / len(calificaciones)

def determinar_estado(calificaciones, umbral=5.0):
    aprobadas_idx = []
    reprobadas_idx = []
    for i, cal in enumerate(calificaciones):
        if cal >= umbral:
            aprobadas_idx.append(i)
        else:
            reprobadas_idx.append(i)
    return aprobadas_idx, reprobadas_idx

def encontrar_extremos(calificaciones):
    if not calificaciones:
        return None, None
    mejor_idx = calificaciones.index(max(calificaciones))
    peor_idx = calificaciones.index(min(calificaciones))
    return mejor_idx, peor_idx

def main():
    print("--- Calculadora de Promedios ---")
    materias, calificaciones = ingresar_calificaciones()
    
    if not materias:
        print("\nNo se ingresó ninguna materia. Saliendo del programa...")
        return
        
    promedio = calcular_promedio(calificaciones)
    aprobadas_idx, reprobadas_idx = determinar_estado(calificaciones)
    mejor_idx, peor_idx = encontrar_extremos(calificaciones)
    
    print("\n" + "="*30)
    print("--- Resumen Final ---")
    print("="*30)
    
    print("\nListado de materias y calificaciones:")
    for m, c in zip(materias, calificaciones):
        print(f"- {m}: {c}")
        
    print(f"\nPromedio general: {promedio:.2f}")
    
    print("\nMaterias Aprobadas:")
    if aprobadas_idx:
        for i in aprobadas_idx:
            print(f"- {materias[i]} ({calificaciones[i]})")
    else:
        print("- Ninguna")
        
    print("\nMaterias Reprobadas:")
    if reprobadas_idx:
        for i in reprobadas_idx:
            print(f"- {materias[i]} ({calificaciones[i]})")
    else:
        print("- Ninguna")
        
    print(f"\nMejor calificación: {materias[mejor_idx]} con {calificaciones[mejor_idx]}")
    print(f"Peor calificación: {materias[peor_idx]} con {calificaciones[peor_idx]}")
    
    print("\n¡Gracias por utilizar la calculadora de promedios! Hasta pronto.")

if __name__ == "__main__":
    main()