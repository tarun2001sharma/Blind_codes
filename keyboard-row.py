class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        
        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")

        result = []


        def issubset(row, word):
            for char in word:
                if char not in row:
                    return False
            return True
        
        for word in words:
            low_word = word.lower()

            if issubset(row1, low_word) or issubset(row2, low_word) or issubset(row3, low_word):
                result.append(word)
        
        return result
