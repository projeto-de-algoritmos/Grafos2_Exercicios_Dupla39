# Network Delay Time(Atraso de tempo da internet)

import heapq
import math

class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(list)

        for u, v, time in times:
            graph[u].append([v, time])
        
        time = [math.inf] * n
        time[k-1] = 0
        heap = [[0, k]] 

        visited = [] 
        visited.append(k)

        while heap: 
            t, atlVertice = heapq.heappop(heap)
            for v, vTime in graph[atlVertice]:
                total = t + vTime
                if total < time[v-1]:
                    time[v-1] = total
                    visited.append(v)
                    heapq.heappush(heap, [total, v])
            visited.append(atlVertice)

        if (len(visited) == n):
            return max(time)
        else:
            return -1
