class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        mergedstr = ''
        i, j = 0, 0

        while (i < len(word1) and j < len(word2)):
            mergedstr += word1[i]
            mergedstr += word2[j]
            i += 1
            j += 1
        
        if i != len(word1):
            mergedstr += word1[i:] 
        if j != len(word2):
            mergedstr += word2[j:] 
        
        return mergedstr
        
