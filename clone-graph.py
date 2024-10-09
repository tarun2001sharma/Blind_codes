class Node:
    def __init__(self, val: int = 0, neighbors: List['Node'] = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    '''
    Time Complexity:
    O(V + E), where V is the number of vertices (nodes) and E is the number of edges.
    Each node is visited once, and for each node, we traverse all its neighbors (edges).
    
    Space Complexity:
    O(V) for the node_map and the recursion stack (or the queue in BFS).
    The space complexity is proportional to the number of nodes because we store each node in the node_map.
    '''
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        
        # Dictionary to keep track of visited nodes and their clones
        node_map = {}

        # Recursive DFS function to clone the graph
        def dfs(original_node: 'Node') -> 'Node':
            # If the node has already been cloned, return the cloned node
            if original_node in node_map:
                return node_map[original_node]
            
            # Clone the node
            clone = Node(original_node.val)
            node_map[original_node] = clone  # Map the original node to its clone
            
            # Iterate over the neighbors and recursively clone them
            for neighbor in original_node.neighbors:
                clone.neighbors.append(dfs(neighbor))  # Add the cloned neighbors
            
            return clone
        
        # Start the DFS with the original node
        return dfs(node)
