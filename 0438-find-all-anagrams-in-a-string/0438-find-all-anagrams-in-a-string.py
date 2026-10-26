class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        if len(p)>len(s): return []
        d={}
        ind=[]
        n=len(p)
        nd=dict(Counter(p))
        for i in range(n):
            if s[i] not in d:
                d[s[i]]=0
            d[s[i]]+=1
        l, r=0, n-1
        while True:
            if d==nd: ind.append(l)
            if r+1>=len(s): break
            if s[r+1] not in d:
                d[s[r+1]]=0
            d[s[r+1]]+=1
            d[s[l]]-=1
            if d[s[l]]==0: del d[s[l]]
            l, r = l+1, r+1
        return ind