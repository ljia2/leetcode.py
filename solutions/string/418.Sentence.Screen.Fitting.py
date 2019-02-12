# class Solution:
#     def wordsTyping(self, sentence, rows, cols):
#         """
#         :type sentence: List[str]
#         :type rows: int
#         :type cols: int
#         :rtype: int
#         """
#         word_index = 0
#         r = 0
#         c = 0
#         sent_cnt = 0
#         while r < rows:
#             if c + len(sentence[word_index]) + 1 < cols:
#                 c += len(sentence[word_index]) + 1
#                 word_index += 1
#                 if word_index % len(sentence) == 0:
#                     sent_cnt += 1
#                     word_index = 0
#             elif c + len(sentence[word_index]) + 1 == cols or c + len(sentence[word_index]) == cols:
#                 c = 0
#                 r += 1
#                 word_index += 1
#                 if word_index % len(sentence) == 0:
#                     sent_cnt += 1
#                     word_index = 0
#             else:
#                 c = 0
#                 r += 1
#
#         return sent_cnt
#
#
# class SolutionII:
#     def wordsTyping(self, sentence, rows, cols):
#         """
#         :type sentence: List[str]
#         :type rows: int
#         :type cols: int
#         :rtype: int
#         """
#         sent_length = sum([len(word) + 1 for word in sentence])
#         r = 0
#         c = 0
#         result = 0
#
#         while r < rows:
#             sent_cnt, c = self.typingSentence(sent_length, c, cols)
#             result += sent_cnt
#             if c == cols:
#                 r += 1
#                 c = 0
#             else:
#                 # starting typing sentence word by word from c
#                 word_index = 0
#                 while r < rows:
#                     if c + len(sentence[word_index]) + 1 < cols:
#                         c += len(sentence[word_index]) + 1
#                         word_index += 1
#                         if word_index % len(sentence) == 0:
#                             result += 1
#                             break # when finish typing a sentence, starting typing sentence again.
#                     elif cols - 1 <= c + len(sentence[word_index]) <= cols:
#                         c = 0
#                         r += 1
#                         word_index += 1
#                         if word_index % len(sentence) == 0:
#                             result += 1
#                             break # when finish typing a sentence, starting typing sentence again.
#                     else:
#                         c = 0
#                         r += 1
#         return result
#
#     def typingSentence(self, sent_length, start_col, col_num):
#         sent_cnt = (col_num - start_col) // sent_length
#         next_write_column = start_col + sent_cnt * sent_length
#         if col_num - next_write_column < sent_length - 1:
#             return sent_cnt, next_write_column
#         else:
#             return sent_cnt + 1, col_num
#
#

class Solution:
    """

    """
    def wordsTyping(self, sentence, rows, cols):
        """
        Given a rows x cols screen and a sentence represented by a list of non-empty words, find how many times the given sentence can be fitted on the screen.

        Note:

        A word cannot be split into two lines.
        The order of words in the sentence must remain unchanged.
        Two consecutive words in a line must be separated by a single space.
        Total words in the sentence won't exceed 100.
        Length of each word is greater than 0 and won't exceed 10.
        1 ≤ rows, cols ≤ 20,000.
        Example 1:

        Input:
        rows = 2, cols = 8, sentence = ["hello", "world"]

        Output:
        1

        Explanation:
        hello---
        world---

        The character '-' signifies an empty space on the screen.
        Example 2:

        Input:
        rows = 3, cols = 6, sentence = ["a", "bcd", "e"]

        Output:
        2

        Explanation:
        a-bcd-
        e-a---
        bcd-e-

        The character '-' signifies an empty space on the screen.
        Example 3:

        Input:
        rows = 4, cols = 5, sentence = ["I", "had", "apple", "pie"]

        Output:
        1

        Explanation:
        I-had
        apple
        pie-I
        had--

        The character '-' signifies an empty space on the screen.
        :type sentence: List[str]
        :type rows: int
        :type cols: int
        :rtype: int

        concatenate them into one long string with extra space after each string.

        for example, [“abc”, “de”, “f”] → String s: abc de f

        len: the total length of s with white space

        count: how many valid chars have been put so far

        Now, the goal is to find: count/len, how many times the s appears

        We can use a greedy approach: looking for MAXIMUM time the given sentence can be fitted.
        We can try to put as many words in one line as possible, then trim the tailing words don’t fit in that line as a whole,
        leaving remaining positions as spaces.
        For example, we put “abc de “(6 column, so 6 chars) in the first row, and check the 7th char.

        If it’s space, means we successfully fill the first row. We fit 6 chars so far, and the 8th char can be put on next row,
        so in total there are 6+1=7 chars.

        If it’s not space, then it means it’s in middle of words. We check one step left to see if it’s space.
        If it’s space then we just keep the current count. If not, we have to keep moving left one char by one char,
        (at the same time decrease the count) until we find a space.

        """
        sent = " ".join(sentence) + " "
        size = len(sent)
        count = 0
        # for each row, try to write all columns to see where next writing position ends.
        for r in range(rows):
            count += cols
            # next writing position is space, SUCCESS for all columns in that row.
            if sent[count % size] == ' ':
                count += 1 # count += 1 to seek next word for next row
            elif sent[count % size] != ' ':
                # column writing ends within a word. Retreat until encounter a space.
                while count > 0 and sent[(count - 1) % size] != ' ':
                    count -= 1
        return count // size



s = Solution()
print(s.wordsTyping(["hello", "world"], 2, 8))


