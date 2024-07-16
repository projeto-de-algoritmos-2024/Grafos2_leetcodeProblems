import heapq
import sys

class Solution:
    DIR = [0, 1, 0, -1, 0]
    
    def minimumEffortPath(self, heights):
        m, n = len(heights), len(heights[0])
        dist = [[sys.maxsize] * n for _ in range(m)]
        
        minHeap = []
        heapq.heappush(minHeap, (0, 0, 0))  # (distancia, linha, coluna)
        dist[0][0] = 0
        
        while minHeap:
            d, r, c = heapq.heappop(minHeap)
            if d > dist[r][c]:
                continue  
            if r == m - 1 and c == n - 1:
                return d  
            for i in range(4):
                nr, nc = r + self.DIR[i], c + self.DIR[i + 1]
                if 0 <= nr < m and 0 <= nc < n:
                    novoDist = max(d, abs(heights[nr][nc] - heights[r][c]))
                    if dist[nr][nc] > novoDist:
                        dist[nr][nc] = novoDist
                        heapq.heappush(minHeap, (dist[nr][nc], nr, nc))
  