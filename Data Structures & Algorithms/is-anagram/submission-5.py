class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dictA, dictB = {}, {}

        for keys in range(len(s)):
            dictA[s[keys]] = dictA.get(s[keys], 0)+1
            dictB[t[keys]] = dictB.get(t[keys], 0)+1
        for i in dictA:
            if dictA[i] != dictB.get(i, 0):
                return False
        return True

        
        







        