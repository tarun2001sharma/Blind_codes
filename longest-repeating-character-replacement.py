class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Initialize variables
        left = 0
        max_count = 0  # Max frequency of any single character in the current window
        freq = [0] * 26  # Array to count frequency of letters in the current window

        # Iterate with the right pointer
        for right in range(len(s)):
            # Update the frequency of the current character
            freq[ord(s[right]) - ord('A')] += 1
            
            # Update the max_count of the most frequent character in the window
            max_count = max(max_count, freq[ord(s[right]) - ord('A')])
            
            # If the window is invalid, shrink it by moving the left pointer
            if (right - left + 1) - max_count > k:
                freq[ord(s[left]) - ord('A')] -= 1
                left += 1  # Move the left pointer to shrink the window
            
        # The length of the largest valid window
        return len(s) - left


# class Solution:
#     def characterReplacement(self, s: str, k: int) -> int:

#         char_count = [0]*26
#         l, r = 0, 0
#         curr = 0
#         longest_substring = 0

#         while r < len(s):
#             if sum(char_count) - curr < k:
#                 char_count[ord(s[r]) - ord('A')] += 1
#                 curr = max(char_count)
#                 r += 1
            
#             elif char_count[ord(s[r]) - ord('A')] == curr:
#                 char_count[ord(s[r]) - ord('A')] += 1
#                 curr = max(char_count)
#                 r += 1
                
#             else:
#                 char_count[ord(s[l]) - ord('A')] -= 1
#                 curr = max(char_count)
#                 l += 1

#             longest_substring = max(longest_substring, sum(char_count))
        
#         return longest_substring
        
        
