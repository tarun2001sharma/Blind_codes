class Solution:
    def compressedString(self, word: str) -> str:
        comp = []

        pos = 0

        while pos< len(word):
            curr = 0
            curr_char = word[pos]

            while (pos < len(word) and curr < 9 and word[pos] == curr_char):
                curr += 1
                pos += 1
            
            comp.append(str(curr))
            comp.append(curr_char)

        return "".join(comp)
