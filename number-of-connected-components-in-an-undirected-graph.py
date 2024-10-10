# class Solution:
#     def countComponents(self, n: int, edges: List[List[int]]) -> int:
#         connections = 0
#         visited = set()

#         adj_list = {i: [] for i in range(n)}
#         for n1, n2 in edges:
#             adj_list[n1].append(n2)
#             adj_list[n2].append(n1)

#         queue = deque()
        
#         for key, val in adj_list.items():
#             if key not in visited:
#                 connections += 1
#                 queue.append(key)
#                 while queue:
#                     curr = queue.popleft()
#                     visited.add(curr)
#                     for neigh in adj_list[curr]:
#                         if neigh not in visited:
#                             queue.append(neigh)
        
#         return connections

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        rank = [1] * n

        def find(node):
            # temp = node
            while node != parent[node]:
                parent[node] = parent[parent[node]]
                node = parent[node]
            return node
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return 0
            if rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]
            
            return 1
        
        ans = n
        for i, j in edges:
            ans -= union(i, j)
        
        return ans
