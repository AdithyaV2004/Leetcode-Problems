class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        c={}
        for i in s:
            if i not in c:
                c[i]=0
            c[i]+=1
        for i in t:
            if i not in c:
                return False
            c[i]-=1
        for i in c:
            if c[i]!=0:
                return False
        return True
        