import string
from collections import defaultdict

class BFSSolution:
    def findLadders(self, beginWord, endWord, wordList):
        """

        Given two words (beginWord and endWord), and a dictionary's word list, find all shortest transformation sequence(s) from beginWord to endWord, such that:

        Only one letter can be changed at a time
        Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
        Note:

        Return an empty list if there is no such transformation sequence.
        All words have the same length.
        All words contain only lowercase alphabetic characters.
        You may assume no duplicates in the word list.
        You may assume beginWord and endWord are non-empty and are not the same.
        Example 1:

        Input:
        beginWord = "hit",
        endWord = "cog",
        wordList = ["hot","dot","dog","lot","log","cog"]

        Output:
        [
          ["hit","hot","dot","dog","cog"],
          ["hit","hot","lot","log","cog"]
        ]
        Example 2:

        Input:
        beginWord = "hit"
        endWord = "cog"
        wordList = ["hot","dot","dog","lot","log"]

        Output: []

        Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.

        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]

        use BFS to build the whole graph, and then back track the graph to generated all transformations.

        """

        if endWord not in wordList or not wordList:
            return []

        wordDict = set(wordList)

        # during the expansion, records a word's parents.
        parents = defaultdict(list)

        # initialize queue and visited (set) for BFS.
        queue = [beginWord]
        visited = set()
        visited.add(beginWord)

        # records the steps from beginWord to a word
        steps = dict()
        steps[beginWord] = 1

        found = False
        while queue and not found:
            size = len(queue)
            while size > 0:
                word = queue.pop(0)
                step = steps[word]

                if word == endWord:
                    found = True
                    break

                for i in range(len(word)):
                    for c in string.ascii_lowercase:
                        if c == word[i]:
                            continue
                        new_word = word[:i] + c + word[i+1:]

                        # if new_word has been used before
                        if new_word in steps.keys():
                            # new_word has been used by some other path before.
                            # with the same number of steps.
                            # word is a new parent of new_step.
                            if step < steps[new_word]:
                                parents[new_word].append(word)
                        else:
                            if new_word not in wordDict or new_word in visited:
                                continue
                            visited.add(new_word)
                            parents[new_word].append(word)
                            steps[new_word] = steps[word] + 1
                            queue.append(new_word)
        if found:
            results = []
            self.getPaths(parents, endWord, beginWord, [endWord], results)
            return results
        else:
            return []

    # backtracking via DFS over graph to get paths (reversed paths)
    def getPaths(self, graph, start, end, path, ans):
        if start == end:
            p = path.copy()
            p.reverse()
            ans.append(p)
            return
        parents = graph[start]
        for p in parents:
            path.append(p)
            self.getPaths(graph, p, end, path, ans)
            path.pop()
        return

# class BiBFSSolution: # FASTER
#     def findLadders(self, beginWord, endWord, wordList):
#         """
#
#         Given two words (beginWord and endWord), and a dictionary's word list, find all shortest transformation sequence(s)
#         from beginWord to endWord, such that: Only one letter can be changed at a time
#         Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
#
#         Note:
#
#         Return an empty list if there is no such transformation sequence.
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
#         Output:
#         [
#           ["hit","hot","dot","dog","cog"],
#           ["hit","hot","lot","log","cog"]
#         ]
#         Example 2:
#
#         Input:
#         beginWord = "hit"
#         endWord = "cog"
#         wordList = ["hot","dot","dog","lot","log"]
#
#         Output: []
#
#         Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
#
#         :type beginWord: str
#         :type endWord: str
#         :type wordList: List[str]
#         :rtype: List[List[str]]
#         """
#         if endWord not in wordList or not wordList:
#             return []
#
#         wordDict = set(wordList)
#         # Note That the queues are dictionary where key is the words and value is the list of paths,
#         # because there are multiple paths from begin to end
#         q1 = {beginWord: [[beginWord]]}
#         q2 = {endWord: [[endWord]]}
#         results = []
#         while q1 and q2:
#             qs, qb = (q1, q2) if len(q1) < len(q2) else (q2, q1)
#             next_level = dict()
#             for (w, paths) in qs.items():
#                 for i in range(len(w)):
#                     t = w[i]
#                     for c in string.ascii_lowercase:
#                         if c == t:
#                             continue
#                         nw = w[:i] + c + w[i+1:]
#                         # only expand dictionary word
#                         if nw not in wordDict:
#                             continue
#
#                         # avoid revisit
#                         for path in paths:
#                             if nw in path:
#                                 continue
#                             if nw in qb.keys():
#                                 if beginWord in path:
#                                     for pp in qb[nw]:
#                                         results.append(path + pp)
#                                 else:
#                                     for pp in qb[nw]:
#                                         results.append(pp + path)
#                             else:
#                                 if beginWord in path:
#                                     if nw in next_level.keys():
#                                         next_level[nw].append(path + [nw])
#                                     else:
#                                         next_level[nw] = [path + [nw]]
#                                 else:
#
#                                     if nw in next_level.keys():
#                                         next_level[nw].append([nw] + path)
#                                     else:
#                                         next_level[nw] = [[nw] + path]
#             if not results:
#                 if qs is q1:
#                     q1 = next_level
#                 else:
#                     q2 = next_level
#             else:
#                 return results
#         return []

s = BFSSolution()
print(s.findLadders("hit", "cog", ["hot","dot","dog","lot","log","cog"]))
#print(s.findLadders("magic","pearl",["flail","halon","lexus","joint","pears","slabs","lorie","lapse","wroth","yalow","swear","cavil","piety","yogis","dhaka","laxer","tatum","provo","truss","tends","deana","dried","hutch","basho","flyby","miler","fries","floes","lingo","wider","scary","marks","perry","igloo","melts","lanny","satan","foamy","perks","denim","plugs","cloak","cyril","women","issue","rocky","marry","trash","merry","topic","hicks","dicky","prado","casio","lapel","diane","serer","paige","parry","elope","balds","dated","copra","earth","marty","slake","balms","daryl","loves","civet","sweat","daley","touch","maria","dacca","muggy","chore","felix","ogled","acids","terse","cults","darla","snubs","boats","recta","cohan","purse","joist","grosz","sheri","steam","manic","luisa","gluts","spits","boxer","abner","cooke","scowl","kenya","hasps","roger","edwin","black","terns","folks","demur","dingo","party","brian","numbs","forgo","gunny","waled","bucks","titan","ruffs","pizza","ravel","poole","suits","stoic","segre","white","lemur","belts","scums","parks","gusts","ozark","umped","heard","lorna","emile","orbit","onset","cruet","amiss","fumed","gelds","italy","rakes","loxed","kilts","mania","tombs","gaped","merge","molar","smith","tangs","misty","wefts","yawns","smile","scuff","width","paris","coded","sodom","shits","benny","pudgy","mayer","peary","curve","tulsa","ramos","thick","dogie","gourd","strop","ahmad","clove","tract","calyx","maris","wants","lipid","pearl","maybe","banjo","south","blend","diana","lanai","waged","shari","magic","duchy","decca","wried","maine","nutty","turns","satyr","holds","finks","twits","peaks","teems","peace","melon","czars","robby","tabby","shove","minty","marta","dregs","lacks","casts","aruba","stall","nurse","jewry","knuth"]))




