class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if len(s) != len(t):
            return False

        else:
            countS, countT = {}, {}
            for i in range(len(s)):
                countS[s[i]] = 1+ countS.get(s[i], 0)
                countT[t[i]] = 1+ countT.get(t[i], 0)

            for t in countT:
                if countT[t] != countS.get(t, 0):
                    return False

        return True

        
        