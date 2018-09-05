class Solution:
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        read = 0
        write = 0
        while read < len(chars):
            freq = 1
            while read < len(chars)-1 and chars[read+1] == chars[read]:
                read += 1
                freq += 1
            chars[write] = chars[read]
            read += 1
            write += 1
            if freq > 1:
                for c in str(freq):
                    chars[write] = c
                    write += 1

        return write

s = Solution()
print(s.compress(["a","a","a","b","b","a","a"]))