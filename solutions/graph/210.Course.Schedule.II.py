import collections

class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        There are a total of n courses you have to take, labeled from 0 to n-1.

        Some courses may have prerequisites, for example to take course 0 you have to first take course 1,
        which is expressed as a pair: [0,1]

        Given the total number of courses and a list of prerequisite pairs,
        return the ordering of courses you should take to finish all courses.

        There may be multiple correct orders, you just need to return one of them.
        If it is impossible to finish all courses, return an empty array.

        Example 1:

        Input: 2, [[1,0]]
        Output: [0,1]
        Explanation: There are a total of 2 courses to take. To take course 1 you should have finished
                     course 0. So the correct course order is [0,1] .
        Example 2:

        Input: 4, [[1,0],[2,0],[3,1],[3,2]]
        Output: [0,1,2,3] or [0,2,1,3]
        Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both
                     courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
                     So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3] .
        Note:

        The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
        You may assume that there are no duplicate edges in the input prerequisites.

        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]

        typical toplogical sorting

        """

        if not numCourses:
            return []

        if not prerequisites:
            return [i for i in range(numCourses)]

        indict, graph, cnum = self.build_graph(prerequisites)

        # all courses without in-degree
        queue = [i for i in range(numCourses) if i not in indict.keys()]
        ans = []
        courses = 0
        while queue:
            size = len(queue)
            while size > 0:
                c = queue.pop(0)
                size -= 1

                if c in ans:
                    circle = True
                    break

                ans.append(c)
                courses += 1

                if c not in graph.keys():
                    continue

                clist = graph[c]
                for d in clist:
                    indict[d] -= 1
                    if indict[d] == 0:
                        queue.append(d)
                        indict.pop(d)
        if len(ans) != numCourses:
            return []
        else:
            return ans

    def build_graph(self, prerequisites):
        courses = set()
        indict = dict()
        outdict = collections.defaultdict(list)
        for c, p in prerequisites:
            indict[c] = indict.get(c, 0) + 1
            outdict[p].append(c)
            courses.add(c)
            courses.add(p)
        return indict, outdict, len(courses)

s = Solution()
print(s.findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))
print(s.findOrder(3, [[1, 0]]))