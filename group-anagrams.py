class Solution:
    def sortString(self, s: str) -> str:
        count = [0]*26
        for i in s:
            count[ord(i)-ord('a')] += 1
        
        ans = []
        for i in range(26):
            ans.append(chr(ord('a') + i)*count[i])
        
        return ''.join(ans)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        track = {}
        for i in strs:
            new = self.sortString(i)
            # new = str(sorted(i))
            if new not in track:
                track[new] = [i]
            else:
                track[new].append(i)
        
        final = []
        return list(track.values())
            
        
