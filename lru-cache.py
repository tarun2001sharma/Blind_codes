class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.prev = None
        self.next = None

class LRUCache:
    '''
    Time Complexity:
    get and put: O(1) on average due to the hashmap and doubly linked list operations.
    
    Space Complexity:
    O(n) where n is the capacity of the cache (for storing the hashmap and the linked list nodes).
    '''
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} # mapping every key to corresponding node

        self.least_recent, self.most_recent = ListNode(0, 0), ListNode(0, 0)
        self.least_recent.next = self.most_recent
        self.most_recent.prev = self.least_recent
    
    # remove the LRU node
    def remove(self, node):
        prev_node, next_node = node.prev, node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    # add node at the most recently used side
    def insert(self, node):
        prev_node = self.most_recent.prev
        next_node = self.most_recent
        prev_node.next = node
        next_node.prev = node
        node.next = next_node
        node.prev = prev_node
        self.most_recent.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = ListNode(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            # remove the LRU node fro cache
            lru = self.least_recent.next
            self.remove(lru)
            del self.cache[lru.key]

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
