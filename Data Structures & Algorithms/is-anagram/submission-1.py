class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if s and t:
            s = sorted(s)
            t = sorted(t)
            if s == t:
                return True 
            else:return False
        else: return False
        