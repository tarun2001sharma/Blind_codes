class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # BFS Approach:
        # visited = set()

        # if len(edges) != n - 1:
        #     return False
        # if not edges and n == 1:
        #     return True

        # adj_list = {}
        # for pre, post in edges:
        #     if pre not in adj_list:
        #         adj_list[pre] = [post]
        #     else:
        #         adj_list[pre].append(post)
        #     if post not in adj_list:
        #         adj_list[post] = [pre]
        #     else:
        #         adj_list[post].append(pre)

        # queue = deque()
        # queue.append([edges[0][0], -1])
        # prev = -1
        # counter = 0
        # while queue:
        #     curr, parent = queue.popleft()
        #     counter += 1
        #     if curr in visited:
        #         return False
        #     visited.add(curr)
        #     for neigh in adj_list[curr]:
        #         if neigh != parent:
        #             queue.append([neigh, curr])
        #         # prev = curr
        
        # if counter != n:
        #     return False
        # return True

        # DFS Approach

        if not edges:
            return n == 1

        visited = set()
        adj_list = {i: [] for i in range(n)}

        for n1, n2 in edges:
            adj_list[n1].append(n2)
            adj_list[n2].append(n1)

        def dfs(curr, prev):
            if curr in visited:
                return False
            
            visited.add(curr)

            for neigh in adj_list[curr]:
                if neigh != prev:
                    if not dfs(neigh, curr):
                        return False
            
            return True
        
        res = dfs(edges[0][0], -1)
        if len(visited) != n:
            return False
        return res


        
        
