from collections import defaultdict

class UnionFindSolution:
    def accountsMerge(self, accounts):
        """
        Given a list accounts, each element accounts[i] is a list of strings,
        where the first element accounts[i][0] is a name,
        and the rest of the elements are emails representing emails of the account.

        Now, we would like to merge these accounts.
        Two accounts definitely belong to the same person if there is some email that is common to both accounts.
        Note that even if two accounts have the same name, they may belong to different people as people could have the same name.
        A person can have any number of accounts initially, but all of their accounts definitely have the same name.

        After merging the accounts, return the accounts in the following format:
        the first element of each account is the name, and the rest of the elements are emails in sorted order.
        The accounts themselves can be returned in any order.

        Example 1:
        Input:
        accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
        Output: [["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'],  ["John", "johnnybravo@mail.com"], ["Mary", "mary@mail.com"]]

        Explanation:
        The first and third John's are the same person as they have the common email "johnsmith@mail.com".
        The second John and Mary are different people as none of their email addresses are used by other accounts.
        We could return these lists in any order, for example the answer [['Mary', 'mary@mail.com'], ['John', 'johnnybravo@mail.com'],
        ['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']] would still be accepted.

        Note:

        The length of accounts will be in the range [1, 1000].
        The length of accounts[i] will be in the range [1, 10].
        The length of accounts[i][j] will be in the range [1, 30].

        :type accounts: List[List[str]]
        :rtype: List[List[str]]

        Union Find Algorithm.

        """
        num = len(accounts)
        parents = [i for i in range(num)]
        ranks = [1] * num

        index2name = defaultdict(str)
        index2emails = defaultdict(set)
        for index in range(num):
            name, emails = accounts[index][0], accounts[index][1:],
            index2name[index] = name
            index2emails[index] = set(emails)

        # compare each pair of account, they are the same, if 1) the same name and 2) share at least 1 common email;
        for index1 in range(num):
            for index2 in range(index1, num):
                if index2name[index1] == index2name[index2] and index2emails[index1].intersection(index2emails[index2]):
                    p1 = self.find(parents, index1)
                    p2 = self.find(parents, index2)

                    if p1 == p2:
                        continue

                    if ranks[p1] > ranks[p2]:
                        p1, p2 = p2, p1

                    parents[p1] = p2
                    ranks[p2] += ranks[p1]

        mergedemails = defaultdict(set)
        for index in range(num):
            pi = self.find(parents, index)
            newemails = index2emails[index]
            mergedemails[pi] = mergedemails[pi].union(newemails)

        ans = []
        for (index, emails) in mergedemails.items():
            ans.append([index2name[index]] + sorted(emails))
        return ans

    def find(self, parents, s):
        while s != parents[s]:
            parents[s] = parents[parents[s]]
            s = parents[s]
        return s

s = UnionFindSolution()
print(s.accountsMerge([["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]))