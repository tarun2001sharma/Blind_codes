class Solution:
    # O(n) solution
    def isPalindrome(self, s: str) -> bool:
        upperS = s.upper()
        clean = [char for char in upperS if char.isalnum()]

        front = 0
        back = len(clean) - 1

        while front <= back:
            if clean[front] != clean[back]:
                return False
            front += 1
            back -= 1
        
        return True

# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         l, r = 0, len(s) - 1

#         while l < r:

#             while l < r and not s[l].isalnum():
#                 l += 1
#             while l < r and not s[r].isalnum():
#                 r -= 1
            
#             if s[l].lower() != s[r].lower():
#                 return False
            
#             l += 1
#             r -= 1

#         return True

        
