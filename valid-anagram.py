class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sdict = {}
        tdict = {}
        for i in range(len(s)):
            sdict[s[i]] = 1 + sdict.get(s[i], 0)
            tdict[t[i]] = 1 + tdict.get(t[i], 0)
        
        for i in range(len(s)):
            if sdict[s[i]] != tdict.get(s[i], 0):
                return False
        return True
