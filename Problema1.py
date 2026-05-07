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