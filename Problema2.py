def KnapsackFraccionado(capacidad, articulos):
    resultado = 0.0
    cantidades = []
    
    # Calcular densidad y ordenar artículos por densidad (p/w) desc
    # Cada item es un objeto o diccionario con p y w
    for item in articulos:
        item['densidad'] = item['p'] / item['w']
        
    articulos_ordenados = sorted(articulos, key=lambda x: x['densidad'], reverse=True)
    
    for item in articulos_ordenados:
        if capacidad > 0:
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

# --- Casos de Prueba ---

def ejecutar_pruebas():
    # Definición del sistema de artículos
    # Estructura: {'id': nombre, 'p': precio, 'w': peso}
    
    print("--- CASO DE PRUEBA 1: Instancia del Examen ---")
    # Este caso prueba la capacidad de fraccionar el último objeto exactamente
    items1 = [
        {'id': 'item 1', 'p': 60, 'w': 10},  # Densidad: 6.0
        {'id': 'item 2', 'p': 100, 'w': 20}, # Densidad: 5.0
        {'id': 'item 3', 'p': 120, 'w': 30}  # Densidad: 4.0
    ]
    W1 = 50
    texto1, total1 = KnapsackFraccionado(W1, items1)
    print(f"Capacidad: {W1}u | {texto1} | Total: ${total1}\n")

    print("--- CASO DE PRUEBA 2: Artículos con Densidades Similares ---")
    # Obliga al algoritmo a ser preciso en la ordenación.
    items2 = [
        {'id': 'item A', 'p': 50, 'w': 25},  # Densidad: 2.0
        {'id': 'item B', 'p': 19, 'w': 10},  # Densidad: 1.9
        {'id': 'item C', 'p': 100, 'w': 100} # Densidad: 1.0
    ]
    W2 = 30
    texto2, total2 = KnapsackFraccionado(W2, items2)
    print(f"Capacidad: {W2}u | {texto2} | Total: ${total2}\n")

    print("--- CASO DE PRUEBA 3: Mochila con Gran Capacidad ---")
    # El algoritmo debe tomar todo y terminar con capacidad sobrante.
    items3 = [
        {'id': 'item X', 'p': 500, 'w': 10},
        {'id': 'item Y', 'p': 200, 'w': 10}
    ]
    W3 = 100
    texto3, total3 = KnapsackFraccionado(W3, items3)
    print(f"Capacidad: {W3}u | {texto3} | Total: ${total3}\n")

if __name__ == "__main__":
    ejecutar_pruebas()