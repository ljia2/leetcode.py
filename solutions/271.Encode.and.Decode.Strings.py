class Codec:

    def encode(self, strs):
        """Encodes a list of strings to a single string.
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        else:
            encoded = ""
            for s in strs:
                encoded += str(len(s)) + "/" + s
            return encoded

    def decode(self, s):
        """Decodes a single string to a list of strings.

        :type s: str
        :rtype: List[str]
        """
        if s is None:
            return []
        else:
            start = 0
            decodes = []
            while start < len(s):
                delimiter = s.index("/", start)
                length = int(s[start:delimiter])
                decodes.append(s[delimiter+1:delimiter+1+length])
                start = delimiter + 1 + length
            return decodes


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))