class Solution:
    '''
    Time Complexity:
    O(m + n), where m is the number of prerequisites and n is the number of courses. We process each edge (prerequisite) once and each node (course) once.
    
    Space Complexity:
    O(m + n) for the adjacency list, indegree array, and queue.
    '''
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree= [0]*numCourses
        adj_list = []
        for _ in range(numCourses):
            adj_list.append([])

        for post, pre in prerequisites:
            indegree[post] += 1
            adj_list[pre].append(post)
        
        queue = deque()
        for idx in range(len(indegree)):
            if indegree[idx] == 0:
                queue.append(idx)

        nodes_visited = 0
        while queue:
            curr = queue.popleft()
            nodes_visited += 1

            for neigh in adj_list[curr]:
                indegree[neigh]-=1
                if indegree[neigh] == 0:
                    queue.append(neigh)
        
        return nodes_visited == numCourses
        
