class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d={}
        m=0
        for i in s:
            d[i]=0
        l, r=0, 0
        while l<=r and r<len(s):
            d[s[r]]+=1
            while d[s[r]]>1:
                d[s[l]]-=1
                l+=1    
            m=max(m, r-l+1)
            r+=1
        return m
            

