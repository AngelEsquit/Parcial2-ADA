def HacerSencillo(monto, denominaciones):
    # resultado = [ ]
    resultado = []
    
    # Ordenar denominaciones desc
    denominaciones_ordenadas = sorted(denominaciones, reverse=True)
    
    # Para cada d en denominaciones_ordenadas
    for d in denominaciones_ordenadas:
        
        # Mientras monto >= d
        while monto >= d:
            # Agregar d a resultado
            resultado.append(d)
            # monto = monto - d
            monto = monto - d
            
    # Retornar resultado
    return resultado

# --- Casos de prueba ---

def probar_algoritmo():
    # Denominaciones
    monedas = [1, 5, 10, 25]
    
    # Caso 1: Monto de 294 centavos
    # Se esperan: 11 de 25, 1 de 10, 1 de 5, 4 de 1.
    print(f"Caso 1 (294): {HacerSencillo(294, monedas)}")
    
    # Caso 2: Monto de 48 centavos
    # Se esperan: 1 de 25, 2 de 10, 3 de 1.
    print(f"Caso 2 (48):  {HacerSencillo(48, monedas)}")
    
    # Caso 3: Monto de 15 centavos
    # Se esperan: 1 de 10, 1 de 5.
    print(f"Caso 3 (15):  {HacerSencillo(15, monedas)}")

if __name__ == "__main__":
    probar_algoritmo()