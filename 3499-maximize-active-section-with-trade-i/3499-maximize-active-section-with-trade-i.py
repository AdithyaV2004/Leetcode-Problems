class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        n=len(s)
        z=[]
        oc=0
        i=0
        while i<n:
            if s[i]=='0':
                j=i
                while j<n and s[j]==s[i]: j+=1
                z.append(j-i)
                i=j
            else:
                oc+=1
                i+=1
        if len(z)<2: return oc
        maxz=0
        for i in range(1, len(z)):
            maxz=max(maxz, z[i]+z[i-1])
        return oc+maxz



          