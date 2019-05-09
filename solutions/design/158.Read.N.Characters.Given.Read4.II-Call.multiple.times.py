"""
The read4 API is already defined for you.

    @param buf, a list of characters
    @return an integer
    def read4(buf):

# Below is an example of how the read4 API can be called.
file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
buf = [' '] * 4 # Create buffer with enough space to store characters
read4(buf) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
read4(buf) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
read4(buf) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file
"""
import copy

class Solution(object):
    def __init__(self):
        self.buff = []
        self.buff4 = [""] * 4

    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        if n < len(self.buff):
            buf = copy.copy(self.buff[:n])
            self.buff = self.buff[n:]
        else:
            count = n - len(self.buff)
            while count > 0:

                l = read4(self.buff4)
                if l == 4:
                    self.buff += copy.copy(self.buff4)
                    count -= 4
                else:
                    if l > 0:
                        self.buff += copy.copy(self.buff4[:l])
                    count -= l
                    break
            # 1) count > 0 -> reaching end already.
            # 2) count == 0 -> get n characters exampley
            if count >= 0:
                buf = copy.copy(self.buff)
                self.buff = []
            else:
                # get more than n characters, use the first n
                buf = copy.copy(self.buff[:n])
                self.buff = self.buff[n:]
        return len(buf)













