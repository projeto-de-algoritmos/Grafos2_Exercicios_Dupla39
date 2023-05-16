# Path with Maximum Probability(Caminho com Maior Probabilidade)
import heapq

class Solution:
    def maxProbability(self, n: int, edges: list[list[int]], succProb: list[float], start: int, end: int) -> float:
        graph = collections.defaultdict(list)
        for i in range(len(edges)):
            p, s = edges[i]
            graph[p].append((succProb[i], s))
            graph[s].append((succProb[i], p))
        
        # Declarando a maxheap
        max_heap = [[-1, start]]
        visited = []
        
        while max_heap:
            # Remove da heap
            p, vertice = heapq.heappop(max_heap) 
            
            if vertice == end:
                return -p
            
            visited.append(vertice)
            for i, j in graph[vertice]:
                if j not in visited:
                    # Adiciona na heap
                    heapq.heappush(max_heap, [(p*i), j])
                
        return 0.00000