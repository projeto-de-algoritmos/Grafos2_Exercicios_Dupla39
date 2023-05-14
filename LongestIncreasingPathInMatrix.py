class Solution(object):
    def longestIncreasingPath(self, matriz):      
        if not matriz:
            return 0

        linhas = len(matriz)
        colunas = len(matriz[0])
        direcoes = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        cache = [[0] * colunas for _ in range(linhas)]
        maxCaminho = 0

        #Função de busca em profundidade (dfs) para encontrar o caminho mais longo e crescente
        def dfs(i, j):
            if cache[i][j] != 0:
                return cache[i][j]

            comprimento = 1
            for dx, dy in direcoes:
                x = i + dx
                y = j + dy
                if 0 <= x < linhas and 0 <= y < colunas and matriz[x][y] > matriz[i][j]:
                    novoComprimento = 1 + dfs(x, y)
                    if novoComprimento > comprimento:
                        comprimento = novoComprimento

            cache[i][j] = comprimento
            return comprimento

        for i in range(linhas):
            for j in range(colunas):
                novoComprimento = dfs(i, j)
                if novoComprimento > maxCaminho:
                    maxCaminho = novoComprimento


        return maxCaminho

        matriz = [
        [9, 8, 4],
        [6, 4, 8],
        [3, 1, 1]
        ]
        resultado = longestIncreasingPath(matriz)
        print(resultado)