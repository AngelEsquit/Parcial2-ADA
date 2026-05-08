def ContarCombinacionesTeclado(n):
    if n == 1:
        return 10
    
    # Definir diccionario con los vecinos
    # Se omiten * y # según restricciones
    vecinos = {
        0: [8],
        1: [2, 4],
        2: [1, 3, 5],
        3: [2, 6],
        4: [1, 5, 7],
        5: [2, 4, 6, 8],
        6: [3, 5, 9],
        7: [4, 8],
        8: [5, 7, 9, 0],
        9: [6, 8]
    }
    
    # dp = Arreglo de tamaño 10 inicializado en 1
    dp = [1] * 10
    
    for k in range(2, n + 1):
        # nuevo_dp = Arreglo de tamaño 10 inicializado en 0
        nuevo_dp = [0] * 10
        # Para cada digito i desde 0 hasta 9
        for i in range(10):
            for v in vecinos[i]:
                nuevo_dp[i] += dp[v]
        dp = nuevo_dp
        
    return sum(dp)