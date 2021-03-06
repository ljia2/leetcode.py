class Solution(object):
    def stringComparsion(self, s, t):
        if not s or not t:
            raise Exception("Invalid Input!")

        ls, lt = len(s), len(t)

        # # s <= t
        # if ls < lt and s == t[:ls]:
        #     return -1
        # # s >= t
        # if ls > lt and s[:lt] == t:
        #     return 1
        # # s == t
        # if ls == lt and s == t:
        #     return 0

        i = j = 0
        while i < ls and j < lt:
            ts, i = self.nextToken(s, i)
            tt, j = self.nextToken(t, j)

            if ts.isalpha() and tt.isnumeric():
                return -1
            elif ts.isnumeric() and tt.isalpha():
                return 1
            else:
                if ts.isalpha() and tt.isalpha():
                    if ts < tt:
                        return -1
                    elif ts > tt:
                        return 1
                else:
                    its, itt = int(ts), int(tt)
                    if its < itt:
                        return -1
                    elif its > itt:
                        return 1

        if i == ls and j == lt:
            return 0
        elif i == ls and j < lt:
            return -1
        else:
            return 1

    def nextToken(self, s, start):
        if s[start].isnumeric():
            end = start
            while end + 1 < len(s) and s[end+1].isnumeric():
                end += 1
            return s[start:end+1], end + 1
        else:
            return s[start], start + 1

s = Solution()
print(s.stringComparsion("aa99bb", "aa100cc"))
print(s.stringComparsion("a007b", "a7b"))