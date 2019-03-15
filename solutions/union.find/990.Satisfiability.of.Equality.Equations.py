class Solution(object):
    def equationsPossible(self, equations):
        """
        Given an array equations of strings that represent relationships between variables,
        each string equations[i] has length 4 and takes one of two different forms: "a==b" or "a!=b".
        Here, a and b are lowercase letters (not necessarily different) that represent one-letter variable names.

        Return true if and only if it is possible to assign integers to variable names so as to satisfy all the given equations.

        Example 1:

        Input: ["a==b","b!=a"]
        Output: false
        Explanation: If we assign say, a = 1 and b = 1, then the first equation is satisfied, but not the second.
        There is no way to assign the variables to satisfy both equations.

        Example 2:

        Input: ["b==a","a==b"]
        Output: true
        Explanation: We could assign a = 1 and b = 1 to satisfy both equations.

        Example 3:

        Input: ["a==b","b==c","a==c"]
        Output: true

        Example 4:

        Input: ["a==b","b!=c","c==a"]
        Output: false

        Example 5:

        Input: ["c==c","b==d","x!=z"]
        Output: true

        Note:

        1 <= equations.length <= 500
        equations[i].length == 4
        equations[i][0] and equations[i][3] are lowercase letters
        equations[i][1] is either '=' or '!'
        equations[i][2] is '='

        :type equations: List[str]
        :rtype: bool
        """

        if not equations:
            return True

        var2index = dict()
        for equation in equations:
            x, sign, y = equation[0], equation[1:3], equation[3]
            if sign == '!=' and x == y:
                return False
            if x not in var2index.keys():
                var2index[x] = len(var2index.keys())
            if y not in var2index.keys():
                var2index[y] = len(var2index.keys())


        parents = [i for i in range(len(var2index.keys()))]
        sizes = [1 for _ in range(len(var2index.keys()))]

        for equation in equations:
            x, sign, y = equation[0], equation[1:3], equation[3]
            if sign == '==':
                self.union(parents, sizes, var2index[x], var2index[y])

        for equation in equations:
            x, sign, y = equation[0], equation[1:3], equation[3]
            if sign == '!=':
                px = self.find(parents, var2index[x])
                py = self.find(parents, var2index[y])
                if px == py:
                    return False
        return True

    def union(self, parents, sizes, x, y):
        px = self.find(parents, x)
        py = self.find(parents, y)
        if px == py:
            return

        if sizes[px] > sizes[py]:
            px, py = py, px

        parents[px] = py
        sizes[py] += sizes[px]
        return

    def find(self, parents, s):
        while s != parents[s]:
            parents[s] = parents[parents[s]]
            s = parents[s]
        return s

s = Solution()
print(s.equationsPossible(["a==b","b!=c","c==a"]))
print(s.equationsPossible(["c==c","b==d","x!=z"]))
print(s.equationsPossible(["a!=b","b!=c","c!=a"]))
print(s.equationsPossible(["f==a","a==b","f!=e","a==c","b==e","c==f"]))

