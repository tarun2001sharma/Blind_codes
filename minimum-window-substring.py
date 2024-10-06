class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_set = {}
        s_set = {}
        for i in t:
            t_set[i] = 1 + t_set.get(i, 0)
            s_set[i] = 0
            
        have, want = 0, len(t_set)
        l, r = 0, 0
        min_window = ""
        min_count = float("inf")

        for r in range(len(s)):
            if s[r] in t_set:
                s_set[s[r]] = 1 + s_set.get(s[r], 0)

                if s_set[s[r]] == t_set[s[r]]:
                    have += 1
            
            while have == want:
                curr = r-l+1
                if min_count >  curr:
                    min_count = curr
                    min_window = s[l:r+1]

                if s[l] in t_set:
                    if s_set[s[l]] > t_set[s[l]]:
                        s_set[s[l]] -= 1
                    elif s_set[s[l]] == t_set[s[l]]:
                        have -= 1
                        s_set[s[l]] -= 1
                l += 1
        return min_window
        

    # def minWindow(self, s: str, t: str) -> str:
    #     t_set = [0]*52

    #     for i in t:
    #         if i.islower():
    #             t_set[ord(i) - ord('a')] += 1
    #         elif i.isupper():
    #             t_set[26 + ord(i) - ord('A')] += 1

    #     l, r = 0, 0

    #     if not s:
    #         return ""
        
    #     min_substring = ""
    #     min_length = float("inf")
    #     track = [0]*52
    #     # while l < len(s):
    #     for r in range(len(s)):
    #         if s[r].islower() and track[ord(s[r]) - ord('a')] != t_set[ord(s[r]) - ord('a')]:
    #             track[ord(s[r]) - ord('a')] += 1
    #         elif s[r].isupper() and track[26 + ord(s[r]) - ord('A')] != t_set[26 + ord(s[r]) - ord('A')]:
    #             track[26 + ord(s[r]) - ord('A')] += 1
            
    #         if track == t_set:
    #             while track == t_set:
    #                 if (r-l) < min_length:
    #                     min_length = min(min_length, r-l)
    #                     min_substring = s[l:r+1]
    #                 if s[l].islower() and track[ord(s[l]) - ord('a')] > 0:
    #                     track[ord(s[l]) - ord('a')] -= 1
    #                 elif s[l].isupper() and track[26 + ord(s[l]) - ord('A')] > 0:
    #                     track[26 + ord(s[l]) - ord('A')] -= 1
    #                 l += 1
                
    #             while (s[l].islower() and track[ord(s[l]) - ord('a')] == 0) or (s[l].isupper() and track[26 + ord(s[l]) - ord('A')] == 0):
    #                 l += 1
        
    #     return min_substring

        
