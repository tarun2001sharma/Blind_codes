class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding window: O(n) time

        if not s:
            return 0

        l, r = 0,1

        curr = set()
        curr.add(s[l])
        max_string = 1

        while r<len(s):
            while s[r] in curr:
                curr.remove(s[l])
                l+=1
            curr.add(s[r])
            r+=1
            max_string = max(max_string, len(curr))
        
        return max_string
            


        
