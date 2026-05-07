def KnapsackFraccionado(capacidad, articulos):
    resultado = 0.0
    cantidades = []
    
    # Calcular densidad y ordenar artículos por densidad (p/w) desc
    # Cada item es un objeto o diccionario con p y w
    for item in articulos:
        item['densidad'] = item['p'] / item['w']
        
    articulos_ordenados = sorted(articulos, key=lambda x: x['densidad'], reverse=True)
    
    # Para cada item en artículos
    for item in articulos_ordenados:
        # Si capacidad > 0:
        if capacidad > 0:
            # Si item.w <= capacidad
            if item['w'] <= capacidad:
                resultado = resultado + item['p']
                capacidad = capacidad - item['w']
                # Agregar item.w a cantidades
                cantidades.append(f"{item['w']} unidades del {item['id']}")
            else:
                fraccion = capacidad / item['w']
                resultado = resultado + (item['p'] * fraccion)
                # Agregar capacidad a cantidades
                cantidades.append(f"{capacidad} unidades del {item['id']}")
                capacidad = 0
                
    return cantidades, resultado