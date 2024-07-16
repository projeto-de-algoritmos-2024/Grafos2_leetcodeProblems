class unionfind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [1] * n
    
    def find(self, v1):
        while v1 != self.par[v1]:
            self.par[v1] = self.par[self.par[v1]]
            v1 = self.par[v1]
        return v1

    def union(self, v1, v2):
        p1, p2 = self.find(v1), self.find(v2)
        if p1 == p2:
            return False
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.par[p1] = p2
            self.rank[p2] += self.rank[p1]
        return True


class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n, edges):
        for i, e in enumerate(edges):
            e.append(i)
        
        edges.sort(key=lambda e: e[2])
        
        def kruskal(edges, n, banned_edge=None, include_edge=None):
            uf = unionfind(n)
            total_weight = 0
            edges_used = 0

            if include_edge:
                uf.union(include_edge[0], include_edge[1])
                total_weight += include_edge[2]
                edges_used += 1

            for v1, v2, w, i in edges:
                if i == banned_edge:
                    continue
                if uf.union(v1, v2):
                    total_weight += w
                    edges_used += 1
                if edges_used == n - 1:
                    break

            return total_weight if edges_used == n - 1 else float('inf')
        
        original_mst_weight = kruskal(edges, n)
        
        crit, pseud = [], []
        
        for n1, n2, e_weight, i in edges:
            # ver se é critical
            if kruskal(edges, n, banned_edge=i) > original_mst_weight:
                crit.append(i)
            # Ver é pseudo
            elif kruskal(edges, n, include_edge=[n1, n2, e_weight, i]) == original_mst_weight:
                pseud.append(i)
        
        return [crit, pseud]
