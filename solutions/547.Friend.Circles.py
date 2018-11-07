from collections import defaultdict

class DFSSolution:
    def findCircleNum(self, M):
        """
        There are N students in a class. Some of them are friends, while some are not.
        Their friendship is transitive in nature.
        For example, if A is a direct friend of B, and B is a direct friend of C, then A is an indirect friend of C.
        And we defined a friend circle is a group of students who are direct or indirect friends.

        Given a N*N matrix M representing the friend relationship between students in the class.
        If M[i][j] = 1, then the ith and jth students are direct friends with each other, otherwise not.
        And you have to output the total number of friend circles among all the students.

        Example 1:
        Input:
        [[1,1,0],
         [1,1,0],
         [0,0,1]]
        Output: 2
        Explanation:The 0th and 1st students are direct friends, so they are in a friend circle.
        The 2nd student himself is in a friend circle. So return 2.

        Example 2:
        Input:
        [[1,1,0],
         [1,1,1],
         [0,1,1]]
        Output: 1
        Explanation:The 0th and 1st students are direct friends, the 1st and 2nd students are direct friends,
        so the 0th and 2nd students are indirect friends. All of them are in the same friend circle, so return 1.

        Note:
        N is in range [1,200].
        M[i][i] = 1 for all students.
        If M[i][j] = 1, then M[j][i] = 1.

        :type M: List[List[int]]
        :rtype: int

        Use DFS to find the number of connected components.

        However, we need convert matrix to graph!!!!!

        """

        if not M or not M[0]:
            return 0

        graph = defaultdict(list)
        visited = [False] * len(M)
        for r in range(len(M)):
            for c in range(len(M[0])):
                if M[r][c] == 1:
                    graph[r].append(c)
        ans = 0
        for p in graph.keys():
            if not visited[p]:
                ans += 1 if self.dfs(graph, p, visited) else 0
        return ans

    def dfs(self, graph, p, visited):
        if visited[p]:
            return False
        visited[p] = True
        for friend in graph[p]:
            self.dfs(graph, friend, visited)
        return True


class DFSSolutionII:
    def findCircleNum(self, M):
        """
        There are N students in a class. Some of them are friends, while some are not.
        Their friendship is transitive in nature.
        For example, if A is a direct friend of B, and B is a direct friend of C, then A is an indirect friend of C.
        And we defined a friend circle is a group of students who are direct or indirect friends.

        Given a N*N matrix M representing the friend relationship between students in the class.
        If M[i][j] = 1, then the ith and jth students are direct friends with each other, otherwise not.
        And you have to output the total number of friend circles among all the students.

        Example 1:
        Input:
        [[1,1,0],
         [1,1,0],
         [0,0,1]]
        Output: 2
        Explanation:The 0th and 1st students are direct friends, so they are in a friend circle.
        The 2nd student himself is in a friend circle. So return 2.

        Example 2:
        Input:
        [[1,1,0],
         [1,1,1],
         [0,1,1]]
        Output: 1
        Explanation:The 0th and 1st students are direct friends, the 1st and 2nd students are direct friends,
        so the 0th and 2nd students are indirect friends. All of them are in the same friend circle, so return 1.

        Note:
        N is in range [1,200].
        M[i][i] = 1 for all students.
        If M[i][j] = 1, then M[j][i] = 1.

        :type M: List[List[int]]
        :rtype: int

        Use DFS to find the number of connected components.

        What if directly dfs over M?

        """

        if not M or not M[0]:
            return 0
        n = len(M)
        visited = [False] * n
        ans = 0
        for p in range(n):
            ans += 1 if self.dfs(M, p, n, visited) else 0
        return ans

    def dfs(self, M, p, n, visited):
        if visited[p]:
            return False

        visited[p] = True
        for i in range(n):
            if visited[i] or i == p:
                continue
            if M[p][i] == 1:
                self.dfs(M, i, n, visited)
        return True

s = DFSSolutionII()
print(s.findCircleNum([[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]))