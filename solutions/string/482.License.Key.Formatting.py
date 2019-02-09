class Solution:
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        cleanS = ''.join(S.split("-"))
        s1 = K if len(cleanS) % K == 0 else len(cleanS)%K
        res = cleanS[:s1]
        while s1 < len(cleanS):
            res += '-' + cleanS[s1:s1+K]
            s1 += K
        return res.upper()


