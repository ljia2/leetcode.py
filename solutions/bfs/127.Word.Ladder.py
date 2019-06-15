import string

# class BFSSolution: # TLE
#     def ladderLength(self, beginWord, endWord, wordList):
#         """
#
#         Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:
#
#         Only one letter can be changed at a time.
#         Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
#         Note:
#
#         Return 0 if there is no such transformation sequence.
#         All words have the same length.
#         All words contain only lowercase alphabetic characters.
#         You may assume no duplicates in the word list.
#         You may assume beginWord and endWord are non-empty and are not the same.
#         Example 1:
#
#         Input:
#         beginWord = "hit",
#         endWord = "cog",
#         wordList = ["hot","dot","dog","lot","log","cog"]
#
#         Output: 5
#
#         Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
#         return its length 5.
#         Example 2:
#
#         Input:
#         beginWord = "hit"
#         endWord = "cog"
#         wordList = ["hot","dot","dog","lot","log"]
#
#         Output: 0
#
#         Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
#
#         :type beginWord: str
#         :type endWord: str
#         :type wordList: List[str]
#         :rtype: int
#
#         shortest path hints for BFS / bidirectional BFS.
#         1) First Generate the Graph
#         2) Then BFS from beginWord
#
#         """
#         if endWord not in wordList:
#             return 0
#
#         wordDict = set(wordList)
#         step = 0
#         queue = [beginWord]
#         visited = set()
#         visited.add(beginWord)
#         while queue:
#             size = len(queue)
#             while size > 0:
#                 w = queue.pop(0)
#                 size -= 1
#                 if w == endWord:
#                     # the length is the expansion step + 1
#                     return step + 1
#                 for i in range(len(w)):
#                     for t in string.ascii_lowercase:
#                         if t == w[i]:
#                             continue
#                         new_w = w[:i] + t + w[i+1:]
#                         if new_w not in wordDict or new_w in visited:
#                             continue
#                         visited.add(new_w)
#                         queue.append(new_w)
#             step += 1
#         return 0

class BiBFSSolution: # Best Solution
    def ladderLength(self, beginWord, endWord, wordList):
        """

        Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

        Only one letter can be changed at a time.
        Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
        Note:

        Return 0 if there is no such transformation sequence.
        All words have the same length.
        All words contain only lowercase alphabetic characters.
        You may assume no duplicates in the word list.
        You may assume beginWord and endWord are non-empty and are not the same.
        Example 1:

        Input:
        beginWord = "hit",
        endWord = "cog",
        wordList = ["hot","dot","dog","lot","log","cog"]

        Output: 5

        Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
        return its length 5.
        Example 2:

        Input:
        beginWord = "hit"
        endWord = "cog"
        wordList = ["hot","dot","dog","lot","log"]

        Output: 0

        Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.

        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int

        shortest path hints for BFS / bidirectional BFS.
        1) First Generate the Graph
        2) Then BiBFS from beginWord

        """
        if endWord not in wordList:
            return 0

        step = 0
        wordDict = set(wordList)

        queue1 = [beginWord]
        visited1 = set()
        visited1.add(beginWord)

        queue2 = [endWord]
        visited2 = set()
        visited2.add(endWord)

        while queue1 and queue2:

            # always expand from smaller queue.
            if len(queue1) > len(queue2):
                qs, qb, visited = queue2, queue1, visited2
            else:
                qs, qb, visited = queue1, queue2, visited1

            # expansion from the smaller queue
            size = len(qs)
            while size > 0:
                w = qs.pop(0)
                size -= 1

                # when a word in qs appear in qb, two side bfs expansion.
                if w in qb:
                    return step + 1

                # replace a char at i with different char.
                for i in range(len(w)):
                    for c in string.ascii_lowercase:
                    # for j in range(32, 58):
                    #     c = ord(j)
                        if c == w[i]:
                            continue
                        new_w = w[:i] + c + w[i+1:]
                        if new_w not in wordDict or new_w in visited:
                            continue
                        visited.add(new_w)
                        qs.append(new_w)
            step += 1
        return 0

s = BiBFSSolution()
print(s.ladderLength("hit", "cog", ["hot","dot","dog","lot","log", "cog"]))
print(s.ladderLength("game", "thee", ["frye","heat","tree","thee","game","free","hell","fame","faye"]))
print(s.ladderLength("kiss", "tusk", ["miss","dusk","kiss","musk","tusk","diss","disk","sang","ties","muss"]))