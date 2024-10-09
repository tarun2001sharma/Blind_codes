class TrieNode:
    def __init__(self):
        self.children = {}
        self.eow = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.eow = True
        
    def search(self, word: str) -> bool:
        def dfs(node, i):
            if i == len(word):
                return node.eow
            
            char = word[i]
            if char == '.':
                for child in node.children.values():
                    if dfs(child, i+1):
                        return True
                return False
            
            if char in node.children:
                return dfs(node.children[char], i+1)
            else:
                return False
        
        return dfs(self.root, 0)

        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
