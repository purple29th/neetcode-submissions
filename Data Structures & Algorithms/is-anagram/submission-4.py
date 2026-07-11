class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if len(s) != len(t):
        #     return False
        # cntS, cntT = {}, {}

        # for i in range(len(s)):
        #     cntS[s[i]] = cntS.get(s[i], 0)+1
        #     cntT[t[i]] = cntT.get(t[i], 0)+1
        # for c in cntS:
        #     if cntS[c] != cntT.get(c, 0):
        #         return False
        # return True

        if len(s) != len(t):
            return False
        
        dictA, dictB = {}, {}

        for i in range(len(s)):
            dictA[s[i]] = dictA.get(s[i], 0)+1
            dictB[t[i]] = dictB.get(t[i], 0)+1
        for j in dictA:
            if dictA[j] != dictB.get(j, 0):
                return False
        return True

        
        







        