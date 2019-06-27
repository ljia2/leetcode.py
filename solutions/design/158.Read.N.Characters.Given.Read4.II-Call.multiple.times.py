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

class Solution(object):
    def __init__(self):
        # if self.buff4_idx < 4, then we have unread chars in self.buff4.
        self.buff4_idx = 4
        self.buff4_len = 0
        self.buff4 = [""] * 4

    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        idx = 0
        while idx < n:
            if self.buff4_idx == 4:
                self.buff4_len = read4(self.buff4)
                self.buff4_idx = 0

            if self.buff4_len == 0:
                break

            # copy char by char from self.buff4[self.buff4_idx:self.buff4_len] to buf
            while idx < n and self.buff4_idx < self.buff4_len:
                buf[idx] = self.buff4[self.buff4_idx]
                idx += 1
                self.buff4_idx += 1

            # exhaust the buff4 and set the buff4_idx to 4, for next call we can exit while loop.
            if self.buff4_idx == self.buff4_len:
                self.buff4_idx = 4

        return idx















