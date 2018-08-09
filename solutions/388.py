class Solution:
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        dirstack = []
        maxlength = 0
        if input == "":
            return 0
        fields = input.split('\n')
        for field in fields:
            if self.isDir(field):
                dl, dn = self.levelName(field)
                if dirstack: # stack is not empty
                    while dirstack:
                        (ldn, ldl) = dirstack[-1]
                        if ldl >= dl:
                            dirstack.pop()
                        else:
                            break
                    dirstack.append((dn, dl))
                else:
                    dirstack.append((dn, dl))
            elif self.isFile(field):
                fl, fn = self.levelName(field)
                while dirstack:
                    (dn, dl) = dirstack[-1]
                    if dl >= fl:
                        dirstack.pop()
                    else:
                        break
                fullpath = self.composeFullpath(dirstack, fn)
                print(fullpath)
                if len(fullpath) > maxlength:
                    maxlength = len(fullpath)
        return maxlength

    def levelName(self, input):
        level = 0
        for c in input:
            if c == '\t':
                level += 1
        return level, input[level:]

    def isDir(self, input):
        return input.find(".") < 0

    def isFile(self, input):
        return -1 < input.rindex(".") < len(input)-1

    def composeFullpath(self, dirstack, fn):
        fullpath = ""
        for (d, l) in dirstack:
            fullpath += d + "/"
        return fullpath + fn



def main():
    s = Solution()
    results = s.lengthLongestPath("dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext")
    print(results)
    results = s.lengthLongestPath("dir\n    file.txt")
    print(results)

if __name__ == "__main__":
    main()