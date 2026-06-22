class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        diction = {}
        for i in range(len(s)):
            diction[s[i]] = diction.get(s[i], 0)+1
            diction[t[i]] = diction.get(t[i], 0)-1
        for cnt in diction.values():
            if cnt != 0:
                return False
        return True




        