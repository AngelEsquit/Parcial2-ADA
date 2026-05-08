def ContarCombinacionesTeclado(n):
    if n == 1:
        return 10
    
    # Definir diccionario con los vecinos
    # Se omiten * y # según restricciones
    vecinos = {
        0: [0, 8],
        1: [1, 2, 4],
        2: [2, 1, 3, 5],
        3: [3, 2, 6],
        4: [4, 1, 5, 7],
        5: [5, 2, 4, 6, 8],
        6: [6, 3, 5, 9],
        7: [7, 4, 8],
        8: [8, 5, 7, 9, 0],
        9: [9, 6, 8]
    }
    
    # dp = Arreglo de tamaño 10 inicializado en 1
    dp = [1] * 10
    
    for k in range(2, n + 1):
        # nuevo_dp = Arreglo de tamaño 10 inicializado en 0
        nuevo_dp = [0] * 10
        # Para cada digito i desde 0 hasta 9
        for i in range(10):
            for v in vecinos[i]:
                nuevo_dp[v] += dp[i]
        dp = nuevo_dp
        
    return sum(dp)

# --- Casos de Prueba ---
def ejecutar_pruebas():
    print("--- CASOS DE PRUEBA ---")
    
    # Caso 1: n = 2
    print(f"n = 2: {ContarCombinacionesTeclado(2)} combinaciones")
    
    # Caso 2: n = 3
    print(f"n = 3: {ContarCombinacionesTeclado(3)} combinaciones")
    
    # Caso 3: n = 5
    print(f"n = 5: {ContarCombinacionesTeclado(5)} combinaciones")

if __name__ == "__main__":
    ejecutar_pruebas()