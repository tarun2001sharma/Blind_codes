class Solution:
    def minChanges(self, s: str) -> int:
        '''
        2 pointer approach (sliding window)
        1 pointer approach
        '''
        count = 0
        for i in range(0, len(s), 2):
            # if i == len(s) -1:
            #     if count > 0:
            #         count -= 1
            #     break
            if s[i] != s[i+1]:
                count += 1
        
        return count
        
