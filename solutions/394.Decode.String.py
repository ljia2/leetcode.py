class Solution:
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return s
        else:
            token_stack = []
            freq_stack = []
            i = 0
            while i < len(s):
                if s[i].isnumeric():
                    freq = int(s[i])
                    while i < len(s)-1 and s[i+1].isnumeric():
                        i += 1
                        freq = freq * 10 + int(s[i])
                    freq_stack.append(freq)
                elif s[i] != ']':
                    token_stack.append(s[i])
                else:
                    freq = freq_stack.pop()
                    encode = ""
                    while token_stack:
                        token = token_stack.pop()
                        if token == '[':
                            break
                        else:
                            encode = token + encode
                    encode = "".join([encode] * freq)
                    token_stack.append(encode)
                i += 1

            return "".join(token_stack)


s = Solution()
print(s.decodeString("ab3[a12[cd]]ef"))