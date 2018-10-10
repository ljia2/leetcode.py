import string

class BFSSolution:
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
        2) Then BFS from beginWord

        """
        if endWord not in wordList:
            return 0

        wordDict = set(wordList)
        if beginWord in wordDict:
            wordDict.remove(beginWord) # remove beginWord since queue is initialize with beginWord
        step = 0
        queue = [beginWord]
        while queue:
            step += 1
            next_level = []
            while queue:
                w = queue.pop(0)
                for i in range(len(w)):
                    c = w[i]
                    for t in string.ascii_lowercase:
                        if t == c:
                            continue
                        new_w = w[:i] + t + w[i+1:]
                        if new_w not in wordDict:
                            continue
                        if new_w == endWord:
                            return step + 1
                        # BFS, if a word is removed from dict, which is one step aways from beginWord. Further steps should avoid to use them.
                        wordDict.remove(new_w)
                        next_level.append(new_w)
            queue.extend(next_level)
        return 0

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
        wordDict1 = set(wordList)
        wordDict2 = set(wordList)
        queue1 = [beginWord]
        queue2 = [endWord]

        if beginWord in wordDict1:
            wordDict1.remove(beginWord)
        if endWord in wordDict2:
            wordDict2.remove(endWord)

        while queue1 and queue2:
            qs, qb, wdict = (queue2, queue1, wordDict2) if len(queue1) > len(queue2) else (queue1, queue2, wordDict1)
            # step records how many times of expansions from either side
            step += 1
            # expand the smaller queue
            next_level = []
            # iterate all the words from qs (they are the same distance from beginword)
            while qs:
                w = qs.pop(0)
                for i in range(len(w)):
                    c = w[i]
                    for t in string.ascii_lowercase:
                        if t == c:
                            continue
                        new_w = w[:i] + t + w[i+1:]
                        if new_w not in wdict:
                            continue
                        if new_w in qb:
                            return step + 1
                        # BFS, if a word is removed from dict, which is one step aways from beginWord. Further steps should avoid to use them.
                        wdict.remove(new_w)
                        next_level.append(new_w)
            qs.extend(next_level)
        return 0

s = BiBFSSolution()
#print(s.ladderLength("hit", "cog", ["hot","dot","dog","lot","log", "cog"]))
#print(s.ladderLength("game", "thee", ["frye","heat","tree","thee","game","free","hell","fame","faye"]))
print(s.ladderLength("kiss", "tusk", ["miss","dusk","kiss","musk","tusk","diss","disk","sang","ties","muss"]))