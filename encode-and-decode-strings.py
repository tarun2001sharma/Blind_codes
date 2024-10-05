class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        encodedstr = ""
        for s in strs:
            encodedstr += f"{len(s)}#{s}"
        return encodedstr
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        decoded_list = []
        i = 0
        while i<len(s):
            j = i
            while s[j] != '#':
                j += 1
            tr = int(s[i:j])
            i = j + 1
            decoded_list.append(s[i: i+tr])
            i+= tr
        return decoded_list
            
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
