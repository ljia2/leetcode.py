class Solution:
    def lengthLongestPath(self, input):
        """
        Suppose we abstract our file system by a string in the following manner:

        The string "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" represents:

        dir
            subdir1
            subdir2
                file.ext
        The directory dir contains an empty sub-directory subdir1 and a sub-directory subdir2 containing a file file.ext.

        The string "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext" represents:

        dir
            subdir1
                file1.ext
                subsubdir1
            subdir2
                subsubdir2
                    file2.ext
        The directory dir contains two sub-directories subdir1 and subdir2. subdir1 contains a file file1.ext and an empty second-level sub-directory subsubdir1. subdir2 contains a second-level sub-directory subsubdir2 containing a file file2.ext.

        We are interested in finding the longest (number of characters) absolute path to a file within our file system. For example, in the second example above, the longest absolute path is "dir/subdir2/subsubdir2/file2.ext", and its length is 32 (not including the double quotes).

        Given a string representing the file system in the above format, return the length of the longest absolute path to file in the abstracted file system. If there is no file in the system, return 0.

        Note:
        The name of a file contains at least a . and an extension.
        The name of a directory or sub-directory will not contain a ..
        Time complexity required: O(n) where n is the size of the input string.

        Notice that a/aa/aaa/file1.txt is not the longest file path, if there is another path aaaaaaaaaaaaaaaaaaaaa/sth.png.

        :type input: str
        :rtype: int
        """
        if input == "":
            return 0
        dirstack = []
        maxlength = 0
        fields = input.split('\n')
        for field in fields:
            if self.isDir(field):
                dl, dn = self.levelName(field)
                # stack is not empty
                while dirstack:
                    ldn, ldl = dirstack[-1]
                    if ldl >= dl:
                        dirstack.pop()
                    else:
                        break
                dirstack.append((dn, dl))
            elif self.isFile(field):
                fl, fn = self.levelName(field)
                while dirstack:
                    dn, dl = dirstack[-1]
                    if dl >= fl:
                        dirstack.pop()
                    else:
                        break
                fullpath = self.composeFullpath(dirstack, fn)
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
        return "/".join(dirstack) + "/" + fn



s = Solution()
results = s.lengthLongestPath("dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext")
print(results)
results = s.lengthLongestPath("dir\n    file.txt")
print(results)